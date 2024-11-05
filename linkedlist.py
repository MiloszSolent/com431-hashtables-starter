from node import Node

class TuplesLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    # TODO modify "add()" so that it takes a key and a value as parameters and 
    # creates a tuple using them. The Node should then be created using the
    # tuple.
    def add(self, key, value):
        n = Node((key, value))
        #n.value is now a tuple of key and value = n.value = ("cat", 32)
        # rather than just a single value as key and value are being passed through as a tuple

        if self.first is None:
            self.first = n
            self.last = n
        else:
            self.last.link(n)
            self.last = n

    def get(self, index):
        counter = 0

        currentNode = self.first
        while currentNode is not None:
            if counter == index:
                return currentNode
            else:
                currentNode = currentNode.next
                counter += 1
        return None
    
    # TODO modify "find()" so that it takes a KEY as a parameter  and searches 
    # the linked list until it finds a tuple with that key. It should then
    # return the value (i.e. the second member of the tuple)
    def find(self, key):
        currentNode = self.first

        while currentNode is not None:
            if currentNode.value[0] == key:
                return currentNode
            else:
                currentNode = currentNode.next
        return None

LinkedList = TuplesLinkedList()
#TuplesLinkedList.add(LinkedList, "cat", 32)
#TuplesLinkedList.add(LinkedList, "dog", 33)
#print(TuplesLinkedList.find(LinkedList, "cat"))