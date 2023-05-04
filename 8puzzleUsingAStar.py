def heuristic(current, goal, gn):
    hn = 0
    for i in range(9):
        if current[i] != goal[i] and current[i] != 0:
            hn += 1
    return hn + gn

def index(current):
    for i in range(9):
        if current[i] == 0:
            return i

def solving(possible, current, goal, iter, arrcost):
    index_ = index(current)
    arr = possible[index_]
    newcosts = []
    curnew = current.copy()
    min_ = float("inf")
    ind = 0
    for j in range(len(arr)):
        currentnew = current.copy()
        currentnew[index_] = current[arr[j]]
        currentnew[arr[j]] = 0
        val = heuristic(currentnew, goal, iter)
        newcosts.append(val)
        if newcosts[j] < min_:
            ind = j
            min_ = newcosts[j]
            curnew = currentnew
    print("CURRENT PUZZLE ARRANGEMENT IS:")
    print(*curnew)
    arrcost.append(newcosts[ind])
    print("---------------------------------------------------")
    if curnew != goal:
        solving(possible, curnew, goal, iter + 1, arrcost)
    else:
        print("SUCCESSFUL!!")

start = [2, 8, 3, 1, 6, 4, 7, 0, 5]
goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]
possibilities = {0: [1, 3],
                 1: [0, 2, 4],
                 2: [1, 5],
                 3: [0, 4, 6],
                 4: [1, 3, 5, 7],
                 5: [2, 4, 8],
                 6: [3, 7],
                 7: [6, 4, 8],
                 8: [7, 5]}
arrcost = []
sumtotal = 0
heuristic(start, goal, 0)
solving(possibilities, start, goal, 0, arrcost)
sumtotal = sum(arrcost)
print("TOTAL COST IS:", sumtotal)
