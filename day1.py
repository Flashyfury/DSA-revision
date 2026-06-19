import ctypes


class mylist:

    def __init__(self):
        self.size = 1
        self.n = 0
        # create a c type array of self.size
        self.A = self.__make_array(self.size)

    def __make_array(self, capacity):
        # creates a c type array with size(fixed) capacity
        return (capacity * ctypes.py_object)()

    def __len__(self):
        return self.n

    def __str__(self):
        result = ""
        for i in range(self.n):
            result += str(self.A[i]) + ", "
        return "[" + result[:-2] + "]" if self.n > 0 else "[]"

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0:
                index = self.n + index
            if 0 <= index < self.n:
                return self.A[index]
            raise IndexError("List index out of range")
        raise TypeError("Invalid index type")

    def append(self, item):
        if self.n == self.size:
            self.__resize(self.size * 2)

        self.A[self.n] = item
        self.n += 1

    def __resize(self, new_capacity):
        B = self.__make_array(new_capacity)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.size = new_capacity

    def pop(self):
        if self.n == 0:
            raise IndexError("pop from empty list")
        val = self.A[self.n - 1]
        self.A[self.n - 1] = None
        self.n -= 1
        return val

    def insert(self, index, item):
        if index < 0:
            index = self.n + index
        if index < 0:
            index = 0
        if index > self.n:
            index = self.n

        if self.n == self.size:
            self.__resize(self.size * 2)

        for i in range(self.n, index, -1):
            self.A[i] = self.A[i - 1]

        self.A[index] = item
        self.n += 1

    def remove(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                for j in range(i, self.n - 1):
                    self.A[j] = self.A[j + 1]
                self.A[self.n - 1] = None
                self.n -= 1
                return
        raise ValueError("list.remove(x): x not in list")


if __name__ == "__main__":
    print("Testing mylist class...")
    l = mylist()
    print("Initial list:", l, "Length:", len(l))

    # Test append
    l.append(10)
    l.append(20)
    l.append(30)
    print("After appending 10, 20, 30:", l, "Length:", len(l))

    # Test indexing
    print("Element at index 1:", l[1])
    print("Element at index -1 (negative index):", l[-1])

    # Test insert
    l.insert(1, 15)
    print("After inserting 15 at index 1:", l)

    # Test pop
    popped = l.pop()
    print("Popped element:", popped)
    print("After popping:", l)

    # Test remove
    l.remove(15)
    print("After removing 15:", l)

    try:
        l.remove(99)
    except ValueError as e:
        print("Expected error when removing non-existent item:", e)

