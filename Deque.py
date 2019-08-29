class Queue:
    def __init__(self):
        self.queue = []
        # инициализация хранилища данных
    def enqueue(self, item):
        self.queue.insert(0,item)
        # вставка в хвост
    def dequeue(self):
        if self.size() < 1:
            return None # если стек пустой
        return self.queue.pop(self.size()-1)
        
    def size(self):
        return len(self.queue) # размер очереди
