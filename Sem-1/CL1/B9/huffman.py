from itertools import groupby
from heapq import *
import socket
class Node:
	key=None
	freq=0
	left=None
	right=None
	def __init__(self,key,freq):
		self.key=key
		self.freq=freq
	
	def __cmp__(self,obj):
		return cmp(self.freq,obj.freq)
		
	def setchildren(self,l,r):
		self.left=l
		self.right=r
		
def huffman(ip):
	x=sorted(ip.split())
	itemqueue=[Node(a,len(list(b))) for a,b in groupby(x)]
	heapify(itemqueue)
	while(len(itemqueue)>1):
		l=heappop(itemqueue)
		r=heappop(itemqueue)
		n=Node(None,l.freq+r.freq)
		n.setchildren(l,r)
		heappush(itemqueue,n)
		
	codes={}
	
	def coding(s,node):
		if node.key:
			if not s:
				codes[node.key]="0"
			else:
				codes[node.key]=s
		else:
			coding(s+"0",node.left)
			coding(s+"1",node.right)
	
	coding("",itemqueue[0])
	print codes
ip=raw_input()
huffman(ip)
