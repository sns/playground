from ctci.ds.linkedlist.linkedlist import LinkedList

def generateLinkedListFromList(inputList: LinkedList):
    linkedList = LinkedList()
    for item in inputList:
        linkedList.insertNode(item)
    return linkedList

def removeDupsFromUnsortedLinkedListWithTreePointers(linkedList: LinkedList) -> LinkedList:
    if linkedList.size() < 2:
        return linkedList
    currSrcNode = linkedList.head
    while currSrcNode is not None:
        slowRunnerNode = currSrcNode
        runnerNode = currSrcNode.getNextNode()
        while runnerNode is not None:
            if runnerNode.getData() == currSrcNode.getData():
                slowRunnerNode.setNextNode(runnerNode.getNextNode())
            else:
                slowRunnerNode = runnerNode
            runnerNode = runnerNode.getNextNode()
        currSrcNode = currSrcNode.getNextNode()
    return linkedList

def removeDupsFromUnsortedLinkedListWithTwoPointers(linkedList: LinkedList) -> LinkedList:
    if linkedList.size() < 2:
        return linkedList
    currSrcNode = linkedList.head
    while currSrcNode is not None:
        runnerNode = currSrcNode
        while runnerNode is not None and runnerNode.getNextNode() is not None:
            if runnerNode.getNextNode().getData() == currSrcNode.getData():
                runnerNode.setNextNode(runnerNode.getNextNode().getNextNode())
            runnerNode = runnerNode.getNextNode()
        currSrcNode = currSrcNode.getNextNode()
    return linkedList

def removeDupsFromUnsortedLinkedListWithBuffer(linkedList: LinkedList) -> LinkedList:
    if linkedList.size() < 2:
        return linkedList
    mem = set()
    currNode = linkedList.head
    mem.add(currNode.getData())
    runnerNode = linkedList.head.getNextNode()
    while runnerNode is not None:
        if runnerNode.getData() in mem:
            currNode.setNextNode(runnerNode.getNextNode())
        else:
            mem.add(runnerNode.getData())
        runnerNode = runnerNode.getNextNode()
    return linkedList


def solve():
    linkedList = generateLinkedListFromList([1,1,2,3,3])
    # print("unsorted input list: \n")
    # linkedList.printList()
    # resWithoutBuffer = removeDupsFromUnsortedLinkedListWithTwoPointers(linkedList)
    # print("result list without duplicates: \n")
    # resWithoutBuffer.printList()
    resWithBuffer = removeDupsFromUnsortedLinkedListWithTwoPointers(linkedList)
    print("result list without duplicates using buffer (more efficient): \n")
    resWithBuffer.printList()
    # print("Both results are equal: %s" % (resWithoutBuffer == resWithBuffer))

