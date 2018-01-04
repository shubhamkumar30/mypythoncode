#!/usr/bin/python
import commands
n=int(raw_input("Enter the number of IP to show:"))

#taking out IP of all system
result=(commands.getoutput('arp-scan -I wlp7s0 --localnet | grep -i 192.168 > /root/ip.txt; cat /root/ip.txt')).split('\t')


k=commands.getoutput('wc -l /root/ip.txt')
k=(k.split(' ')[0])
l=int(k)

#storing output a variable [list]

#checking condition for no of IP requested or we have
if n <= l:
	n=n*2+1
else:
	n=l*2+1

#define tuple
y=[]
y.append(result[0])

for i in range(2,n,2):
	a=result[i].split('\n')
	y.append(a[-1])
y.pop(-1)


print("No of IP active:")
print len(y)


#printing ip list
print(" IP' are:")
for i in y:
	print(" "+i)


