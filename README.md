# Scientific Calculator Interpreter

A terminal based calculator implemented in python that takes natural language queries and evaluates the scientific expression

## Prerequisites
python 2.7

PLY - python lex and yacc

## Installing

pip install ply

RUN `calc1.py` file

## Description

The program is to implement a scientific calculator that accept input as natural language queries and evaluates the expression.

The Scientific expression may include any of the following functions
- Basic arithmatic operations
- Logarithmic Operations
- Trigonometric operations
- Squares and squareroots
- Power function
- Logical functions
- Factorial
- There are four registers A,B,C,D

# Examples
```
Available registers are A,B,C,D
calc>Find the sum of 2 and 1000
1002 

calc>what is the factorial of 5
120

calc>ln(0)
Math domain error

calc>what is the product of sin 30 degrees and cos 60 degrees
0.25 

calc>A = 50

calc>B = 10

calc>A/B
5

calc>1 AND 1
1
```
