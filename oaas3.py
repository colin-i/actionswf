#!/usr/bin/python3

import sys
if len(sys.argv)!=3:
	print('Usage: as3.py output_folder output_file')
	# only_src   a1 a2a a2b a3 b1b b2b   splits_folder rule_ext splits_format_ext splits_printf_ext
	# header ffdec
	exit(1)

import os

def changeable(a,b,c): globals()[a + b] = c if os.environ.get(a + b) == None else os.environ.get(a + b)
changeable('a','1','/')
changeable('a','2a','/')
changeable('a','2b','*')
changeable('a','3','3')
changeable('b','1b','*')
changeable('b','2b','/')

def premade_formats():
	#environ or defaults at edor

	splits_folder=os.environ.get('splits_folder')
	if splits_folder==None:
		splits_folder='osrc'

	rule_ext=os.environ.get('rule_ext')
	if rule_ext==None:
		rule_ext='oac'

	splits_format_ext=os.environ.get('splits_format_ext')
	if splits_format_ext==None:
		splits_format_ext='split'

	#and here at src
	splits_printf_ext=os.environ.get('splits_printf_ext')
	if splits_printf_ext==None:
		splits_printf_ext='format'

	def ext(a): return '' if a=='' else os.extsep+a     #notice: os.extsep is not direct connected with my edor and src, is like a guardian?
	a=('' if splits_folder=='' else splits_folder+os.sep)

	#'a.q.swf' is a.q
	return (a+os.path.splitext(out_file_name)[0]+ext(rule_ext)+ext(splits_format_ext),a+out_file_name+ext(splits_printf_ext))

out_file_name=sys.argv[2]

splits_file, splits_mix = premade_formats()

dest=sys.argv[1]

try:
	os.mkdir(dest)
except FileExistsError:
	pass

def hx_ext(fl): return os.path.join(dest,os.path.splitext(fl)[0]+'.hx')

#for filename in os.listdir(src):
with open(splits_file,'rb') as splits_file:
	splits_file_data=splits_file.read()
	with open(splits_mix,'rb') as splits_mix:
		splits_mix_data=splits_mix.read()

		files = splits_file_data.decode('utf-8').split('\x00')
		files.pop() # Remove the last empty string
		for f in files:
			with open(f) as sfile:
				filename=os.path.basename(f)
				with open(hx_ext(filename),'wb') as dfile: #haxe will not do for .as
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
dest_file=os.path.realpath(out_file_name)
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
for f in files:
	filename=os.path.basename(f)
	os.remove(hx_ext(filename))
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
