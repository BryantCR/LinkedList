from LinkedList import LinkedList

# At this point the list is empty
listOfNumbers = LinkedList()

# Adding the first node to the list
#listOfNumbers.insertLast( 10 )
#listOfNumbers.insertLast( 30 )
#listOfNumbers.insertLast( 50 )
#listOfNumbers.insertLast( 80 )
#listOfNumbers.insertFirst(50)
#listOfNumbers.insertFirst(30)
#listOfNumbers.insertFirst(20)
#listOfNumbers.printList()
#listOfNumbers.findNode(30)
#listOfNumbers.deleteNode(50)
#listOfNumbers.count()
#listOfNumbers.insertAtPosition(30, 10)
#listOfNumbers.printList()

# listOfNumbers.insertLast( 10 )
# listOfNumbers.insertLast( 5 )
# listOfNumbers.insertLast( 20 )
# listOfNumbers.insertLast( 15 )
# listOfNumbers.insertLast( 30 )

listOfNewNodes = listOfNumbers.insertLast( 30 ).insertLast( 20 ).insertLast( 50 )

# listOfNumbers.insertAtPosition( 5, 50 )
listOfNumbers.printList()

listOfNumbers.findMaximumValueNode(listOfNewNodes)
