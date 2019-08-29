class Deque:
    def __init__(self):
        self.deque = []
        # инициализация внутреннего хранилища

    def addFront(self, item):
        self.deque.insert(0,item)
        # добавление в голову

    def addTail(self, item):
        self.deque.insert(self.size(),item)
        # добавление в хвост

    def removeFront(self):
        # удаление из головы
        if self.size() < 1:
            return None # если стек пустой
        return self.deque.pop(0)

    def removeTail(self):
        # удаление из хвоста
        if self.size() < 1:
            return None # если стек пустой
        return self.deque.pop(self.size()-1)

    def size(self):
        return len(self.deque) # размер очереди

    def polindrom(self,deque):
        reverse_deque = []
        for i in range(len(deque)):
            reverse_deque.append(deque[i])
        reverse_deque.reverse()
        if reverse_deque == deque:
            return 'Polindrom'
        return 'no polindrom'