#Priority Queue
class PriorityQueue:
    def __init__(self):
        self.arr=[]
        self.size=0
    def insert(self,priority,value):
        if self.arr==[]:
            self.arr.append([priority,value])
        else:
            for i in range(self.size):
                if self.arr[i][0]>priority:
                    self.arr.insert(i,[priority,value])
                    break
            else:
                self.arr.append([priority,value])
        self.size+=1
    def remove(self):
        return(self.arr.pop(0))
    def printqueue(self):
        print("Priority\tValue")
        for element in self.arr:
            print(f"{element[0]}\t\t{element[1]}")
queue=PriorityQueue()
queue.insert(10,"Hi")
queue.insert(20,"He")
queue.insert(15,"Hr")
queue.insert(12,"Ht")
queue.insert(17,"Hy")
queue.insert(2,"Ht")
#print(queue.remove())
queue.printqueue()