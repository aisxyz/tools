#coding:utf-8

unitR=[u'分',u'角']
unitL=[u'元',u'万',u'亿']
cn={'0':u'零','1':u'壹','2':u'贰','3':u'叁','4':u'肆','5':u'伍','6':u'陆','7':u'柒','8':u'捌','9':u'玖'}
bit=(u'',u'拾',u'佰',u'千')

def ntoc(sn):
	sn=str(float(sn))	#不宜采用百亿以上，因为sno太大时会被自动转换成指数形式
	#start=0
	#for c in sn:		#从左边第一个不为0的位置开始算
	#	if c!='0':
	#		break
	#	start+=1
	point=sn.rfind('.')
	snl,snr=('','')
	if point>=0:
		#snl=sn[start:point]
		snl=sn[:point]
		snr=sn[point+1:point+3]		#最多保留小数点后两位
	else:
		snl=sn
	result=readL(snl)
	if snr:
		result+=readR(snr)
	return result

def readL(snl):
	length=len(snl)
	groupN=length/4
	high=length%4
	groups=[]
	if snl[:high]:
		groups.append(snl[:high])
	while groupN:
		groups.append(snl[high:high+4])
		high=high+4
		groupN-=1
	r=''
	groupN=len(groups)-1
	for group in groups:
		r+=handleG(group)+unitL[groupN]
		groupN-=1
	return r
	
def handleG(group):
	r=u''
	zf=False
	bitN=len(group)
	index=0
	#temp=0
	for c in group:
		bitN-=1
		if not zf or c!='0':
			r+=cn[c]
		if c=='0':
			#temp=index		#记录非零数字前的0的位置
			zf=True
		else:
			r+=bit[bitN]
			zf=False
		index+=1
		if not float(group[index:]):	#剩余的部分为0就结束本组处理
			break
	return r

def readR(snr):
	r=''
	leng=len(snr)
	for c in snr:
		leng-=1
		if c=='0':
			continue
		r+=cn[c]+unitR[leng]
	return r

if __name__=="__main__":
	result=ntoc('1111')
	print result