from math import log
f=open("data.txt","r")
data=[]

def process():
	for line in f:
		d={}		
		l=line.split()
		n=0
		for i in l:
			if i=="?":
				d[n]="-ve"
			else:	
				d[n]=i
			n+=1
		data.append(d)

def probability(data,attr):
	freq={}
	for x in data:
		value=x[attr]
		if value!="-ve":
			if value in freq.keys():
				freq[value]+=1
			else:
				freq[value]=1		
	for attribute,count in freq.items():
		freq[attribute]=count/len(data)

	return freq

def entropy(data,attr):
	sum=0
	p=probability(data,attr)
	for value,prob in p.items():
		sum+=prob*log(prob)
	return -1*sum
			
def gain(data,attr):
	V=[]
	Es=entropy(data,14)

	for x in data:
		value=x[attr]
		if value!="-ve":
			V.append(value)

	D=[]
	l=[]
	m=[]
	h=[]
	for x in data:
		if x[6]=="norm":
			l.append(x)
		elif x[6]=="hyp":
			m.append(x)
		else:
			h.append(x)
	D.append(l)
	D.append(h)
	D.append(m)
	sum=0
	for i in range(0,3):
		sum+=len(l[i])/len(data)*entropy(D[i],6)
	return Es-sum
		
	
process()
for i in range(0,14):
	print(entropy(data,i))
print("GAIN=",gain(data,6))

