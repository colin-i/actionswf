#!/usr/bin/python3

import sys
if len(sys.argv)!=4:
	print('Usage: as3.py input_folder output_folder output_file')
	exit(1)

#will remove //3 and at left, /*3 and ending */
#also, need to make dirs tree to merge files

import os

src=sys.argv[1]
dest=sys.argv[2]
for filename in os.listdir(src):
	with open(os.path.join(src,filename)) as sfile:
		with open(os.path.join(dest,os.path.splitext(filename)[0]+'.hx'),'wb') as dfile: #haxe will not do for .as
			for line in sfile:
				#print(line,end='')
				dfile.write(line.encode())

def error():
	if r.returncode:
		print('error')
		exit(r.returncode)

import subprocess

c_dir=os.getcwd() #haxe says no to abs path
dest_file=os.path.realpath(sys.argv[3])
os.chdir(dest)
r=subprocess.run(['haxe','--swf',dest_file,'--main','Main'])
# --swf-header 960:640:60:f68712 --swf-version 15
#w:h:fps:rgb
error()

#done for output_folder
os.chdir(c_dir) #back for clean
for filename in os.listdir(src):
	os.remove(os.path.join(dest,os.path.splitext(filename)[0]+'.hx'))

#confirm is as3

dest_file_tmp=dest_file+'.tmp'
ffdec=os.environ.get('ffdec')
if ffdec==None:
	ffdec='ffdec'
r=subprocess.run([ffdec,'-decompress',dest_file,dest_file_tmp])
error()
with open(dest_file_tmp,'rb') as file:
	file.seek(8)
	#rect
	b=file.read(1)
	n=b[0]>>3 # 0xff >> 1 is 0x7f
	n=5+(n*4)
	if n%8:
		n=int(n/8)+1
	else:
		n=n/8
	file.seek(n+3,1)
	#tag
	tag=file.read(2)
	tg=tag[1]<<2
	tg_low=tag[0]>>6
	tg|=tg_low
	if tg!=69:
		print('no FileAttributes tag')
		exit(1)
	tg=tag[0]&0x3f
	if tg==0x3f:
		print('malformed FileAttributes tag')
		exit(1)
	#tag data
	tg=file.read(1)
	if (tg[0]&8)==0:
		print('ActionScript3 bit is not set')
		exit(1)

os.remove(dest_file_tmp)
