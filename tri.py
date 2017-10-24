#!/usr/bin/python3
from random import randint
import argparse


class Some:
	"""docstring for Some"""
	def __init__(self, x,y):
		self.x = x
		self.y = y
		self.matrix = [[randint(1,99) for i in range(self.y)] for a in range(self.x)]
			#for k in range(self.y):
				#self.matrix[i].append(randint(10,100))
	def gogo(self):
		ce = -1
		kiki = 0
		print("Matrix: \n")
		for line in self.matrix:
			print("\tList[",kiki,"]","  ",end=" ")
			ce += 1
			kiki += 1
			for go in range(len(line)):
				if go > ce:
					print("",end=" ")
				else:
					if line[go] in range(1,10):
						print("[ ",line[go],"]",end=" ")
					else:	
						print("[",line[go],"]",end=" ")		
			print()
		print("\n")


def Main():
	argo = argparse.ArgumentParser("Enter two numbers")
	argo.add_argument("-a",dest = "first",help = "Enter first number",type = int)
	argo.add_argument("-b",dest = "sec",help = "Enter first number",type = int)

	do = argo.parse_args()
	if (not do.first) | (not do.sec):
		print("Put all arguments pls")
	else:	
		soso = Some(do.first,do.sec)
		soso.gogo()

if __name__ == "__main__":
	Main()	
