from queue import PriorityQueue
import copy

#A star
def AStar(gameBoard,goalState1, goalState2, h):

    hueristic = Hueristic1 if h == "h1" else Hueristic2
    depth = -1
    numCreated = 0
    numExpanded = 0
    maxFringe = 0

    visited = []
    queue = PriorityQueue()

    startState = copy.deepcopy((gameBoard))
    queue.put((0,gameBoard))
    visited.append(gameBoard)
    # Infinite loop until found
    while queue:

        maxFringe = max(maxFringe, queue.qsize())
        currentState = queue.get()[1]

        #Goal found
        if currentState == goalState1 or currentState == goalState2:
            break
        else:
            for d in ('r','d','l','u'):
                if(currentState.can_move(d)):
                    numCreated +=1
                    newState = copy.deepcopy(currentState)
                    newState.order = numCreated
                    newState.move(d)
                    if newState not in visited:
                        state_heuristic = hueristic(newState,goalState1,goalState2)
                        queue.put((state_heuristic + len(newState.path),newState))
                        visited.append(newState)

        numExpanded += 1

    depth = len(currentState.path)
    return depth, numCreated if depth != -1 else 0, numExpanded if depth != -1 else 0, maxFringe if depth != -1 else 0, currentState.path

#Greedy Best First
def GBFS(gameBoard,goalState1, goalState2, h):

    hueristic = Hueristic1 if h == "h1" else Hueristic2
    depth = -1
    numCreated = 0
    numExpanded = 0
    maxFringe = 0

    visited = []
    queue = PriorityQueue()

    startState = copy.deepcopy((gameBoard))
    queue.put((0,gameBoard))
    visited.append(gameBoard)
    # Infinite loop until found
    while queue:

        maxFringe = max(maxFringe, queue.qsize())
        currentState = queue.get()[1]

        # Goal found
        if currentState == goalState1 or currentState == goalState2:
            break
        else:
            for d in ('r','d','l','u'):
                if(currentState.can_move(d)):
                    numCreated +=1
                    newState = copy.deepcopy(currentState)
                    newState.order = numCreated
                    newState.move(d)
                    if newState not in visited:
                        state_heuristic = hueristic(newState,goalState1,goalState2)
                        queue.put((state_heuristic,newState))
                        visited.append(newState)

        numExpanded += 1

    depth = len(currentState.path)
    return depth, numCreated if depth != -1 else 0, numExpanded if depth != -1 else 0, maxFringe if depth != -1 else 0, currentState.path

#Number of misplaced tiles
def Hueristic1(boardState, goalState1, goalState2):
    mismatch1 = 0
    mismatch2 = 0
    for i in range(len(boardState.flat)):
        if boardState.flat[i] != " " and boardState.flat[i] != goalState1.flat[i]:
            #print(boardState.flat[i])
            mismatch1 += 1
        if boardState.flat[i] != " " and boardState.flat[i] != goalState2.flat[i]:
            mismatch2 += 1

    return min(mismatch1,mismatch2)

#Total manhattan distance to target
def Hueristic2(boardState, goalState1, goalState2):
    dict = {}
    for r in range(boardState.rows):
        for c in range(boardState.columns):
            dict[boardState.grid[r][c]]=(r,c)

    total_distance1 = 0
    total_distance2 = 0
    for r in range(boardState.rows):
        for c in range(boardState.columns):
            if (r,c) != boardState.blank:
                xdiff = abs(dict[goalState1.grid[r][c]][0] - r)
                ydiff = abs(dict[goalState1.grid[r][c]][1] - c)
                total_distance1 += xdiff + ydiff
                xdiff = abs(dict[goalState2.grid[r][c]][0] - r)
                ydiff = abs(dict[goalState2.grid[r][c]][1] - c)
                total_distance2 += xdiff + ydiff

    return min(total_distance1,total_distance2)