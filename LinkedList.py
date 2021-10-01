from Node import Node

class LinkedList:
    def __init__( self ):
        self.head = None
    
    def insertLast( self, val ):
        newNode = Node( val )
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode
    
    def printList( self ):
        current = self.head
        while current != None:
            print( current.val )
            current = current.next

    def insertFirst( self, val ):
        newNode = Node( val )
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def findNode( self, val ):#Do this one
        print(f"findNode method is looking for the Node => {val}")
        current = self.head
        print(self.head.val)
        while current.val != val:
            current = current.next
        print(f"findNode method Found the Node => {current.val}")

    # def findNode( self, val ):
    #     current = self.head
    #     while current != None:
    #         if current.val == val:
    #             return current
    #         current = current.next
    #     return None

    # def deleteNode(self, val):
    #     print(f"deleteNode method is looking for the Node => {val}")
    #     current = self.head
    #     previous = self.head
    #     print(self.head.val)
    #     print(current.val)
    #     print(val)

    #     if self.head.val == val:
    #         self.head = self.head.next
    #         current.next = None
    #     else:
    #     while current != None and current.val != val:
    #         print(current.val)
    #         print(val)
    #         previous = current
    #         current = current.next
    #     print(f"Node Found => {current.val}")

    #         if current != None:
    #             previous.next = current.next
    #             current.next = None
    def deleteNode( self, val ):
        if self.head == None:
            return None
        current = self.head
        previous = self.head
        if self.head.val == val:
            self.head = self.head.next
            current.next = None
        else:
            while current != None and current.val != val:
                previous = current
                current = current.next
            if current != None:
                previous.next = current.next
                current.next = None
    
    # Validate the index, that it exists in the list (lenght() counts how many elements we have)
    #def countNodes():
    #    count = 0
    #    if self.head == None:
    #        count = 0
    #    else:
    #        count = count + 1
    # Move along the list until the given index to add it
    # If list is empty do not add if the index is not 0
    # def insertAtPosition(self, val1, val2):
    #     if self.head == None:
    #         return None
    #     else:
    #         self.findNode( val1 )
    #         newNode = Node( val2 )
    #         current = self.head
    #         while current.next != None:
    #             current = current.next
    #         current.next = newNode

    def length( self ):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def insertAtPosition( self, index, val ):
        newNode = Node( val )
        if index <= self.length():
            if index == 0:
                self.insertFirst( val )
            else:
                count = 0
                current = self.head
                while count < index - 1:
                    count += 1
                    current = current.next
                newNode.next = current.next
                current.next = newNode

    def moveHighestToLast( self ):
        if self.length() > 1:
            max = self.head
            current = self.head
            prevToMax = self.head
            prevToCurrent = self.head
            
            while current.next != None:
                prevToCurrent = current
                current = current.next
                if current.val > max.val:
                    max = current
                    prevToMax = prevToCurrent

            if self.head.val == max.val:
                self.head = self.head.next
            if max.val != current.val:
                prevToMax.next = max.next
                current.next = max
                max.next = None

    def bubbleSort(self, num):
        for i in range (0, len(num) -1, 1):
            for n in range (1 +1, len(num), 1):
                if num[n] > num[n+1]:
                    temp = nun[n]
                    num[n] = num[n+1]
                    num[n+1] = temp

    def removeNegativeNumbers(self, listes):
        positiveNumbers = []
        for i in range (0, len(listes) ,1):
            if listes[i] > 0:
                positiveNumbers.append(listes[i])
            listes = positiveNumbers
            print(listes)



# Find the maximun value inside a list of numbers and move it to the last node
    # def findMaximumValueNode( self, val2 ):
    #     listOfNodes = val2[0]
    #     for i in val2:
    #         if i > listOfNodes:
    #             listOfNodes = i
                
    #     print(listOfNodes)
        
        # count = 0
        # if self.head == None:
        #     count = 0
        #     else:
        #         count = count + 1

        # if self.head == None:
        #     return None
        #     else:
        #         newNode = Node( val2 )
        #         current = self.head
        #         while current.next != None:
        #             current = current.next
        #         current.next = newNode
# Find the minimum value inside a list of numbers and move it to the head of the list

