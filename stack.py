class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

class Stack:
    def __init__(self):
        self._head = None
        # _size is useful if we want len(s) in O(1)
        self._size = 0

    def isEmpty(self):
        return self._head == None

    def __iter__(self):
        cursor = self._head
        while cursor is not None:
            yield cursor
            cursor = cursor.next

    def push(self, value):
        # generate the node
        node = Node(value)
        # point to the current head
        node.next = self._head
        # declare the new node a head
        self._head = node
        # Update _size if we want len(stack) in O(1)
        self._size += 1

    def pop(self):
        if self.isEmpty():
            raise RuntimeError('Empty stack')
        
        # Step 1: save the curr head
        head = self._head
        # Step 2: the next node is the new head
        self._head = self._head.next

        # Update _size if we want len(stack) in O(1)
        self._size -= 1

        # Step 3: return the value of the 
        # (old) top of the stack
        return head.value

    def __len__(self):

        # O(n)
        '''
        counter = 0
        node = self._head
        
        while node:
            counter += 1
            node = node.next

        return counter
        '''
        # O(1): if we have an additional
        # attribute _size
        # and we update it in push/pop
        return self._size


    def peek(self):
        if self.isEmpty():
            raise RuntimeError('Empty stack')
        return self._head.value

    def __str__(self):
        '''returns a string given a stack'''
        result = ''

        node = self._head
        
        while node != None:
            result += f'{node}->'
            node = node.next
        
        return result
    
#if __name__ == '__main__':
s = Stack()
