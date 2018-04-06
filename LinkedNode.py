#单循环链表的python实现



class Node:
	def __init__(self,initdata):
		self.__data = initdata
		self.__next = None

# 调用print时候可以打印该节点的值
	def __repr__(self):
		return str(self.data)

	def getData(self):
		return self.__data

	def getNext(self):
		return self.__next

	def setData(self, new):
		self.__data = new

	def setNext(self, newnext):
		self.__next = newnext


class Linkedlist:
	def __init__(self):
		self.head = Node(None)
		self.head.setNext(self.head)

	def add(self, item):
		tmp = Node(item)
		tmp.setNext(self.head.getNext())
		self.head.setNext(tmp)

	def remove(self, item):
		prev = self.head
		# prev不是循环链表尾部
		while prev.getNext() != self.head:
			cur = prev.getNext()
			if cur.getData() == item:
				# item的前一个节点指向item的后一个节点
				prev.setNext(cur.getNext())
			prev = prev.getNext()

	def search(self, item):
		cur = self.head.getNext()
		while cur != self.head:
			if cur.getData() == item:
				return True
			cur = cur.getNext()
		return False

	def empty(self):
		return self.head.getNext() == self.head

	def size(self):
		count = 0
		cur = self.head.getNext()
		while cur != self.head:
			count += 1
			cur = cur.getNext()
		return count

if __name__ == '__main__':
	s = Linkedlist()
	s.add(19)
	s.add(51)
	s.add(120)
	print(s.size())
	s.remove(51)
	print(s.size())