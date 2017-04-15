import unittest
class binarySearch:
	def __init__(self,arr,key):
		self.arr=arr
		self.key=key
		self.sort_elements()
		self.display_elements()

	def sort_elements(self):
		self.arr.sort()

	def display_elements(self):
		print "Sorted list : " , self.arr
		print "Key : " ,self.key

	def search_recur(self,left,right):
		mid = (left+right)/2
		arr = self.arr
		key = self.key
		
		if arr[mid]==key:
			return mid
		elif left == right:
			return len(arr)
		elif key<arr[mid]:
			return self.search_recur(left,mid-1)
		elif key>arr[mid]:
			return self.search_recur(mid+1,right)
		
	
	def search(self):
		arr = self.arr
		left =0
		right = len(arr)-1
		index = self.search_recur(left,right)
		if index >= len(arr):
			print "Element not found"
		else:
			print "Element found at " ,index

		return index

class Mytestcase(unittest.TestCase):

	def test_pos(self):
		print "\nPositive Testing\n"
		print "Entered list : [10, 12, 15, 9, 18]\n" 
		obj = binarySearch([10,12,15,9,18],15)
		self.assertEqual(obj.search(),3)
	
	def test_neg(self):
		print "\nNegative testing\n"
		print "Entered list : [10, 12, 15, 9, 18]\n"
		obj = binarySearch([10,12,15,9,18],11)
		self.assertEqual(obj.search(),5)

l = map(int,raw_input("Enter elements\n").split())
print "Entered list :" , l
key = input("Enter key to be searched\n")
obj = binarySearch(l,key)
obj.search()
print "\n-----------TESTING--------------\n"
unittest.main()








