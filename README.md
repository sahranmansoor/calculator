# calculator
task1-4 of python developer intership

# Math Expression Parser

A lightweight, procedural math expression parser and evaluator written in Python. Built without using Object-Oriented Programming (classes) to demonstrate core Computer Science concepts using pure functions and data structures.

## Features

- **Basic Arithmetic:** Supports addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- **Parentheses:** Fully supports nested parentheses for complex expressions.
- **Operator Precedence:** Correctly follows the standard order of operations (BODMAS).
- **Interactive REPL:** Includes a continuous Read-Eval-Print Loop for quick calculations.
- **Error Handling:** Gracefully catches syntax errors, mismatched parentheses, and division by zero.

## How It Works

The program processes math expressions in three distinct phases:

1. **Lexical Analysis (Tokenizer):** Scans the raw string character-by-character and groups them into meaningful tokens (Numbers, Operations, Symbols).
2. **Infix to Postfix Conversion:** Uses the **Shunting Yard Algorithm** with an operator stack to convert standard human-readable math (Infix: `3 + 4 * 2`) into machine-friendly Reverse Polish Notation (Postfix: `3 4 2 * +`).
3. **Postfix Evaluation:** Reads the Postfix expression from left to right, using a single evaluation stack to compute the final result.

## Usage

Simply run the script in your terminal:

```bash
python calculator.py
```

### Example Session:

```text
Type 'exit' to quit.

calc > 5 + 10 * 2
25
calc > (5 + 10) * 2
30
calc > 10 / (5 - 5)
MATH ERROR: can not divide by zero
calc > 5 + * 2
SYNTAX ERROR: invalid expression
calc > exit
Exiting...
```
