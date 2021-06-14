import sys,copy, Gameboard as gb, Uninformed, Informed

args = sys.argv[1:len(sys.argv)]
#print(args)

initialState = "123456789ABCDEF ";
searchMethod = "AStar";
option = None

if(len(args) > 0):
    initialState = args[0]
    searchMethod = args[1]
    option = "h1"


if len(args)==3:
    option = args[2]

#Goal states
goal1 = gb.Gameboard("123456789ABCDEF ")
goal2 = gb.Gameboard("123456789ABCDFE ")
board = gb.Gameboard(initialState)

if board.is_solvable():
    if (searchMethod == "BFS"):
        depth, numCreated, numExpanded, maxFringe, path = Uninformed.BFS(board, goal1, goal2)
    elif (searchMethod == "DFS"):
        depth, numCreated, numExpanded, maxFringe, path = Uninformed.DFS(board, goal1, goal2)
    elif (searchMethod == "DLS"):
        depth, numCreated, numExpanded, maxFringe, path = Uninformed.DLS(board, goal1, goal2, option)
    elif (searchMethod == "ID"):
        depth, numCreated, numExpanded, maxFringe, path = Uninformed.ID(board, goal1, goal2, option)
    elif (searchMethod == "GBFS"):
        depth, numCreated, numExpanded, maxFringe, path = Informed.GBFS(board, goal1, goal2, option)
    elif (searchMethod == "AStar"):
        depth, numCreated, numExpanded, maxFringe, path = Informed.AStar(board, goal1, goal2, option)
    else:
        depth = None
        numCreated = None
        numExpanded = None
        maxFringe = None
        path = None
        print("INVALID SEARCH METHOD")

    print(depth, ", ", numCreated, ", ", numExpanded, ", ", maxFringe)
    print("PATH: ", path)

else:
    print("Unsolvable board state")






