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

class Test():

    def test_add(self):
        deq = Deque()
        test_deque = Deque()
        for i in range(10):
            deq.addTail(i)
            test_deque.addTail(i)
        print(deq.size())
        print(deq.deque)
        deq.removeFront()
        if deq.deque[0] == test_deque.deque[0]:
            print('no delete')
        print('delete in front')
        print(deq.size())
        print(deq.deque)
        deq.removeTail()
        if deq.deque[deq.size()-1] == test_deque.deque[test_deque.size()-1]:
            print('no delete')
        print('delete in tail')
        print(deq.size())
        print(deq.deque)


test = Test()
test.test_add()
#deq = Deque()
#deq.addFront("f1")
#deq.addTail("t1")
#deq.addFront("f2")
#deq.addTail("t2")
#print(deq.deque)
#print(deq.polindrom(deq.deque))
#deq1 = Deque()
#deq1.addFront('н')
#deq1.addFront('а')
#deq1.addFront('в')
#deq1.addFront('л')
#deq1.addFront('о')
#deq1.addFront('б')
#deq1.addFront(',')
#deq1.addFront('б')
#deq1.addFront('о')
#deq1.addFront('л')
#deq1.addFront('в')
#deq1.addFront('а')
#deq1.addFront('н')
#print(deq1.deque)
#print(deq1.polindrom(deq1.deque))




#while deq.size() > 0:
    #print(deq.removeFront())
    #print(deq.removeTail())

