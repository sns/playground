class Node:
    def __init__(self, data = None, nextNode = None):
        self.data = data
        self.nextNode = nextNode
    def __eq__(self, other):
        return self.getData() == other.getData()
    def getData(self):
        return self.data
    def setData(self, data):
        self.data = data
    def getNextNode(self):
        return self.nextNode
    def setNextNode(self, nextNode):
        self.nextNode = nextNode

class LinkedList:
    def __init__(self, head= None):
        self.head = head
    
    def insertNode(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            curr = self.head
            while curr.getNextNode() is not None:
                curr = curr.getNextNode()
            curr.setNextNode(node)
    
    def insertNodeAtTheBeginning(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.setNextNode(self.head)
            self.head = node
    
    def insertNodeAt(self, data, index):
        if abs(index) > self.size():
            raise ValueError("Invalid index")
        if index < 0:
            self.insertNodeAt(data, self.size() + index + 1)
        elif index == 0:
            self.insertNodeAtTheBeginning(data)
        else:
            node = Node(data)
            currIndex = 1
            curr = self.head
            while currIndex != index:
                if curr is not None:
                    curr = curr.getNextNode()
                    currIndex += 1
                else: 
                    raise ValueError("Invalid index")
            node.setNextNode(curr.getNextNode())
            curr.setNextNode(node)

    def deleteNode(self, data):
        prev = None
        curr = self.head
        while curr is not None:
            if curr.getData() == data:
                prev.setNextNode(curr.getNextNode())
                return
            prev = curr
            curr = curr.getNextNode()
        raise ValueError(data + " does not exist in the list")

    def deleteNodeFromTheBeginning(self):
        self.head = self.head.getNextNode()

    def deleteNodeFromTheEnd(self):
        if self.head is None:
            raise Exception("The linked list is empty.")
        prev = None
        curr = self.head
        while curr.getNextNode() is not None:
            prev = curr
            curr = curr.getNextNode()
        prev.setNextNode(None)

    def getLastNode(self):
        if self.head is None:
            raise Exception("The linked list is empty.")
        curr = self.head
        while curr.getNextNode() is not None:
            curr = curr.getNextNode()
        return curr

    def size(self):
        size = 0
        curr = self.head
        while curr is not None:
            size += 1
            curr = curr.getNextNode()
        return size
    
    def search(self, data):
        curr = self.head
        while curr is not None:
            if curr.getData() == data:
                return curr
            curr = curr.getNextNode()
        raise ValueError(data + " does not exist in the list")

    def printList(self):
        node = self.head
        while node is not None:
            print(node.getData())
            node = node.getNextNode()

    def __eq__(self, other):
        i = self.head
        j = other.head
        while i is not None and j is not None:
            if i != j:
                return False
            i = i.getNextNode()
            j = j.getNextNode()
        
        return i is None and j is None