15-Puzzle
AI that solves 15-puzzle using search algorithms

****************************************************
FifteenProblem.py is the main execution file
To run program using command line (windows):
'py FifteenProblem.py "123456789ABC DFE" BFS'
****************************************************

The input to the command line follows the following format:

  STARTING_STATE SEARCH OPTION
  
  STARTING_STATE: The starting configuration of the board. Surrounded in quotation marks containing the
                  Hexadecimals 1-F (CASE SENSITIVE FOR A-F) and a space for the empty block. Is inputed 
                  into the grid from the top left to bottom right.
               
  SEARCH:         The search method to be used to solve the problem. Options are BFS, DFS 
                  DLS, GBFS, and AStar (ALL CASE SENSITIVE).
                  
  OPTION:         An extra option avaible for when using GBFS (Greed-Best-First-Search) or AStar (A* search) 
                  to chose the hueristic, should be left empty for all other searches. "h1" for Hueristic 1, 
                  the number of misplaced tiles. "h2" for Hueristic 2, total manhattan distance to target
                  state. In the case of DLS (Depth-limited-Search), it is used as an integer to specify
                  the max depth to search to.
                  
  Example Uses:
                  "123456789ABC DFE" BFS
                  "123456789ABC DFE" DFS
                  "123456789AC DEBF" DLS 4
                  "123456789AC DEBF" DLS 2
                  "123456789BC DAEF" GBFS h1
                  "123456789BC DAEF" AStar h1
                  "123456789BC DAEF" GBFS h2
                  "123456789BC DAEF" AStar h2
                  
  (NOTICE) There are two valid "goal" states:
  
                  "123456789ABCDEF " AND "123456789ABCDFE "
                  (i.e F and E are interchangable).
