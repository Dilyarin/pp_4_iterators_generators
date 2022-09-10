# Итератор:
nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

class FlatIterator:
    def __init__(self, list):
        self.start = 0
        self.end = 0
        self.list = list
        self.stopped = False

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stopped:
            while self.start < len(self.list):
                if self.end < len(self.list[self.start]):
                    i = self.list[self.start][self.end]
                    self.end += 1
                    return i
                self.start += 1
                self.end = 0
            self.stopped = True
            raise StopIteration

# Генератор:

nested_list_new = [i for n in nested_list for i in n]


if __name__ == '__main__':
    flat_list = list(FlatIterator(nested_list)) #Итератор
    print(flat_list)

    print(nested_list_new) #Генератор

