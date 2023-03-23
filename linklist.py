class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

class Slinkedlist:
    def __init__(self):
        self.headval = None

    
#adding a node at the beginning of the list
    def AtBeginning(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode
#adding a node at the end of the list
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval = NewNode



#Print the linked List
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
            print()

    def iterate_item(self):
        current_item = self.headval
        while current_item:
            # print(current_item)
            val = current_item.dataval
            current_item = current_item.nextval
            yield val

# enter the head val
# if head is busy go to next
# repeat
# l = Slinkedlist()
# l.AtBeginning('Test')
# l.AtBeginning('Test2')
# l.AtEnd(('Test3'))
# l.listprint()