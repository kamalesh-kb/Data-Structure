class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    """ linked list insertion methods"""
    def push(self, new_data):
        new_head = Node(new_data)
        new_head.next = self.head
        self.head = new_head
        self.size += 1

    def insert_at_mid(self, new_data):
        new_node = Node(new_data)
        mid = self.size // 2
        temp = self.head
        prev = temp
        pos = 0

        while pos < mid:
            prev = temp
            temp = temp.next
            pos += 1

        new_node.next = prev.next
        prev.next = new_node
        self.size += 1


    def append(self, new_data):
        new_end = Node(new_data)
        end = self.head

        while end.next:
            end = end.next

        end.next = new_end
        self.size += 1

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
        self.size += 1

    def insert_using_key(self, key, new_data):
        new_node = Node(new_data)
        temp = self.head
        prev = temp
        while temp:
            if temp.data is key:
                break
            prev = temp
            temp = temp.next

        new_node.next = prev.next
        prev.next = new_node
        self.size += 1

    """linked list deletion methods"""
    def delete_at_beginning(self):
        self.head = self.head.next
        self.size -= 1

    def delete_at_mid(self):
        temp = self.head
        mid = self.size // 2
        pos = 0
        prev = temp
        while pos < mid:
            prev = temp
            temp = temp.next
            pos += 1

        prev.next = temp.next
        del temp
        self.size -= 1

    def pop(self):
        end = self.head
        prev = end
        while end.next:
            prev = end
            end = end.next

        prev.next = None
        del end
        self.size -= 1

    def delete_at_position(self, position):
        pos = 0
        temp = self.head
        prev = temp

        c = 0
        while temp:
            temp = temp.next
            c += 1
        temp = self.head
        if position > c:
            print('The position is out of range')
            print('Please enter the position between 0 and', c)

        if position == 0:
            self.head = self.head.next
            return

        while pos < position:
            prev = temp
            temp = temp.next
            pos += 1

        prev.next = temp.next
        self.size -= 1

    def remove(self, key): #method to do deletion using key
        temp = self.head
        prev = temp
        if temp.data is key:
            self.head = self.head.next
            return
        while temp:
            if temp.data is key:
                break
            prev = temp
            temp = temp.next

        prev.next = temp.next
        del temp
        self.size -= 1


    """ method to find the length of the linked list"""
    def get_length(self):
        print('length of the linked list is', self.size)

    def get_node(self, value):
        temp = self.head
        c = -1
        while temp:
            if temp.data is value:
                c += 1
                print('value', value, 'is in the node', c, 'in the linked list')
                break
            c += 1
            temp = temp.next
        if temp is None:
            print('the entered value', value, 'is not in the linked list')

    def get_value(self, node):
        print(self.size)
        if node >= self.size:
            print('the given node is out of range')
            return
        c = 0
        temp = self.head
        while c < node:
            temp = temp.next
            c += 1

        print('the value in node', node, 'is', temp.data)

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
l.size += 4

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

print('\n\nthe linked list after deleting_at_beginning')
l.delete_at_beginning()
l.delete_at_beginning()
l.display()

print('\n\nthe linked list after popping operations')
l.pop()
l.pop()
l.pop()
l.display()

print('\n\nthe linked list after deleting using delete_at_position method')
l.delete_at_position(3)
l.delete_at_position(9)
l.delete_at_position(0)
l.display()

print('\n\nmethod to find the length of the linked list')
print('the length of the linked list is', l.get_length())

print('\n\nthe linked list after remove operations(deletion using key)')
l.remove(27)
l.remove(9)
l.remove(3)
l.display()

print('\n\nthe linked list after delete_at_mid operations')
l.delete_at_mid()
l.display()

print('\n\nthe linked list after insert_at_mid operations')
l.insert_at_mid(0)
l.display()

print('\n\n')
l.get_node(0)

print('\n\n')
l.get_value(3)