# Small application that converts mp4 to mp3
# Execute this application in the folder your have mp4 files
# Make sure filenames have no spaces in them
# Ramesh Vyas
import os
import subprocess
rootdir = os.getcwd()
count=0
print ("started converting mp4 to mp3...." + " in directory : " + rootdir)
for subdir, dirs, files in os.walk(rootdir):
  for filename in files:
    if filename.endswith(".mp4"):    
        try:    
            outfile=os.path.splitext(filename)[0] +".mp3"             
            sou=os.path.join(subdir, filename)      
            des=os.path.join(subdir, outfile)
            print (sou)
            subprocess.call(['ffmpeg ' + ' -i ' + sou + " " + des],shell=True)
            count=count+1            
        except:          
            continue      
    else:
        continue
print("total " + str(count) + " conversions finished, thank you for using this tool.")



