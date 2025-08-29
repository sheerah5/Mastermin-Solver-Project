# Mastermind Solver Project

## Introduction
Mastermind is a classic code-breaking game that requires logic and reasoning.  
In this project, we implemented an **AI-based solver** for the game using a **logical elimination strategy**.  
The goal is to demonstrate how Artificial Intelligence can solve constraint-based problems through search and optimization techniques.
##  Run Online

You can run this project directly in your browser using Binder:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sheerah5/Mastermind-Solver-Project/HEAD?urlpath=lab/tree/mastermind_solver.ipynb)

Click the button above to launch the solver without installing anything locally.

---

## Problem Description
- The game generates a **secret code** of 4 digits.  
- Each digit ranges from **0–5**.  
- The challenge is to guess the code in as few attempts as possible.  
- Feedback after each guess:
  - **Black pegs** → Correct digit in the correct position.
  - **White pegs** → Correct digit but in the wrong position.  

The solver reduces the number of possible codes after each guess by eliminating combinations that don’t match the feedback.

---

## Algorithm
1. Generate all possible codes (6⁴ = 1296 possibilities).  
2. Make an initial guess.  
3. Get feedback (black and white pegs).  
4. Eliminate all codes that would not produce the same feedback.  
5. Repeat until the code is solved (4 black pegs).  

This method efficiently narrows down possibilities using logical elimination.

---

## Implementation
The project is implemented in **Python** using:
- `itertools` → To generate possible combinations.  
- `random` → To select guesses from the possible codes.  

---

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/mastermind-solver.git
   cd mastermind-solver
   ```

2. Run the solver:
   ```bash
   python mastermind_solver.py
   ```

The program will randomly select a secret code and attempt to solve it step by step.

---

## Example Output
```
Secret Code (hidden): (3, 5, 1, 2)
Attempt 1: Guess (0, 4, 3, 2) => Feedback (1, 1)
Attempt 2: Guess (3, 5, 1, 2) => Feedback (4, 0)
Code cracked in 2 attempts!
```

---

## Contributors
- **Bashirat Shaibu**  
- **Umar Faruk Abubakar**  
- **Victor Kevin**  
- **Maleek Isa**

---

## Conclusion
This project demonstrates how a logical elimination algorithm can efficiently solve the Mastermind game. By applying feedback iteratively, our AI program narrows down the possibilities and finds the correct code, showcasing the power of AI in solving logic-based problems.
