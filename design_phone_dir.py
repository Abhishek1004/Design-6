from collections import deque

class phone_directory:
	def __init__(self, maxnumbers):#time - O(n), n = maxnumbers
		self.hashset = set()
		self.q = deque()
		self.size = maxnumbers
		for i in range(self.size):
			self.q.append(i)

	def get(self): #time - O(1)
		if self.size>0:
			num = self.q.popleft()
			self.hashset.add(num)
			self.size-=1
			return num
		return -1
		

	def check(self, number): #time - O(1)
		return True if number not in self.hashset else False
		

	def release(number): #time - O(1)
		if number in self.hashset:
			self.hashset.remove(number)
			self.size+=1
			self.q.append(number)

#space complexity - O(n), the space of both hashset and queue