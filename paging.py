#coding:utf-8

# level 1 (python 2.x):
#def more(text,numlines=15):
#	lines = text.splitlines()
#	while lines:
#		chunk = lines[:numlines]
#		lines = lines[numlines:]
#		for line in chunk:
        #			print line
#		if lines and raw_input("More?(y/n)") not in ('y','Y'):
#			break

############################################################
# level 2 (python 3.x):
import sys

def getReply():
        if sys.stdin.isatty():
                return input("?")
        if sys.platform[:3] == 'win':
                import msvcrt
                msvcrt.putch(b'?')
                key = msvcrt.getche()
                msvcrt.putch(b'\n')
                return key
        else:
                assert False, 'platform not supported'
                # linux: open('/dev/tty').readlines()[:-1]

def more(text, numlines=10):
        lines = text.splitlines()
        while lines:
                chuck = lines[:numlines]
                lines = lines[numlines:]
                for line in chuck:
                        print(line)
                if lines and getReply() not in (b'y', b'Y'):
                        break
			
if __name__ == "__main__":
        if len(sys.argv) == 1:
                more(sys.stdin.read())
        else:
                more(open(sys.argv[1]).read())
