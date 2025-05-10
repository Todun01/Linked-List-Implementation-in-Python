class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head == None:
            print("LinkedList is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' -> '
            itr = itr.next
        print(llstr)
    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    def length_of_list(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count
    def remove_at(self, index):
        if index < 0 or index >= self.length_of_list():
            raise Exception("Index out of range")
        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
            count += 1
            itr = itr.next
    def insert_at(self, index, data):
        if index < 0 or index >= self.length_of_list():
            raise Exception("Index out of range")
        if index == 0:
            self.head = Node(data, self.head)
            return
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
            count += 1
            itr = itr.next
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values([5, 3, 19, 26, 900])
    ll.print()
    ll.remove_at(2)
    ll.print()
    ll.insert_at(2, 300)
    ll.print()