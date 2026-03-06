# exercise 1
class CircularBuffer:
    def __init__(self, buffer_size):
        self._buffer_size = buffer_size
        self._buffer = []
        
    @property
    def buffer_size(self):
        return self._buffer_size
    
    def put(self, obj):
        self._buffer.append(obj)
        if len(self._buffer) > self._buffer_size:
            self._buffer.pop(0)
        
    def get(self):
        if not self._buffer:
            return None
        return self._buffer.pop(0)

buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True
# better version
class CircularBuffer:
    def __init__(self, buffer_size):
        self._buffer_size = buffer_size
        self._buffer = [None for i in range(buffer_size)]
        self._next = 0
        self._oldest = 0
        
    @property
    def buffer_size(self):
        return self._buffer_size
    
    def put(self, obj):
        if self._buffer[self._next] is not None:
            self._oldest = (self._next + 1) % self.buffer_size
        
        self._buffer[self._next] = obj
        self._next = (self._next + 1) % self.buffer_size
            
    def get(self):
        value = self._buffer[self._oldest]
        self._buffer[self._oldest] = None
        if value is not None:
            self._oldest = (self._oldest + 1) % self.buffer_size
        return value
        

buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.get())             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True

# exercise 2
# exercise 3
# exercise 4
# exercise 5
# exercise 6