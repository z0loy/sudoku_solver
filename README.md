# sudoku_solver

This mini-project was done while i was learning about the **Backtracking Algorithm**, which is a technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time.

Returning to the basic algorithm that all human apply while solving **Sudoku**, we just need to follow the next steps:
  1. Look for an empty case
  2. Try to place digits (1-9) in this case
  3. Check if that digit is valid
      - if it is valid: try to fill recursively the board (the next cases) using the previous steps (1->3)
      - if not: reset the case, and go back to the previous step
  4. Once the board is full, we have finished and resolved the problem.
  

# Implementation

## Vizualisation function
This function quite simply helps to show us the board of sudoku, here I just used 9x9 sudoku table (we can implement any dimension for this algorithm), very easy and basic function that print a multidimensionnel table, isn't it ?

## Looking for an empty case function
In my scenario, the empty cases are the ones who have "0" value, so all we need is to loop the table until we find an empty case, and return the (row, column) values.

## Is valid funciton
This function will check if the filled digit is valid or not, there is 3 things we need to check

 **1. check if the filled digit is not repeated in the colmun**
 
  ![GitHub Logo](https://github.com/z0loy/sudoku_solver/blob/master/Images/2.jpg)
  
 **2. check if the filled digit is not repeated in the row**
 
 ![GitHub Logo](https://github.com/z0loy/sudoku_solver/blob/master/Images/1.jpg)
 
 **3. check if the filled digit is not repeated in the intern-box**
 
  ![GitHub Logo](https://github.com/z0loy/sudoku_solver/blob/master/Images/3.jpg)

The function is_valid look a little bit complicated, but in fact it's not, the given parameters are the board, the value filled in, and the position of the empty case (i,j)
  1. first when we start checking if the value is valid relatively to the column, from the position value (exactly the column value j), we start looping for each row if the value exist there or not, if it does then return False.
  2. respectively for the row checking.
  3. for the intern-box checking, there is a little trick when we need to get the range of the intern-box
    - we get the the position (i,j) of the empty case, then we divise (i/3, j/3)
    - two loops to scroll through the intern-box (per row, per column) 
    - return False if it does exist.
 
## Solve backtrack funciton

here, we'll try to use the previous funciton, and apply the backtracking algorithm.

first we check if there is no empty cases (it means that the board is all filled and we're ready to finish the execution), else if there is an empty case then we get it index (row, column), then we start trying the digit (from 1 to 9) and check if the new filled value **is_valid** using our previous funciton. if it is then recursively call the **solve_backtrack** function and return True and so on ...
