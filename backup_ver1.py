#!/usr/bin/python
#Filename:backup_ver1.py
#无法运行，可以参考tarfile包

import os
import time

#1,The files and directories to be backed up are specified in a list
print 'please enter the source path'
source = raw_input()
#2,The backup must be stored in a main backup directory
print 'please enter the target path'
target_dir = raw_input()
#3,The files are backed up into a zip file.
#4,The name of zip archive is the current date and time

target = target_dir+'/'+time.strftime('%Y%m%d%H%M%S')+'.tar'

#5,We use the zip command to put the files in a zip archive

zip_command = 'tar-zcvf %s %s'%(target,source)

#run the backup
print source
print target
if os.system(zip_command) == 0:
	print 'Successful backup to',target
else:
	print 'backup failed'
