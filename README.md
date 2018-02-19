## splay tree
>A splay tree is a self-adjusting binary search tree with the additional property that recently accessed elements are quick to access again. It performs basic operations such as insertion, look-up and removal in O(log n) amortized time. For many sequences of non-random operations, splay trees perform better than other search trees, even when the specific pattern of the sequence is unknown. The splay tree was invented by Daniel Sleator and Robert Tarjan in 1985. For more information visit https://en.wikipedia.org/wiki/Splay_tree.

##### How to use:

  *description*: **`splay()`**
  
  *Space-Complexity*: **`O(n)`** *where **n** is the no of keys in the tree*
  
  ```python
  import splay
  
  ob = splay.splay() 
  # Now u cud add keys and values/data to the tree
  ```
  
##### insert:

  *description*: **`insert(k, data = None)`** *it **inserts k, data (by default None)** to the tree*
  
  *Time-Complexity*: **`amortized O(lg n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  ob.insert(1001, 'apple') # or ob[1001] = 'apple'
  ob.insert(1002, 'banana')
  ob.insert(1003) # or ob[1003] = None
  ob.insert(1004, 'orange')
  ob.insert(2001, 'pen')
  ob.insert(2002, 'pencil')
  ```

##### delete:

  *description*: **`delete(k)`** *it **deletes k** from the tree, also returns **data** of that key, if no such key then raises a **KeyError** exception*
  
  *Time-Complexity*: **`amortized O(lg n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  ob.delete(1001) # will delete and return (1001, 'apple') from the tree
  # or del ob[1001], but this will not return anything
  ```

##### getData:

  *description*: **`getData(k)`** *it returns **data** of key k, if no such key then raises a **KeyError** exception*
  
  *Time-Complexity*: **`amortized O(lg n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  print(ob.getData(1001)) # or print(ob[1001])
  # will print (1001, 'apple') on the console
  ```
  
##### member:

  *description*: **`member(k)`** *it returns **True** if the key **k** is present in the tree*
  
  *Time-Complexity*: **`amortized O(lg n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  print(ob.member(1001))
  # will print True on the console
  ```
  
##### select:

  *description*: **`select(rank)`** *it returns **(k, data) having rank (i.e; the inorder (sorted in asc order) position of the key) as specified** as **tuple***
  
  *Time-Complexity*: **`amortized O(lg n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  print(ob.select(1))
  # will print (1001, 'apple') on the console
  ```
 
##### rank:

  *description*: **`rank(k)`** *it returns **rank (i,e; the inorder position of the key)** of **k***
  
  *Time-Complexity*: **`amortized O(lg n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  print(ob.rank(1001))
  # will print 1 on the console
  ```
  
##### getRootKey:

  *description*: **`getRootKey()`** *it returns **root's (k, data)** as **tuple***
  
  *Time-Complexity*: **`O(1)`** 
  
  ```python
  print(ob.getRootKey())
  # will print (2002, 'pencil') on the console
  ```

##### getFarthestKey:

  *description*: **`getFarthestKey()`** *it returns **farthest (i.e; the key which is farthest from the root) (k, data)** as **tuple***
  
  *Time-Complexity*: **`amortized O(lg n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  print(ob.getFarthestKey())
  # will print (1001, 'apple') on the console
  ```
  
##### min:

  *description*: **`min()`** *it returns **min (k, data)** as **tuple***
  
  *Time-Complexity*: **`amortized O(lg n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  print(ob.min())
  # will print (1001, 'apple') on the console
  ```
 
##### extractMin:

  *description*: **`extractMin()`** *it returns **min (k, data)** as **tuple**, also it removes it from the tree*
  
  *Time-Complexity*: **`amortized O(lg n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  print(ob.extractMin())
  # will print (1001, 'apple') on the console
  ```
  
##### max:

  *description*: **`max()`** *it returns **max (k, data)** as **tuple***
  
  *Time-Complexity*: **`amortized O(lg n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  print(ob.max())
  # will print (2002, 'pencil') on the console
  ```
 
##### extractMax:

  *description*: **`extractMax()`** *it returns **max (k, data)** as **tuple**, also it removes it from the tree*
  
  *Time-Complexity*: **`amortized O(lg n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  print(ob.extractMax())
  # will print (2002, 'pencil') on the console
  ```
  
