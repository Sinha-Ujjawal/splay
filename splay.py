class _splay_node:
	def __init__(self, k, data):
		self._k = k
		self._data = data
		self._left = self._right = None
		self._height = 0
		self._nod_cnt = 1
		
	def __del__(self):
		del self._k, self._data, self._left, self._right, self._height, self._nod_cnt

class splay:
	def __init__(self):
		'''initialize a empty splay tree object
		'''
		self._root = None
		
	def __repr__(self):
		A = []
		for i in self:
			A.append(i)
		return 'splay({})'.format(A)
		
	def __iter__(self):
		return self.inorder()
		
	@property
	def key_set(self):
		A = []
		for i in self:
			A.append(i[0])
		return A
		
	@property
	def key_value_set(self):
		A = []
		for i in self:
			A.append(i)
		return A
		
	def __getitem__(self, k):
		return self.getData(k)
		
	def __setitem__(self, k, data):
		self.insert(k, data)
		
	def __delitem__(self, k):
		self.delete(k)
	
	def __len__(self):
		return self.getKeyCount()
	
	def __del__(self):
		self.delAll()
		del self._root
		
	def isEmpty(self):
		'''checks if the tree is empty or not
		'''
		return self._root == None
		
	def getKeyCount(self):
		'''returns the no of keys in the tree
		'''
		return self.__getNodeCount(self._root)
		
	def height(self):
		'''returns the height of the tree
		'''
		return self.__getHeight(self._root)
	
	def __getHeight(self, x):
		if x:
			return x._height
		return -1
		
	def __getNodeCount(self, x):
		if x:
			return x._nod_cnt
		return 0
		
	def __updateAug(self, x):
		x._height = 1 + max(self.__getHeight(x._left), self.__getHeight(x._right))
		x._nod_cnt = 1 + self.__getNodeCount(x._left) + self.__getNodeCount(x._right)
		
	def __leftRotate(self, x):
		y = x._right
		z = y._left

		x._right = z
		y._left = x
		
		self.__updateAug(x)
		self.__updateAug(y)
		
		return y
				
	def __rightRotate(self, x):
		y = x._left
		z = y._right
		
		x._left = z
		y._right = x
		
		self.__updateAug(x)
		self.__updateAug(y)
		
		return y
		
	def __splay(self, root, k, t = None):
		self.__updateAug(root)
		if root == self._root:
			if root._left and k == root._left._k:
				return self.__rightRotate(root), t
			elif root._right and k == root._right._k:
				return self.__leftRotate(root), t
						
		if root._left:
			if root._left._right and k == root._left._right._k:
				root._left = self.__leftRotate(root._left)
				return self.__rightRotate(root), t
			elif root._left._left and k == root._left._left._k:
				return self.__rightRotate(self.__rightRotate(root)), t
		
		if root._right:
			if root._right._left and k == root._right._left._k:
				root._right = self.__rightRotate(root._right)
				return self.__leftRotate(root), t
			elif root._right._right and k == root._right._right._k:
				return self.__leftRotate(self.__leftRotate(root)), t

		return root, t
		
	def __minUtil(self, root):
		if root._left != None:
			root._left, t = self.__minUtil(root._left)
			return self.__splay(root, t[0], t)
		return root, (root._k, root._data)
		
	def min(self):
		'''returns the min_key, data as tuple, if no such key then returns None
		'''
		if not self.isEmpty():
			self._root, minn = self.__minUtil(self._root)
			return minn
		
	def __maxUtil(self, root):
		if root._right != None:
			root._right, t = self.__maxUtil(root._right)
			return self.__splay(root, t[0], t)
		return root, (root._k, root._data)
			
	def max(self):
		'''returns the max_key, data as tuple, if no such key then returns None
		'''
		if not self.isEmpty():
			self._root, maxx = self.__maxUtil(self._root)
			return maxx
		
	def __extractMinUtil(self, root, parent):
		if root._left != None:
			root._left, p, minn = self.__extractMinUtil(root._left, root)
			return self.__splay(root, p._k, p) + (minn,)
		else:
			minn = root._k, root._data
			t = root._right
			del root
			return t, parent, minn
	
	def extractMin(self):
		'''returns the min_key, data as tuple, also remove it from the tree, if no such key then returns None
		'''
		if not self.isEmpty():
			self._root, p, minn = self.__extractMinUtil(self._root, None)
			return minn
	
	def __extractMaxUtil(self, root, parent):
		if root._right != None:
			root._right, p, maxx = self.__extractMaxUtil(root._right, root)
			return self.__splay(root, p._k, p) + (maxx,) 
		else:
			maxx = root._k, root._data
			t = root._left
			del root
			return t, parent, maxx
			
	def extractMax(self):
		'''returns the max_key, data as tuple, also remove it from the tree, if no such key then returns None
		'''
		if not self.isEmpty():
			self._root, p, maxx = self.__extractMaxUtil(self._root, None)
			return maxx
	
	def __insertUtil(self, k, data, root):
		if root == None:
			return _splay_node(k, data)
		
		if k < root._k:
			root._left = self.__insertUtil(k, data, root._left)
		elif k > root._k:
			root._right = self.__insertUtil(k, data, root._right)
		else:
			root._data = data
			
		return self.__splay(root, k)[0]
		
	def insert(self, k, data = None):
		'''insert k, data in the tree
		'''
		if isinstance(k, (int, float)):
			self._root = self.__insertUtil(k, data, self._root)
		else:
			raise TypeError('key can only be integers or floating point number')
		
	def __deleteUtil(self, k, root, parent):
		if root == None:
			return None, None, None
		tmp = p = None
		if k < root._k:
			root._left, p, tmp = self.__deleteUtil(k, root._left, root)
		elif k > root._k:
			root._right, p, tmp = self.__deleteUtil(k, root._right, root)
		else:
			tmp = root._k, root._data
			if root._left == None:
				t = root._right
				del root
				return t, parent, tmp
			elif root._right == None:
				t = root._left
				del root
				return t, parent, tmp
			else:
				root._left, p, t = self.__extractMaxUtil(root._left, root)
				root._k, root._data = t[0], t[1]
				return root, parent, tmp
		
		if p != None:
			return self.__splay(root, p._k, p) + (tmp,)
		return root, p, tmp
		
	def delete(self, k):
		'''deletes key k from the tree, also returns data of that key, if no such key then raises a KeyError exception
		'''
		if isinstance(k, (int, float)):
			self._root, p, t = self.__deleteUtil(k, self._root, None)
			if t:
				return t[1]
			else:
				raise KeyError('key {} does\'nt exist in the tree'.format(k))
		else:
			raise TypeError('key can only be integers or floating point number')
			
	def __getDataUtil(self, k, root):
		if root == None:
			return None, None
		t = None
		if k < root._k:
			root._left, t = self.__getDataUtil(k, root._left)
		elif k > root._k:
			root._right, t = self.__getDataUtil(k, root._right)
		else:
			return root, (root._k, root._data)
		if t != None:
			return self.__splay(root, k, t)
		return root, t
		
	def getData(self, k):
		'''returns data associated with the key k in the tree, if no such key then raises a KeyError exception
		'''
		if isinstance(k, (int, float)):
			self._root, t = self.__getDataUtil(k, self._root)
			if t:
				return t[1]
			else:
				raise KeyError('key {} does\'nt exist in the tree'.format(k))
		else:
			raise TypeError('key can only be integers or floating point number')
			
	def member(self, k):
		'''checks if key k is in the tree or not
		'''
		try:
			self.getData(k)
			return True
		except KeyError:
			return False
			
	def __getFarthestKey(self, root):
		if root:
			lh = self.__getHeight(root._left)
			rh = self.__getHeight(root._right)
			if lh == -1 and rh == -1:
				return root, (root._k, root._data)
			elif lh > rh:
				root._left, t = self.__getFarthestKey(root._left)
			else:
				root._right, t = self.__getFarthestKey(root._right)
			return self.__splay(root, t[0], t)
			
	def getFarthestKey(self):
		'''returns the farthest key from the root and its associated data, if the tree is empty returns None
		'''
		if not self.isEmpty():
			self._root, xnode = self.__getFarthestKey(self._root)
			return xnode
			
	def getRootKey(self):
		'''returns the root key and its associated data, if tree is empty returns None
		'''
		if not self.isEmpty():
			return self._root._k, self._root._data
			
	def __selectUtil(self, root, rank):
		if root:
			t = self.__getNodeCount(root._left) + 1
			if rank == t:
				return root._k, root._data
			elif rank < t:
				return self.__selectUtil(root._left, rank)
			else:
				return self.__selectUtil(root._right, rank - t)
		
	def select(self, rank):
		'''selects a key having the specified rank and returns it and its associated data, it no such key then returns None
		'''
		if isinstance(rank, int):
			if not self.isEmpty():
				return self.__selectUtil(self._root, rank)
		else:
			raise TypeError('rank can only be integers')
			
	def __rankUtil(self, root, k, rank):
		if root:
			t = self.__getNodeCount(root._left) + 1
			if k == root._k:
				return rank + t
			elif k < root._k:
				return self.__rankUtil(root._left, k, rank)
			else:
				return self.__rankUtil(root._right, k, rank + t)
	
	def rank(self, k):
		'''returns the rank of the key k, if no such key then returns None
		'''
		if isinstance(k, (int, float)):
			if not self.isEmpty():
				return self.__rankUtil(self._root, k, 0)
		else:
			raise TypeError('key can only be integers or floating point number')
		
	def __preorderUtil(self, root):
		if root != None:
			yield root._k, root._data
			yield from self.__preorderUtil(root._left)
			yield from self.__preorderUtil(root._right)
				
	def preorder(self):
		'''returns a generator the yields postorder traversal of tree
		'''
		return self.__preorderUtil(self._root)
		
	def __inorderUtil(self, root):
		if root != None:
			yield from self.__inorderUtil(root._left)
			yield root._k, root._data
			yield from self.__inorderUtil(root._right)
	
	def inorder(self):
		'''returns a generator the yields inorder traversal of tree
		'''
		return self.__inorderUtil(self._root)
	
	def __postorderUtil(self, root):
		if root != None:
			yield from self.__postorderUtil(root._left)
			yield from self.__postorderUtil(root._right)
			yield root._k, root._data
			
	def postorder(self):
		'''returns a generator the yields postorder traversal of tree
		'''
		return self.__postorderUtil(self._root)
	
	def getAll(self, desc = False):
		'''returns a generator the yields inorder traversal (either desc or asc) of tree
		'''
		if desc:
			return reversed(self)
		return self
		
	def printAll(self, order = 'inorder'):
		'''print the content of tree on console
		'''
		if order.lower() == 'inorder':
			order = self.inorder
		elif order.lower() == 'preorder':
			order = self.preorder
		elif order.lower() == 'postorder':
			order = self.postorder
		else:
			raise Exception('Order not recognized, should be either inorder, preorder or postorder')
		for i in order():
				print(i)
	
	def __delAllUtil(self, root):
		if root != None:
			root._left = self.__delAllUtil(root._left)
			root._right = self.__delAllUtil(root._right)
			if root._right == None and root._left == None:
				del root
				return None
	
	def delAll(self):
		'''empties the tree
		'''
		if not self.isEmpty():
			self._root = self.__delAllUtil(self._root)
				
	def __successorUtil(self, k, root):
		if root == None:
			return None, None
		t = None
		if k < root._k:
			root._left, t = self.__successorUtil(k, root._left)
		elif k > root._k:
			root._right, t = self.__successorUtil(k, root._right)
		else:
			if root._right != None:
				root._right, minn = self.__minUtil(root._right)
				t = minn
		if t == None and root._k > k:
			t = root._k, root._data
		if t:
			return self.__splay(root, t[0], t)
		return root, t
						
	def successor(self, k):
		'''returns k1, data as tuple where k1 is the successor k, if no such key then returns None
		'''
		if isinstance(k, (int, float)):
			if not self.isEmpty():
				self._root, succ = self.__successorUtil(k, self._root)
				return succ
		else:
			raise TypeError('key can only be integers or floating point number')
			
	def __predecessorUtil(self, k, root):
		if root == None:
			return None, None
		t = None
		if k < root._k:
			root._left, t = self.__predecessorUtil(k, root._left)
		elif k > root._k:
			root._right, t = self.__predecessorUtil(k, root._right)
		else:
			if root._left != None:
				root._left, maxx = self.__maxUtil(root._left)
				t = maxx
		if t == None and root._k < k:
			t = root._k, root._data
		if t != None:
			return self.__splay(root, t[0], t)
		return root, t
			
	def predecessor(self, k):
		'''returns k1, data as tuple where k1 is the predecessor k, if no such key then returns None
		'''
		if isinstance(k, (int, float)):
			if not self.isEmpty():
				self._root, pred = self.__predecessorUtil(k, self._root)
				return pred
		else:
			raise TypeError('key can only be integers or floating point number')
