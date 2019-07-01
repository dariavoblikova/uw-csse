import bank

class node:
    def __init__(self, key, value = None):
        self.__key = key
        self.__value = value
        self.__leftChild = None
        self.__rightChild = None

    def getLeftChild(self):
        return self.__leftChild

    def getRightChild(self):
        return self.__rightChild

    def setLeftChild(self, theNode):
        self.__leftChild = theNode

    def setRightChild(self, theNode):
        self.__rightChild = theNode

    def getValue(self):
        return self.__value

    def setValue(self, value):
        self.__value = value

    def getKey(self):
        return self.__key

    def setKey(self, key):
        self.__key = key

    def isLeaf(self):
        return self.getLeftChild() == None and self.getRightChild() == None

    def __str__(self):
        return str(self.__key) + " : " + str(self.__value)

class BinarySearchTree:
    def __init__(self):
        self.__root = None
        self.__size = 0

    def size(self):
        return self.__size

    def isEmpty(self):
        return self.size() == 0

    def get(self, key):
        #currentNode = node(key) to help with coding, knows that it's a node and shows autocomplete
        currentNode = self.__root
        while currentNode != None:
            if currentNode.getKey() == key:
                return currentNode.getValue()
            elif key < currentNode.getKey():
                currentNode = currentNode.getLeftChild()
            else:
                currentNode = currentNode.getRightChild()
        return None

    def __getitem__(self, key):#overloads []
        return self.get(key)

    def contains(self, key):
        if self.get(key) != None:
            return True
        else:
            return False

    def put(self, key, value):
        if self.isEmpty():
            self.__root = node(key, value)
            self.__size = 1
            return
        currentNode = self.__root
        while currentNode != None:
            if currentNode.getKey() == key:
                currentNode.setValue(value)
                return
            elif currentNode.getKey() > key:
                if currentNode.getLeftChild() == None:
                    newNode = node(key, value)
                    currentNode.setLeftChild(newNode)
                    break
                else:
                    currentNode = currentNode.getLeftChild()
            else:
                if currentNode.getRightChild() == None:
                    newNode = node(key, value)
                    currentNode.setRightChild(newNode)
                    break
                else:
                    currentNode = currentNode.getRightChild()
        self.__size += 1

    def __setitem__(self, key, value):
        self.put(key, value)

    def inOrderTraversal(self, func):
        theNode = self.__root#different
        self.__inOrderTraversalRec(self.__root, func)

    def __inOrederTraversalRec(self, theNode, func):
        if theNode != None:
            self.__inOrederTraversalRec(theNode.getLeftChild(), func)
            func(theNode.getValue())#different
            self.__inOrderTraversalRec(theNode.getRightChild(), func)

    #PreOrder (Polish Notation)
    def preOrderTraversal(self, func):
        theNode = self.__root
        self.__preOrderTraversalRec(self.__root, func)

    def __preOrderTraversalRec(self, theNode, func):
        if theNode != None:
            func(theNode.getKey(), theNode.getValue())
            self.__preOrderTraversalRec(theNode.getLeftChild(), func)
            self.__preOrderTraversalRec(theNode.getRightChild(), func)

    #PostOrder
    def postOrderTraversal(self, func):
        theNode = self.__root
        self.__postOrderTraversalRec(self.__root, func)

    def __postOrderTraversalRec(self, theNode, func):
        if theNode != None:
            self.__postOrderTraversalRec(theNode.getLeftChild(), func)
            self.__postOrderTraversalRec(theNode.getRightChild(), func)
            func(theNode.getKey(), theNode.getValue())
    
    #finish
    def remove(self, key):
        if self.__root == None:
            return None
        if self.__root.getKey() == key:
            self.__size -= 1
            if self.__root.getLeftChild() == None:
                self.__root = self.__root.getRightChild()
            elif self.__root.getRightChild() == None:
                self.root = self.__root.getLeftChild()
            else:
                replaceNode = self.__getAndRemoveRightSmall(self.__root)
                self.__root.setkey(replaceNode.getKey())
                self.__root.setValue(replaceNode.getValue())
        else:
            currentNode = self.__root
            while currentNode != None:
                if currentNode.getLeftChild() and currentNode.getLeftChild().getKey() == key:
                    foundNode = currentNode.getLeftChild()
                    if foundNode.isLeaf():
                        currentNode.setLeftChild(None)
                    elif foundNode.getLeftChild() == None:
                        currentNode.setLeftChild(foundNode.getRightChild())
                    elif foundNode.getRightChild() == None:
                        currentNode.setLeftChild(foundNode.getLeftChild())
                    else:
                        replaceNode = self.__getAndRemoveRightSmall(foundNode)
                        foundNode.setKey(replaceNode.getKey())
                        foundNode.setValue(replaceNode.getValue())
                    break
                elif currentNode.getRightChild() and currentNode.getRightChild().getKey() == key:
                    foundNode = currentNode.getRightChild()
                    if foundNode.isLeaf():
                        currentNode.setRightChild(None)
                    elif foundNode.getLeftChild() == None:
                        currentNode.setRightChild(foundNode.getRightChild())
                    elif foundNode.getRightChild == None:
                        currentNode.setRightChild(foundNode.getLeftChild())
                    else:
                        replaceNode = self.__getAndRemoveRightSmall(foundNode)
                        foundNode.setKey(replaceNode.getKey())
                        foundNode.setValue(replaceNode.getValue())
                    break
                elif currentNode.getKey() > key:
                    currentNode = currentNode.getLeftChild()
                else:
                    currentNode = currentNode.getRightChild()
            if currentNode != None:
                self.__size -= 1

    def __str__(self):#not working properly
        currentNode = self.__root
        if currentNode != None:
            s = str(currentNode)
            if currentNode.getLeftChild() != None:
                s = str(currentNode.getLeftChild()) + str(", ") + s
            if currentNode.getRightChild() != None:
                s += ' ' + str(currentNode.getRightChild())
            return s
        return ''

    def Display(self):
        self.display(self.__root)

    def display(self, inNode):
        if inNode is not None:
            self.display(inNode.getLeftChild())
            if isinstance(inNode.getValue(), bank.Account):
                inNode.getValue().displayAllFunds()
            else:
                print(f"{inNode.getKey()} {inNode.getValue()} ")
            self.display(inNode.getRightChild())
