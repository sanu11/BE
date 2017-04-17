import random
import threading
from pymongo import MongoClient
import time

class Philosophers(threading.Thread):
	client = MongoClient("127.0.0.1",27017)

	@staticmethod
	def readfrommongo(i):
		limit = 0
		db = Philosophers.client.test.dini
		cursor = db.find({"ph_no":i})[limit:limit+1]
		print cursor[0] 


	def __init__(self,index,name,leftFork,rightFork):
		threading.Thread.__init__(self)
		self.index = index
		self.name = name
		self.leftFork=leftFork
		self.rightFork=rightFork

	def run(self):
		time.sleep(random.uniform(3,13))
		print "Philosopher ",self.name , " is hungry"
		
		self.dine()

	def dine(self):
		fork1 ,fork2 = self.leftFork,self.rightFork
		while True:
			fork1.acquire(True)
			unlocked = fork2.acquire(False)
			if unlocked:
				break
			fork1.release()

		self.dining()	
		fork1.release()
		fork2.release()

	def dining(self):
		print "\n\nPhilosopher " , self.name , " starts eating "
		Philosophers.readfrommongo(self.index)
		time.sleep(5)
		print "\nPhilosopher ",self.name , " finishes eating and releases fork"

def diningPhilosophers():
	fork = [threading.Lock() for n in range(5)]
	names = ["a","b","c","d","e"]
	philosophers = [(Philosophers(i,names[i],fork[i%5],fork[(i+1)%5])) for i in range(5)]
	for p in philosophers:
		p.start()

diningPhilosophers()