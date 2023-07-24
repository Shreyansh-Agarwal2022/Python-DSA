class Heap:
    def __init__(self, array=[]):
        self.array = array
        self.size = len(array)

    def parent(self, index):
        return (index - 1) // 2

    def left(self, index):
        return 2 * index + 1

    def right(self, index):
        return 2 * index + 2

    def is_leaf(self, index):
        return index >= self.size // 2 and index < self.size

    def swap(self, index1, index2):
        self.array[index1], self.array[index2] = self.array[index2], self.array[index1]

    def heapify(self, index):
        while not self.is_leaf(index):
            parent_index = self.parent(index)
            if self.array[index] < self.array[parent_index]:
                self.swap(index, parent_index)
                index = parent_index

    def insert(self, value):
        self.array.append(value)
        self.size += 1
        index = self.size - 1
        while not self.is_leaf(index) and self.array[index] < self.array[self.parent(index)]:
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def heappop(self):
        minimum = self.array[0]
        self.array[0] = self.array[-1]
        self.size -= 1
        self.array.pop()
        self.heapify(0)
        return minimum

    def heappush(self, value):
        self.insert(value)
        self.heapify(self.size - 1)

    def __repr__(self):
        return str(self.array)

h=Heap()
print(h.array)