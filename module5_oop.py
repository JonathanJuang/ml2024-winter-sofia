# MSCS2202_Assignment_5.2

#TzuYi Juang

#1.Create a Python program:

class NumberList:
    def __init__(self):
        self.numbers = []

    def add_number(self, num):
        self.numbers.append(num)

    def find_index(self, x):
        for i, num in enumerate(self.numbers, start=1):
            if num == x:
                return i
        return -1

def main():
    N = int(input("Enter the number of elements (N): "))

    num_list = NumberList()

    for i in range(N):
        num = int(input(f"Enter number {i + 1}: "))
        num_list.add_number(num)

    X = int(input("Enter the number to search for (X): "))

    index = num_list.find_index(X)

    if index == -1:
        print("-1")
    else:
        print(f"The index of {X} is: {index}")

if __name__ == "__main__":
    main()
