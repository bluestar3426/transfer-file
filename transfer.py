import os
import glob

file=glob.glob('/media/usb1/farrow_202106/*.h264')

lis=[]
for i in file:
    lis.append(i.rstrip('h264'))

    
with open('/media/usb1/code/test.sh', 'w') as f:
    for i in lis:
        f.writelines('ffmpeg -i '+str(i)+'h264'+' '+str(i)+'mp4\n')
        f.writelines('sleep 5\n')
        f.writelines('rm '+str(i)+'h264\n')
f.close()
