# sudoku_solver

This mini-project was done while i was learning about the **Backtracking Algorithm**, which is a technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time.

Returning to the basic algorithm that all human apply while solving **Sudoku**, we just need to follow the next steps:
  1. Look for an empty case
  2. Try to place digits (1-9) in this case
  3. Check if that digit is valid
      -if it is valid: try to fill recursively the board (the next cases) using the previous steps (1->3)
      -if not: reset the case, and go back to the previous step
  4. Once the board is full, we have finished and resolved the problem.
  
 
#Implementation

##Vizualisation function
This function quite simply helps to show us the board of sudoku, here I just used 9x9 sudoku table (we can implement any dimension for this algorithm), very easy and basic function that print a multidimensionnel table, isn't it ?

##Looking for an empty case function
In my scenario, the empty cases are the ones who have "0" value, so all we need is to loop the table until we find an empty case, and return the (row, column) values.
