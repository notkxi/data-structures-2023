"""
Kai Ibarrondo 
Professor Guy 
Data Structures
30 November 2023
"""



class ListNode:
    def __init__(self, val: int):
        """
        ListNode: Represents a node in a singly linked list.
        Arguments:
            val (int): Value to be stored in the node.
        """
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        """
        LinkedList: Represents a singly linked list and includes operations such as push, pop, reverse, queue, average, stack, enqueue, dequeue.
        """
        self.head = None
        self.tail = None
        self.is_queue = False

    def push(self, val: int) -> None:
        """
        push: Adds a new node with the given value to the front of the linked list.
        Time complexity: O(1) - Adding a node at the head.
        Arguments:
            val (int): Value to be added to the linked list.
        """
        if self.is_queue == False: 
            if self.head == None:
                self.head = self.tail = ListNode(val)
            else:
                new_node = ListNode(val)
                new_node.next = self.head
                self.head = new_node
            linked_list_printer()
        else: 
            print("ERROR")
    
    def pop(self, num: int) -> None:
        """
        pop: Removes 'num' nodes from the front of the linked list.
        Time complexity:
            - Best case: O(1) - Removing the first node.
            - Worst case: O(n) - Removing 'num' nodes where 'n' is the number of nodes.
        Arguments:
            num (int): Number of nodes to be removed from the linked list.
        """

        if self.is_queue == False:
            count = 0
            current = self.head

            while current:
                count += 1
                current = current.next

            if num > count:
                print("ERROR")
            else:
                for i in range(num):
                    if self.head == self.tail:  
                        self.head = self.tail = None
                    else:
                        self.head = self.head.next
                linked_list_printer()        
        else: 
            print("ERROR")


    def reverse(self) -> None:
        """
        reverse: Reverses the order of nodes in the linked list.
        Time complexity: O(n) - Reversing the linked list by iterating through 'n' nodes.
        """

        previous = None
        current = self.head
        self.tail = self.head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous
    
    
    def queue(self) -> None:
        """
        queue: Changes the behavior of the linked list to act as a queue.
        Time complexity: O(1) - Changing the value.
        """
        self.is_queue = True


    def average(self) -> float: 
        """
        average: Computes the average value of all nodes in the linked list.
        Time complexity: O(n) - Computing the average by traversing 'n' nodes.
        Returns:
            float: Average value of nodes in the linked list.
        """

        sum = 0.0
        count = 0
        if self.head != None:
            current = self.head
            while current:
                sum += current.val
                count += 1
                current = current.next
            return sum / count
        else: 
            return(0.0)
        
 
    def stack(self) -> None:
        """
        stack: Changes the behavior of the linked list to act as a stack.
        Time complexity: O(1) - Changing the value.
        """

        self.is_queue = False

   
    def enqueue(self, val: int) -> None:
        """
        enqueue: Adds a new node with the given value to the end of the linked list.
        Time complexity: O(1) - Adding a node at the tail.
        Arguments:
            val (int): Value to be added to the linked list.
        """

        if self.is_queue == True: 
            if self.head == None:
                self.head = self.tail = ListNode(val)
            else:
                new_node = ListNode(val)
                self.tail.next = new_node
                self.tail = new_node
            linked_list_printer()
        else: 
            print("ERROR")
    

    def dequeue(self) -> None: 
        """
        dequeue: Removes the first node from the linked list.
        Time complexity:
            - Best case: O(1) - Removing the first node.
            - Worst case: O(n) - Removing the first node after traversing 'n' nodes.
        """

        if self.is_queue == True: 
            if self.head != None:
                if self.head == self.tail:  
                    self.head = self.tail = None
                else:
                    self.head = self.head.next
                linked_list_printer()
            else:
                print("ERROR")
        else: 
            print("ERROR")


def linked_list_printer():
    """
    linked_list_printer: Prints all the values of nodes in the linked list.
    Time complexity: O(n) - Printing 'n' nodes.
    """

    if S.head:
        current = S.head
        while current:
            print(current.val, end=" ")
            current = current.next
        print()
    else:
        print("EMPTY")

# Initialize a linked list object
S = LinkedList()

while True: 
    """
    Continuously prompts for user input until 'END' command is encountered.
    """

    operation = input().split()

    if operation[0] == "END":
        break
    if operation[0] == "PUSH":
        S.push(int(operation[1]))
    elif operation[0] == "POP":
        S.pop(int(operation[1]))
    elif operation[0] == "REVERSE":
        S.reverse()
        linked_list_printer()
    elif operation[0] == "QUEUE":
        S.queue()
    elif operation[0] == "ENQUEUE":
        S.enqueue(int(operation[1]))
    elif operation[0] == "DEQUEUE":
        S.dequeue()
    elif operation[0] == "AVERAGE":
        print(S.average())
    elif operation[0] == "STACK":
        S.stack()
    else:
        print("Invalid command.")