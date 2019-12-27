from ctci.ds.linkedlist.linkedlist import LinkedList

def generateLinkedListFromList(inputList):
    linkedList = LinkedList()
    for item in inputList:
        linkedList.insertNode(item)
    return linkedList

def removeDupsFromUnsortedLinkedList(unsortedLinkedList):
    pass

def main():
    linkedList = generateLinkedListFromList([2,3,4])
    linkedList.printList()
