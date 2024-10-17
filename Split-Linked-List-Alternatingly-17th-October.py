class Solution:
    # Function to append a new node with newData at the end of a linked list
    def append(self, headRef, newData):
        new_node = Node(newData)
        last = headRef[0]

        if headRef[0] is None:
            headRef[0] = new_node
            return

        while last.next:
            last = last.next
        last.next = new_node

    # Function to split a linked list into two lists alternately
    def alternatingSplitList(self, head):
        a = [None]
        b = [None]
        current = head

        while current:
            self.append(a, current.data)
            current = current.next

            if current:
                self.append(b, current.data)
                current = current.next

        return [a[0], b[0]]
