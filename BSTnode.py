from random import randint
class BSTnode(object):

	def __init__(self,parent,k,index,left=None,right=None):
		self.key = k
		self.parent = parent
		self.left = left
		self.right = right
		self.index = index
		self.mem = id(self)
	def insert(self,k,i):
		if k>self.key:
			if self.right == None:
				newNode = BSTnode(self,k,i)
				self.right = newNode
				return newNode
			else:
				return self.right.insert(k,i)
		if k<self.key:
			if self.left == None:
				newNode = BSTnode(self,k,i)
				self.left = newNode
				return newNode
			else:
				return self.left.insert(k,i)
	def findMin(self):
		if self.left==None:
			return self
		else:
			return self.left.findMin()
	def nextLarger(self):
		if self.right==None:
			node = self
			while node.parent!=None and node.parent.right==node:
				node = node.parent
			return node.parent

		if self.right != None:
			return self.right.findMin()
	def delete(self):
		if self.left is None and self.right is None:
			if self is self.parent.left:
				self.parent.left = None
			if self is self.parent.right:
				self.parent.right = None
		if self.left is None and self.right is not None:
			if self is self.parent.left:
				self.parent.left = self.right
				self.right.parent = self.parent
			if self is self.parent.right:
				self.parent.right = self.right
				self.right.parent = self.parent
		if self.left is not None and self.right is None:
			if self is self.parent.left:
				self.parent.left = self.left
				self.left.parent = self.parent
			if self is self.parent.right:
				self.parent.right = self.left
				self.left.parent = self.parent
		if self.left is not None and self.right is not None:
			nl = self.nextLarger()
			nl.key , self.key = self.key , nl.key
			nl.index , self.index = self.index , nl.index
			nl.delete()
	def search(self,k):
		if self.key==k:
			return self.index
		elif k>self.key and self.right is not None:
			return self.right.search(k)
		elif k<self.key and self.left is not None:
			return self.left.search(k)
		else:
			return "sorry"
	def height(self):
		if self.left is None and self.right is None:
			return 1
		if self.left is None and self.right is not None:
			return self.right.height()+1
		if self.left is not None and self.right is None:
			return self.left.height()+1
		if self.left is not None and self.right is not None:
			return max(self.left.height(),self.right.height()) + 1

class BST(object):
	def __init__(self,a = [33,54,87,23,76,34,797,23,2,523,6,2,76,24,798,3,3,87,23,79,12]):
		self.root = BSTnode(None,a[0],0)
		self.mems =[self.root.mem]
		self.nodes = [self.root]
		for i in range(1,len(a)):
			self.nodes.append( self.root.insert(a[i],i) )
			if self.nodes[i]!=None:
				self.mems.append(self.nodes[i].mem or None)			
			else:
				self.mems.append(None)
		print self.root.height()
		print self.mems
	
b = BST()