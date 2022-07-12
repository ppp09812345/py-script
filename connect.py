from netmiko import ConnectHandler
from xlutils.copy import copy
import re
import xlwt
import xlrd

def getall(ip):
    hw = {
            'device_type': 'huawei',
            'host': ip,
            # 用户名
            'username': '在此输入用户名',
            # 密码
            'password': '在此输入密码',
    }
    net_connect = ConnectHandler(**hw)
    # 输入命令
    arplist = net_connect.send_command('dis arp all | include GE')
    # 匹配每一行
    abc = u"(.+GE.+)"
    arpall = re.compile(abc)
    result =arpall.findall(arplist)
    for i in range(len(result)):
        #print(i)
        # ip列表
        iplist = re.findall(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b',result[i])
        # mac列表
        maclist = re.findall(r'[0-9a-f]{4,4}-[0-9a-f]{4,4}-[0-9a-f]{4,4}',result[i])
        # 端口列表
        interfacelist = re.findall(r'GE[0-9]{1,3}/[0-9]{1,3}/[0-9]{1,3}',result[i])
        # vpn实例
        vpnlist = re.findall(r'vRoute_Probe\S*',result[i])
        # 设备名
        decvicename = net_connect.send_command('dis cu | include sysname')
        decvicename = (decvicename.split(" "))[1]

        # 写入文件
        excellist = xlrd.open_workbook(filepath)
        # 获取工作簿中的所有表格
        sheets = excellist.sheet_names()
        # 获取工作簿中所有表格中的的第一个表格
        first_sheet = excellist.sheet_by_name(sheets[0])
        # 获取表格中已存在的数据的行数
        rows_old = first_sheet.nrows
        # 将xlrd对象拷贝转化为xlwt对象
        new_excellist = copy(excellist)
        # 获取转化后工作簿中的第一个表格
        new_sheet = new_excellist.get_sheet(0)

        new_sheet.write(rows_old,0,decvicename)
        new_sheet.write(rows_old,1,iplist)
        new_sheet.write(rows_old,2,maclist)
        new_sheet.write(rows_old,3,interfacelist)
        new_sheet.write(rows_old,4,vpnlist)
        new_excellist.save(filepath)
    print("写入一台:",ip)

try:
    # 文件存放路径
    filepath = r'./result_index.xls'
    excel = xlwt.Workbook(encoding='utf-8')
    sheet = excel.add_sheet('sheet1', cell_overwrite_ok=True)
    sheet.write(0,0,'设备名称')
    sheet.write(0,1,'IP地址')
    sheet.write(0,2,'MAC地址')
    sheet.write(0,3,'接口')
    sheet.write(0,4,'vpn实例')
    excel.save(filepath)

    # 打开ip地址表文件
    with open('./ip.txt', 'r') as f:
        cmd_line = f.readlines()
    ips = []
    for c in cmd_line:
        ips.append(c)
    for ip in ips:
        getall(ip)
except:
    print('%s\tError\n'%(ip))
