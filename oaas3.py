#!/usr/bin/python3

import sys
if len(sys.argv)!=4:
	print('Usage: as3.py input_folder output_folder output_file')
	# only_src
	# header ffdec
	exit(1)

import os

dest=sys.argv[2]

try:
	os.mkdir(dest)
except FileExistsError:
	pass

src=sys.argv[1]

a1='/'
a2a='/'
a2b='*'
a3='3'

b1b='*'
b2b='/'

for filename in os.listdir(src):
	with open(os.path.join(src,filename)) as sfile:
		with open(os.path.join(dest,os.path.splitext(filename)[0]+'.hx'),'wb') as dfile: #haxe will not do for .as
			mode=0
			for line in sfile:
				chars = bytearray(len(line))
				pos = 0
				for c in line:
					chars[pos]=ord(c)
					pos+=1
					if mode==0:
						if c==a1:
							mode=1
					elif mode==1:
						if c==a2a:
							mode=2
						elif c==a2b:
							mode=3
						else:
							mode=0
					elif mode==2 or mode==3:
						if c==a3:
							mode*=2
							pos=0
						else:
							mode=0
					elif mode==6:
						if c==b1b:
							mode=7
					elif mode==7:
						if c==b2b:
							mode=0
							pos-=2
						else:
							mode=6
				if mode==4:
					mode=0
				dfile.write(chars[:pos])

if os.environ.get('only_src'):
	exit(0)

def error():
	if r.returncode:
		print('error')
		exit(r.returncode)

import subprocess

c_dir=os.getcwd() #haxe says no to abs path
dest_file=os.path.realpath(sys.argv[3])
os.chdir(dest)
hd=os.environ.get('header')
if hd:
	r=subprocess.run(['haxe','--swf',dest_file,'--main','Main','--swf-header',hd])
else:
	r=subprocess.run(['haxe','--swf',dest_file,'--main','Main'])
# --swf-header 960:640:60:f68712 --swf-version 15
#w:h:fps:rgb
error()

#done for output_folder
os.chdir(c_dir) #back for clean
for filename in os.listdir(src):
	os.remove(os.path.join(dest,os.path.splitext(filename)[0]+'.hx'))
os.rmdir(dest)

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
