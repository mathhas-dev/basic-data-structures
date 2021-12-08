from structures.node import Node

# Stacks are like stacking books. Put one, then another.
# To remove, it has to be the last inserted.
# Removal order is LAST to FIRST.
# This is called LIFO (last-in-first-out)

# Basic methods:
# - push
# - pop
# - peek


class Stack():
    def __init__(self) -> None:
        self.top = None
        self._size = 0

    def push(self, item) -> None:
        """
        insert an item into the stack
        """
        node = Node(item)

        if self.top:
            # the next is the previous
            node.next = self.top

        self.top = node
        self._size += 1

        print("Item inserted successfully!")

    def pop(self):
        """
        Always remove from top of stack
        """
        if self.top:
            removed_item = self.top
            self.top = self.top.next
            self._size -= 1

            print("Item removed successfully!")
            return removed_item
        else:
            print("No items to be removed!")

    def peek(self):
        if self.top:
            return self.top.data
        return self.top

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        data = ""
        next = self.top

        if self._size > 0:
            while(next):
                data = data + str(next.data) + "\n"
                next = next.next

        return data

    def __str__(self) -> str:
        return self.__repr__()
