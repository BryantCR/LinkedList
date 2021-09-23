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

    def deleteNode(self, val):
        print(f"deleteNode method is looking for the Node => {val}")
        current = self.head
        previous = self.head
        print(self.head.val)
        print(current.val)
        print(val)

        if self.head == val:
            self.head 0 self.head.next
            current.next = None

        while current != None and current.val != val:
            print(current.val)
            print(val)
            previous = current
            current = current.next
        print(f"Node Found => {current.val}")

            if current != None:
                previous.next = current.next
                current.next = None
