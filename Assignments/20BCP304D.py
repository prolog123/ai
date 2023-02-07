class priorityQueue:
    def _init_(self):
        self.queue = []
    
    def add(self, child, parent, cost):
        index = 0
        for i in self.queue:
            if i[2] < cost:
                index+=1
            if i[0] == child:
                if cost > i[2]:
                    return
                else:
                    self.queue.remove(i)
                    break
        self.queue.insert(index, (child, parent, cost))
    
    def pop(self):
        if len(self.queue) != 0:
            return self.queue.pop(0)
        else:
            print("Queue is Empty")
            return False
    
    def isEmpty(self):
        return len(self.queue) == 0

class State:
    def _init_(self, rows, cols, array):
        self.rows = rows
        self.cols = cols
        self.array = array
    
    def getChild(self):
        ind = self.array.index("*")
        r = ind // (self.cols)
        c = ind % (self.cols)

        child = []

        if r-1 >= 0:
            child.append(State(self.rows, self.cols, swap([i for i in self.array], r*self.rows+c, (r-1)*self.rows+c)))
        if r+1 < self.rows:
            child.append(State(self.rows, self.cols, swap([i for i in self.array], r*self.rows+c, (r+1)*self.rows+c)))
        if c-1 >= 0:
            child.append(State(self.rows, self.cols, swap([i for i in self.array], r*self.rows+c, r*self.rows+c-1)))
        if c+1 < self.cols:
            child.append(State(self.rows, self.cols, swap([i for i in self.array], r*self.rows+c, r*self.rows+c+1)))

        return child
    
    # calculate heuristic values
    def heuristic(self, goal):
        cost = 0
        for i in range(self.rows*self.cols):
            if goal.array[i] != self.array[i]:
                cost+=1
        return cost
    
    def show(self):
        print('[', end=" ")
        for i in range(self.rows-1):
            print(self.array[ i*self.rows : (i*self.rows) + self.cols ], end=", ")
        print(self.array[-self.cols : ], end="]\n")

# returns an instance of a possible path
def makeState(rows, cols):
    array = []

    for i in range(rows*cols):
        val = input("Enter "+str(i+1)+" element: ")
        if val!="*":
            val = int(val)
        array.append(val)
    return array

# swap positions of the matrix
def swap(arr, ind1, ind2):
    arr[ind1], arr[ind2] = arr[ind2], arr[ind1]
    return arr

def findNode(name, List):
    for i in List:
        if i.name == name:
            return i

def check(ele, List, index, cost):
    for i in List:
        if i[index].array == ele.array:
            if i[2] < cost:
                return True
            else:
                List.remove(i)
                return False
    return False

def CostFunction(child, level, goal):
    return child.heuristic(goal) + level

def AStar(start, goal):
    priorQ = priorityQueue()
    priorQ.add(start, None, CostFunction(start, 0, goal))
    visited = []
    current = None

    while not priorQ.isEmpty():
        lowest = priorQ.pop()
        myCost = lowest[2]
        current = lowest[0]

        for child in current.getChild():
            fcost = CostFunction(child, myCost - current.heuristic(goal) + 1, goal)
            if not check(child, visited, 0, fcost):
                priorQ.add(child, current, fcost)
        
        visited.append(lowest)
        if current.array == goal.array:
            break
    
    print("Traversal path:")
    for i in visited:
        i[0].show()

    path = []
    current = goal
    cost = 0

    for j in visited[::-1]:
        if j[0].array == current.array:
            if current.array==goal.array:
                cost = j[2]
            path.append(current)
            current = j[1]

    print("\n\nActual path:")
    for i in path[:0:-1]:
        i.show()

    path[0].show()
    print("Cost:",cost )


rows = int(input("Enter no. of rows: "))
cols = int(input("Enter no. of cols: "))

print("Enter initial State: ")
Start = State(rows, cols, makeState(rows, cols))
print("\nEnter Final State: ")
Goal = State(rows, cols, makeState(rows, cols))

AStar(Start, Goal)