##### getKeyCount:

  *description*: **`getKeyCount()`** *it returns the no of keys in the tree*
  
  *Time-Complexity*: **`O(1)`**
  
  ```python
  print(ob.getKeyCount()) # or print(len(ob))
  # will print 6 on the console
  ```

##### isEmpty:

  *description*: **`isEmpty()`** *it returns **True** if the tree is empty, otherwise returns **False***
  
  *Time-Complexity*: **`O(1)`**
  
  ```python
  print(ob.isEmpty())
  # will print False on the console
  ```
  
##### height:

  *description*: **`height()`** *it returns the height of the tree*
  
  *Time-Complexity*: **`O(1)`**
  
  ```python
  print(ob.height())
  # will print 5 on the console
  ```
  
##### inorder:

  *description*: **`inorder()`** *it returns a **generator** that generate **inorder traversal** of the tree*
  
  *Time-Complexity*: **`O(n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  for i in ob.inorder():
      print(i)
  # will print
  # (1001, 'apple')
  # (1002, 'banana')
  # (1003, None)
  # (1004, 'orange')
  # (2001, 'pen')
  # (2002, 'pencil')
  ```
  
##### preorder:

  *description*: **`preorder()`** *it returns a **generator** that generate **preorder traversal** of the tree*
  
  *Time-Complexity*: **`O(n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  for i in ob.preorder():
      print(i)
  # will print
  # (2002, 'pencil')
  # (2001, 'pen')
  # (1004, 'orange')
  # (1003, None)
  # (1002, 'banana')
  # (1001, 'apple')
  ```
  
##### postorder:

  *description*: **`postorder()`** *it returns a **generator** that generate **postorder traversal** of the tree*
  
  *Time-Complexity*: **`O(n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  for i in ob.postorder():
      print(i)
  # will print
  # (1001, 'apple')
  # (1002, 'banana')
  # (1003, None)
  # (1004, 'orange')
  # (2001, 'pen')
  # (2002, 'pencil')
  ```
  
##### printAll:

  *description*: **`printAll(order = 'inorder')`** *it prints the content of the tree in the specified order, if order not recognized it raises a error*
  
  *Time-Complexity*: **`O(n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  ob.printAll('inorder')
  # will print
  # (1001, 'apple')
  # (1002, 'banana')
  # (1003, None)
  # (1004, 'orange')
  # (2001, 'pen')
  # (2002, 'pencil')
  ```

##### delAll:

  *description*: **`delAll()`** *it just deletes all the keys from the tree*
  
  *Time-Complexity*: **`O(n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  ob.delAll()
  # will empty the tree
  ```
  
##### successor:

  *description*: **`successor(k)`** *it **returns k1, data** as **tuple** where **k1** is the **successor** of **k***
  
  *Time-Complexity*: **`amortized O(lg n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  print(ob.successor(1000))
  # will print
  # (1001, 'apple')
  print(ob.successor(1001))
  # will print
  # (1002, 'banana')
  ```

##### predecessor:

  *description*: **`predecessor(k)`** *it **returns k1, data** as **tuple** where **k1** is the **predecessor** of **k***
  
  *Time-Complexity*: **`amortized O(lg n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  print(ob.predecessor(2000))
  # will print
  # (1004, 'orange')
  print(ob.predecessor(1003))
  # will print
  # (1002, 'banana')
  ```

##### __iter__:

  *description*: **`__iter__`** *splay object is **iterable***
  
  *Time-Complexity*: **`O(n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  for i in ob:
      print(i)
  # will print
  # (1001, 'apple')
  # (1002, 'banana')
  # (1003, None)
  # (1004, 'orange')
  # (2001, 'pen')
  # (2002, 'pencil')
  ```
  
##### __repr__:

  *description*: **`__repr__`**
  
  *Time-Complexity*: **`O(n)`** *where **n** is the no of keys in the tree* 
  
  ```python
  print(ob)
  # will print
  # splay([(1001, 'apple'), (1002, 'banana'), (1003, None), (1004, 'orange'), (2001, 'pen'), (2002, 'pencil')])
  ```
