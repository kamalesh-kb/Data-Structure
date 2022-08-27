class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    """ linked list insertion methods"""
    def push(self, new_data):
        new_head = Node(new_data)
        new_head.next = self.head
        self.head = new_head

    def append(self, new_data):
        new_end = Node(new_data)
        end = self.head

        while end.next:
            end = end.next

        end.next = new_end

    def insert_at_position(self, new_data, position):
        new_node = Node(new_data)
        flag_node = self.head
        prev_node = flag_node
        pos = 0
        """ if the condition in the while loop is written as
        pos <= position, then the new_node will be inserted after 
        the position, which can lead to another method called 
        'insert_after_position' 
        
        likewise if we write as pos < position - 1,
        then the new_node will be inserted before the position"""
        while pos < position:
            prev_node = flag_node
            flag_node = flag_node.next
            pos += 1

        prev_node.next = new_node
        new_node.next = flag_node

    def insert_using_key(self, key, new_data):
        new_node =  Node(new_data)
        temp = self.head

        while temp:
            if temp.data is key:
                break
            prev = temp
            temp = temp.next

        new_node.next = prev.next
        prev.next = new_node



    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next


l = LinkedList()
l.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

l.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

print('The original linked list created')
l.display()

print('\n\nthe linked list after pushing operations')
l.push(10)
l.push(27)
l.push('hi')
l.push(98)
l.display()

print('\n\nthe linked list after appending operations')
l.append(87)
l.append('it can contain many data type')
l.append(23)
l.display()

print('\n\nthe linked list after inserting using insert_at_position operations')
l.insert_at_position(71, 3)
l.display()

print('\n\nthe linked list after inserting using insert_using_key operations')
l.insert_using_key(27, 100)
l.insert_using_key(87, 9)
l.insert_using_key('it can contain many data type', 'anywhere')
l.display()