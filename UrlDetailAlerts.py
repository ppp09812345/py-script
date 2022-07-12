#!/usr/bin/python3
import socket
import sys
import subprocess
import time
import os

number = 0

while number <= 3:
    file_name = sys.argv[1]
    file_path = '/tmp/url_msg/' + file_name

    with open(file_path, 'r') as f:
        url_msg = f.read()

    url_code = str(url_msg.split('_')[3]).replace('\n', '').replace('\r', '').replace('\t', '')
    url_site = url_msg.split('_')[0]
    #url_site = url_site.split('_')[1]

    try:
        url_ip = str(socket.getaddrinfo(url_site, None)[0][4][0])
    except:
        url_ip = '无法获取ip'

    if url_code == '403':
        number += 1
        time.sleep(1)
        # 获取一下url状态
        sub_pp = subprocess.Popen('/bin/bash /etc/sop/conf.d/url_script/%s.sh' % file_name,
                                  shell=True,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE, )
        rel = sub_pp.wait(timeout=11)  # 等待子进程结束
        if number == 3:
            msg = '龙田外网拨测 异常网站：%s 参考：服务器可能拒绝了请求 状态码：%s 域名ip地址：%s' % (url_site, url_code, url_ip)
            # print(msg.replace('\n', '').replace('\r', ''))
            if not os.path.isfile('/usr/bin/touch /tmp/url_detail/%s' % url_site):
                sub_file = subprocess.Popen('/usr/bin/touch /tmp/url_detail/%s' % url_site,
                                            shell=True,
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE, )

            with open('/tmp/url_detail/%s' % url_site, 'w') as f:
                f.write(msg)

    elif url_code == '404':
        number += 1
        time.sleep(1)
        # 获取一下url状态
        sub_pp = subprocess.Popen('/bin/bash /etc/sop/conf.d/url_script/%s.sh' % file_name,
                                  shell=True,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE, )
        rel = sub_pp.wait(timeout=11)  # 等待子进程结束
        if number == 3:
            msg = '龙田外网拨测 异常网站：%s 参考：可能找不到要查询的页面 状态码：%s, 域名ip地址：%s' % (url_site, url_code, url_ip)
            # print(msg.replace('\n', '').replace('\r', ''))
            if not os.path.isfile('/usr/bin/touch /tmp/url_detail/%s' % url_site):
                sub_file = subprocess.Popen('/usr/bin/touch /tmp/url_detail/%s' % url_site,
                                            shell=True,
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE, )

            with open('/tmp/url_detail/%s' % url_site, 'w') as f:
                f.write(msg)

    elif url_code == '503':
        number += 1
        time.sleep(1)
        # 获取一下url状态
        sub_pp = subprocess.Popen('/bin/bash /etc/sop/conf.d/url_script/%s.sh' % file_name,
                                  shell=True,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE, )
        rel = sub_pp.wait(timeout=11)  # 等待子进程结束
        if number == 3:
            msg = '龙田外网拨测 异常网站：%s 参考：服务器可能过载或则服务器无法处理请求 状态码：%s, 域名ip地址：%s' % (url_site, url_code, url_ip)
            # print(msg.replace('\n', '').replace('\r', ''))
            if not os.path.isfile('/usr/bin/touch /tmp/url_detail/%s' % url_site):
                sub_file = subprocess.Popen('/usr/bin/touch /tmp/url_detail/%s' % url_site,
                                            shell=True,
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE, )

            with open('/tmp/url_detail/%s' % url_site, 'w') as f:
                f.write(msg)

    elif url_code == '502':
        number += 1
        time.sleep(1)
        # 获取一下url状态
        sub_pp = subprocess.Popen('/bin/bash /etc/sop/conf.d/url_script/%s.sh' % file_name,
                                  shell=True,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE, )
        rel = sub_pp.wait(timeout=11)  # 等待子进程结束
        if number == 3:
            msg = '龙田外网拨测 异常网站：%s 参考：用户访问请求的响应超时造成的 状态码：%s, 域名ip地址：%s' % (url_site, url_code, url_ip)
            # print(msg.replace('\n', '').replace('\r', ''))
            if not os.path.isfile('/usr/bin/touch /tmp/url_detail/%s' % url_site):
                sub_file = subprocess.Popen('/usr/bin/touch /tmp/url_detail/%s' % url_site,
                                            shell=True,
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE, )

            with open('/tmp/url_detail/%s' % url_site, 'w') as f:
                f.write(msg)

    elif url_code == 'null':
        number += 1
        time.sleep(1)
        # 获取一下url状态
        sub_pp = subprocess.Popen('/bin/bash /etc/sop/conf.d/url_script/%s.sh' % file_name,
                                  shell=True,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE, )
        rel = sub_pp.wait(timeout=11)  # 等待子进程结束
        if number == 3:
            msg = '龙田外网拨测 异常网站：%s 参考：timeout 10 无法访问此网站 状态码：%s, 域名ip地址：%s' % (url_site, url_code, url_ip)
            # print(msg.replace('\n', '').replace('\r', ''))
            if not os.path.isfile('/usr/bin/touch /tmp/url_detail/%s' % url_site):
                sub_file = subprocess.Popen('/usr/bin/touch /tmp/url_detail/%s' % url_site,
                                            shell=True,
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE, )

            with open('/tmp/url_detail/%s' % url_site, 'w') as f:
                f.write(msg)

    elif url_code == '200':
        msg = '龙田外网拨测 状态：%s， 网站正常运行中......' % url_code
        # print(msg.replace('\n', '').replace('\r', ''))
        if not os.path.isfile('/usr/bin/touch /tmp/url_detail/%s' % url_site):
            sub_file = subprocess.Popen('/usr/bin/touch /tmp/url_detail/%s' % url_site,
                                        shell=True,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE, )

        with open('/tmp/url_detail/%s' % url_site, 'w') as f:
            f.write(msg)
        break

    else:
        number += 1
        time.sleep(1)
        # 获取一下url状态
        sub_pp = subprocess.Popen('/bin/bash /etc/sop/conf.d/url_script/%s.sh' % file_name,
                                  shell=True,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE, )
        rel = sub_pp.wait(timeout=11)  # 等待子进程结束
        if number == 3:
            msg = '龙田外网拨测 异常网站：%s 状态码：%s, 域名ip地址：%s' % (url_site, url_code, url_ip)
            # print(msg.replace('\n', '').replace('\r', ''))
            if not os.path.isfile('/usr/bin/touch /tmp/url_detail/%s' % url_site):
                sub_file = subprocess.Popen('/usr/bin/touch /tmp/url_detail/%s' % url_site,
                                            shell=True,
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE, )

            with open('/tmp/url_detail/%s' % url_site, 'w') as f:
                f.write(msg)
