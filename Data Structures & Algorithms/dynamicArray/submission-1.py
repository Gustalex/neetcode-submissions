class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size >= self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1


    def popback(self) -> int:
        last_index = self.size - 1
        last_element = self.arr[last_index]
        self.arr[last_index] = 0
        self.size -= 1
        return last_element

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        old_arr = self.arr
        new_arr = [0] * new_capacity

        for i in range(self.size):
            new_arr[i] = old_arr[i]

        self.arr = new_arr
        self.capacity = new_capacity

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:        return self.capacity