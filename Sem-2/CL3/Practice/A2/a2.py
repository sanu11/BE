import threading
import xml.etree.ElementTree as X
import unittest

class quickSort:
	def __init__(self,arr):	
		self.arr = arr
		print "Entered list : ",arr
		self.qsort(0,len(arr)-1)
		
	def partition(self,low,high):
		arr= self.arr
		pivot = arr[high]
		i = low-1
		for j in range (low,high):
			if(arr[j]<=pivot):
				i=i+1
				arr[i],arr[j]=arr[j],arr[i]

		arr[high],arr[i+1]=arr[i+1],arr[high]
		return i+1

	def qsort(self,low,high):
		arr = self.arr
		if low >high:
			return
		pivot = self.partition(low,high)
		t1= threading.Thread(target=self.qsort,args=(low,pivot-1))
		t2= threading.Thread(target=self.qsort,args=(pivot+1,high))
		t1.start()
		t2.start()
		t1.join()
		print t1.getName()
		t2.join()
		print t2.getName()
		return arr

	def display(self):
		print self.arr


class MytestCase(unittest.TestCase):
	def test_pos(self):
		obj=quickSort([5,7,2,1])
		self.assertEqual(obj.qsort(0,3),[1,2,5,7])

data= X.parse('input.xml').getroot()

data= map(int,data.text.split())
obj = quickSort(data)
obj.display()

print "--------------___TESTING____------------------"
unittest.main()