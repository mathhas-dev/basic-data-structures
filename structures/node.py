class Node():
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f"data: {str(self.data)}\nnext: {str(self.next.data)}"

    def __str__(self) -> str:
        return str(self.data)


class BinaryNode():
    def __init__(self, data=None) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"data: {str(self.data)}\nleft: {str(self.left.data)}\nright: {str(self.right.data)}"

    def __str__(self) -> str:
        return str(self.data)
