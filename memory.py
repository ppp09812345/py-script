#!/usr/bin/python

#请按照这样的日期格式（xxxx-xx-xx）每日生成一个文件，例如今天生成的文件为2018-03-05.log， 并且把磁盘的使用情况写到到这个文件中。

import time

import os

new_time = time.strftime('%Y-%m-%d')


disk_status = os.popen('df -h').readlines()


str1 = ''.join(disk_status)


f = file(new_time+'.log','w')


f.write('%s' % str1)

f.flush()

f.close()
