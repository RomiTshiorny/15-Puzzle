import copy
#Iterative Deepening
def ID(gameBoard,goalState1, goalState2, maxDepth):
    count = 0
    while(count < int(maxDepth)):
        count+=1
        #Just call DLS with increasing maxdepth
        depth, numCreated, numExpanded, maxFringe, path = DLS(gameBoard,goalState1, goalState2, count)
        if(depth != -1):
            break

    return depth, numCreated, numExpanded, maxFringe, path


#Depth-Limited Search
def DLS(gameBoard,goalState1, goalState2, maxDepth):
    depth = -1
    numCreated = 0
    numExpanded = 0
    maxFringe = 0

    visited = []
    stack = []
    found = False

    stack.append(gameBoard)
    visited.append(gameBoard)
    # Infinite loop until found or limit reached
    while stack:

        maxFringe = max(maxFringe, len(stack))
        currentState = stack.pop()
        # Goal found
        if currentState == goalState1 or currentState == goalState2:
            found = True
            break
        else:
            # reverse order for stack
            for d in ('u', 'l', 'd', 'r'):
                if (currentState.can_move(d)):
                    numCreated += 1
                    newState = copy.deepcopy(currentState)
                    newState.move(d)
                    if newState not in visited and (len(currentState.path) < int(maxDepth)):
                        stack.append(newState)
                        visited.append(newState)

        numExpanded += 1

    depth = len(currentState.path) if found else -1
    return depth, numCreated if depth != -1 else 0, numExpanded if depth != -1 else 0, maxFringe if depth != -1 else 0, currentState.path

#Depth-First Search
def DFS(gameBoard,goalState1, goalState2):
    depth = -1
    numCreated = 0
    numExpanded = 0
    maxFringe = 0

    visited = []
    stack = []

    stack.append(gameBoard)
    visited.append(gameBoard)

    #Infinite loop until found
    while stack:

        maxFringe = max(maxFringe, len(stack))
        currentState = stack.pop()

        if currentState == goalState1 or currentState == goalState2:
            break
        else:
            #reverse order for stack
            for d in ('u','l','d','r'):
                if(currentState.can_move(d)):
                    numCreated +=1
                    newState = copy.deepcopy(currentState)
                    newState.move(d)
                    if newState not in visited:
                        stack.append(newState)
                        visited.append(newState)

        numExpanded += 1

    depth = len(currentState.path)
    return depth, numCreated if depth != -1 else 0, numExpanded if depth != -1 else 0, maxFringe if depth != -1 else 0, currentState.path

#Breadth-First Search
def BFS(gameBoard,goalState1, goalState2):
    depth = -1
    numCreated = 0
    numExpanded = 0
    maxFringe = 0

    visited = []
    queue = []

    queue.append(gameBoard)
    visited.append(gameBoard)

    # Infinite loop until found
    while queue:

        maxFringe = max(maxFringe, len(queue))
        currentState = queue.pop(0)

        if currentState == goalState1 or currentState == goalState2:
            break
        else:
            for d in ('r','d','l','u'):
                if(currentState.can_move(d)):
                    numCreated +=1
                    newState = copy.deepcopy(currentState)
                    newState.move(d)
                    if newState not in visited:
                        queue.append(newState)
                        visited.append(newState)

        numExpanded += 1

    depth = len(currentState.path)
    return depth, numCreated if depth != -1 else 0, numExpanded if depth != -1 else 0, maxFringe if depth != -1 else 0, currentState.path
