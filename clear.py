#coding:utf-8
import os,os.path

def clear_empty_dir(path):
	for root,dirs,files in os.walk(path,topdown=False):
		for name in dirs:
			try:
				os.rmdir(os.path.join(root,name))
				print os.path.join(root,name)+' has been deleted!'
			except OSError:
				pass
	print "+"*60
	print 'All empty directories under %s have been deleted!' % path
	
if __name__ == '__main__':
	path = raw_input('Which path you want to clear up? ')
	clear_empty_dir(path)