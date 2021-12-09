class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f"data: {str(self.data)}\nnext: {str(self.next.data)}"

    def __str__(self) -> str:
        return str(self.data)
