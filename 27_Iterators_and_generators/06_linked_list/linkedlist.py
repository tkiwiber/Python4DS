from _collections_abc import Iterable


class Node:

    def __init__(self, data=None, next_node=None) -> None:
        self.data = data
        self.next_pointer = next_node


class LinkedList:

    def __init__(self) -> None:

        self.base = None
        self.head = None
        self.next_pointer = None

    def append(self, data: Node) -> None:

        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next_pointer:
                current = current.next_pointer
            current.next_pointer = new_node
        else:
            self.head = new_node
            self.base = self.head

    def get(self, index: int) -> Node:

        current = self.head
        i = 0
        if index == 0:
            return current.data
        while current.next_pointer:
            i += 1
            current = current.next_pointer
            if i == index:
                return current.data

        raise Exception('LinkedList index error')

    def remove(self, index: int) -> None:

        if self.head is None:
            raise Exception('LinkedList is empty')
        if index == 0:
            self.head = self.head.next_pointer
            return

        previous_node = self.head
        current_node = self.head.next_pointer

        i = 1
        while current_node.next_pointer:
            if i == index:
                previous_node.next_pointer = current_node.next_pointer
                return
            previous_node = current_node
            current_node = current_node.next_pointer
            i += 1
        if i == index:
            previous_node.next_pointer = current_node.next_pointer
            return

        raise Exception('LinkedList index error')

    def __iter__(self) -> Iterable[int]:
        self.head = self.base
        return self

    def __next__(self) -> Node:
        if not self.head:
            raise StopIteration
        else:
            item = self.head.data
            self.head = self.head.next_pointer
            return item

    def __str__(self) -> str:
        current = self.head
        list_str = ''
        while current:
            list_str = ''.join([list_str, str(current.data), ' -> '])
            current = current.next_pointer
        list_str = ''.join([list_str, 'NULL'])
        return list_str



