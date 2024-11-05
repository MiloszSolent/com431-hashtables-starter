from linkedlist import TuplesLinkedList

class HashTable:
    def __init__(self, nbuckets):
        #list comprehension
        #Creates a list of "nbuckets" empty linked lists
        #each position (bucket) will contain an empty linked list
        self.internalList = [TuplesLinkedList() for i in range(nbuckets)]

    def calcHashCode(self, key):
        #Calculate the hash code of the key
        #The sum of the ascii codes of each character in the key
        #ord() - gets the ascii code of a character

        hashcode = 0

        for i in range(0, len(key)):
            hashcode += ord(key[i])

        hashcode %= len(self.internalList)

        return hashcode

    #add the key/value pair to the linked list in the appropriate bucket
    def put(self, key, value):
        hashcode = self.calcHashCode(key)

        TuplesLinkedList.add(self.internalList[hashcode], key, value)

    #retrieve the value associated with the given key
    def get(self, key):
        return self.internalList[self.calcHashCode(key)].find(key)

internalListObj = HashTable(4)
internalListObj.put("cat", 32)
internalListObj.put("dog", 33)
internalListObj.put("god", 33)

print(internalListObj.get("dog"))
print(internalListObj.get("god"))