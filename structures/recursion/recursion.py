class Recursion:
    def factorial(self, n: int) -> int:
        # Base
        if n == 1:
            return 1
        
        # Recursive case
        return n * self.factorial(n-1)

    def fibonacci(self, n: int) -> int:
        # Base case
        if n == 0:
            return 0
        elif n == 1:
            return 1

        # Recursive case
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)


if __name__ == "__main__":
    recursion = Recursion()

    print(f"\nn! = {recursion.factorial(9)}\n")
    print(f"\n\nfn = {recursion.fibonacci(6)}\n")
