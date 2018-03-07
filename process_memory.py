#this script to calculate all the occupied memory size and process
#PS aux lists all the processes, to filter out the RSS of the column, and then sum
#!/usr/bin/python2

import os

list = []
m = 1024
sum = 0

str1 = os.popen('ps aux','r').readlines()

for i in str1:

    str2 = i.split()
    new_rss = str2[5]
    list.append(new_rss)

for i in list[1:-1]:

    num = int(i)
    sum = sum + num
print '%s:%sM' %(list[0],sum/m) 
    

