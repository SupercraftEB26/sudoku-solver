# Sudoku Solver

A simplistic terminal based python sudoku solver, works for all **valid** sudokus.


## Description

This project is a command-line Sudoku solver written in Python.
It takes an incomplete **standard 9x9** Sudoku puzzle as input and solves it using a recursive backtracking algorithm.
The solver is designed to work with any valid Sudoku puzzle and demonstrates the use of recursion,
constraint checking, and algorithmic problem-solving. Although its worst-case time complexity is exponential,
it solves most valid Sudoku puzzles efficiently by eliminating invalid moves early.


## Getting Started

### Dependencies

* Python 3.8 or later 
* Any operating system that supports Python (Windows, macOS, or Linux)
* No external libraries are required

### Installing

1. If Python is not installed, download it from:

https://www.python.org/downloads/

2. Clone the repository:
```bash
git clone https://github.com/yourusername/sudoku-solver.git
```
clones to the current directory, if wanted to clone to a specific location:
```bash
git clone https://github.com/yourusername/sudoku-solver.git PathToLocation
```

### Formatting Sudokus

Sudokus are inputted via .txt files, with the 9x9 grid being
written as 9 lines, each lines represent a row of the grid and
therefore being 9 in length, example: 

5 0 0 **|** 4 6 7 **|** 3 0 9  
9 0 3 **|** 8 1 0 **|** 4 2 7  
1 7 4 **|** 2 0 3 **|** 0 0 0  
**------+-------+------**  
2 3 1 **|** 9 7 6 **|** 8 5 4  
8 5 7 **|** 1 2 4 **|** 0 9 0  
4 9 6 **|** 3 0 8 **|** 1 7 2  
**------+-------+------**  
0 0 0 **|** 0 8 9 **|** 2 6 0  
7 8 2 **|** 6 4 1 **|** 0 0 5  
0 1 0 **|** 0 0 0 **|** 7 0 8  

is inputted as:

500467309  
903810427  
174203000  
231976854  
857124090  
496308172  
000089260  
782641005  
010000708  

### Executing program

* Open a terminal
* Navigate to the project folder
* Run the program
```bash
python main.py sudoku.txt
```
*Note that sudoku.txt refers to the target sudoku to be solved,
if not in the same directory full path to the file must be given

## Help

* Attempt the command using python3 instead of python
```bash
python3 main.py sudoku.txt
```

* Verify that Python 3 is installed
```bash
python --version
```

* Ensure the sudoku is valid, as invalid puzzles cannot be solved,
also ensure that the sudoku is formatted correctly

## Authors

[SupercraftEB26](https://github.com/SupercraftEB26)

## Version History

See [commit change]() or See [release history]()

* 0.1
    * Initial Release

## License

This project is completely unlicensed and free forever to be used in any way shape or form.
