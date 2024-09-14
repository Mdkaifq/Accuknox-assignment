class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self._current_index = 0  # Keeps track of the current state during iteration

    def __iter__(self):
        self._current_index = 0  # Reset index for a fresh iteration
        return self

    def __next__(self):
        if self._current_index == 0:
            self._current_index += 1
            return {'length': self.length}
        elif self._current_index == 1:
            self._current_index += 1
            return {'width': self.width}
        else:
            raise StopIteration  # Stop iteration after length and width are yielded

rectangle = Rectangle(10, 5)

for dimension in rectangle:
    print(dimension)
