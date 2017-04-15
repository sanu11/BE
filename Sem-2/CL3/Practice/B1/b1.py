import unittest
import json

def isSafe(board,row,col):
	for i in range(row):
		if(board[i][col]==1):
			return False

		i = row - 1
		j = col - 1

	while i>=0 and j>=0:
		if(board[i][j]==1):
			return False
		i-=1
		j-=1

	i = row - 1
	j = col + 1

	while i>=0 and j<8:
		if(board[i][j]==1):
			return False
		i-=1
		j+=1

	return True
	
# function for every row, iteration for every column
def solve(board,row):
	if(row>7):
		return True
	else:
		i=0
		while i<8:
			if(isSafe(board,row,i)):
				board[row][i]=1

				if(solve(board,row+1)):
					return True

				board[row][i]=0
			i+=1

		return False


def run(filename):
	f = open(filename,'r')
	data = json.load(f) 
	start = data['start']
	print 'start : ',start
	if(start>7 or start < 0):
		return False
	board = [[0 for x in range (8)] for x in range (8)]
	board[0][start] = 1
	# print board
	res = solve(board,1)
	if(res):
		for i in range (8):
			for j in range(8):
				print board[i][j] , " ",
			print ""
	else:
		"Cannot be solved"
	return res

run('input1.json')

class Mytestcase(unittest.TestCase):
	def test_pos(self):
		print "Positive test \n"
		self.assertEqual(run('input1.json'),True)

	def test_neg(self):
		print "Negative test\n"
		self.assertEqual(run('input2.json'),False)

print "----------__Testing__------------\n"		
unittest.main()