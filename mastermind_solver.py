import itertools
import random

# Generate all possible codes (6^4 = 1296 possibilities)
POSSIBILITIES = list(itertools.product(range(6), repeat=4))

def get_feedback(code, guess):
    """
    Returns (black_pegs, white_pegs)
    black_pegs: correct symbol + correct position
    white_pegs: correct symbol wrong position
    """
    black = sum(c == g for c, g in zip(code, guess))
    # Count symbols ignoring correct-position matches
    code_unused = [c for c, g in zip(code, guess) if c != g]
    guess_unused = [g for c, g in zip(code, guess) if c != g]

    white = 0
    for g in guess_unused:
        if g in code_unused:
            white += 1
            code_unused.remove(g)
    return (black, white)

def mastermind_solver(secret_code):
    possible_codes = POSSIBILITIES.copy()
    attempts = 0
    
    while True:
        attempts += 1
        
        # Choose a random guess from possible codes
        guess = random.choice(possible_codes)
        
        feedback = get_feedback(secret_code, guess)
        print(f"Attempt {attempts}: Guess {guess} => Feedback {feedback}")
        
        if feedback == (4, 0):
            print("Code cracked in", attempts, "attempts!")
            return guess
        
        # Eliminate all codes that would not give same feedback
        new_possible = []
        for code in possible_codes:
            if get_feedback(code, guess) == feedback:
                new_possible.append(code)
        possible_codes = new_possible

# Example run with a secret code
if __name__ == "__main__":
    secret = random.choice(POSSIBILITIES)
    print("Secret Code (hidden):", secret)
    mastermind_solver(secret)
