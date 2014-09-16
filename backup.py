import tarfile
import os
import sys
 
user =  os.getenv('USERNAME')
 
filename = '/home/%s/tmp.tgz' % user
print 'The tar file was created here: %s' % filename
mode = 'w:gz'
 
file = tarfile.open( filename, mode )
 
file.add( '/var/log/auth.log' )
file.add( '/var/log/messages' )
 
file.close()
print 'done'
