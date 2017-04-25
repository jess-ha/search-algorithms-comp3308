# search-algorithms-comp3308

This is my solution to the Three-Digit Puzzle outlined in the COMP3308 assignment specification as described below. 

## The Three-Digit Puzzle
Given are two 3‐digit numbers called   (start) and   (goal) and also a set of 3‐digit numbers called          . To solve the puzzle, we want to get from   to   in the smallest number of moves. A move is a transformation of one number into another number by adding or subtracting 1 to one of its digits. For example, a move can take you from 123 to 124 by adding 1 to the last digit or from 953 to 853 by subtracting 1 from the first digit. Moves must satisfy the following constraints:
1. You cannot add to the digit 9 or subtract from the digit 0;
2. You cannot make a move that transforms the current number into one of the forbidden
numbers;
3. You cannot change the same digit twice in two successive moves.
Note that since the numbers have 3 digits, at the beginning there are at most 6 possible moves from  . After the first move, the branching factor is at most 4, due to the constraints on the moves and especially due to constraint 3.
For the purpose of this assignment numbers starting with 0, e.g. 018, are considered 3‐digit numbers.

Heuristics utilised in informed algorithms were to be generated using the Manhattan heuristic.

The Manhattan heuristic for a move between two numbers A and B is the sum of the absolute differencesofthecorrespondingdigitsofthesenumbers,e.g. h(123,492) = |1 - 4| + |2 - 9| + |3 - 2| = 11.

## Usage
`$ python ThreeDigits.py <algorithm> <input text file>`

Possible algorithims:
- `A` A*
- `B` Breadth-first search
- `D` Depth-dirst search
- `G` Greedy search
- `H` Hill-climbing search
- `I` Iterative deepening search

### Input Format
Input formats were specified to be three lines containing:
`start-state`
`goal-state`
`forbidden1,forbidden2,forbidden3,...,forbiddenN (optional)`

Examples are provided in the sample_input directory of the repository.

For the purpose of this university assessment, we were instructed to assume all input provided was correctly formatted and all values given were appropriate for the puzzle.
