from structures.node import Node

# Queue is a linear structure. Elements are inserted always in rear of the queue.
# Removal order is FIRST to LAST.
# This is called FIFO (first-in-first-out)

# Basic methods:
# - push
# - pop
# - peek


class Queue():
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self._size = 0

    def push(self, item) -> None:
        """
        insert an item into the queue
        """
        node = Node(item)

        if self.first is None:
            self.first = node

        if self.last:
            # the next is the newer
            self.last.next = node

        self.last = node
        self._size += 1

        print("Item inserted successfully!")

    def pop(self):
        """
        Always remove from the beginning of the queue
        """
        if self.first:
            removed_item = self.first
            self.first = self.first.next

            if self.first is None:
                self.last = None

            self._size -= 1

            print("Item removed successfully!")
            return removed_item
        else:
            print("No items to be removed!")

    def peek(self):
        if self.first:
            return self.first.data
        return self.first

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        data = ""
        next = self.first

        if self._size > 0:
            while(next):
                data = data + str(next.data) + " "
                next = next.next

        return data

    def __str__(self) -> str:
        return self.__repr__()
