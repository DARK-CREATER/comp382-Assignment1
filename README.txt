# Redesigning Sipser’s NFA into a One-Cycle Form

## Overview
This project explores an automaton example from Michael Sipser’s *Introduction to the Theory of Computation*. 
The original nondeterministic finite automaton (NFA) accepts strings of zeros where the string length is divisible by 2 or 3. 
While correct, Sipser’s design uses an epsilon-transition to nondeterministically “guess” whether to check divisibility by 2 or 3. 
This project redesigns that automaton into a single six-state cycle using modular arithmetic, making the construction simpler and more compact.

The repository includes:
- A presentation explaining the redesign and proof of equivalence.
- Python code demonstrating and comparing the original and redesigned NFAs.
- Diagrams of both automata.

---

## How It Works

### Original NFA
- The machine begins with an epsilon-transition (a free move without reading input).
- It can branch into:
  - A 2-state cycle that accepts strings of even length.
  - A 3-state cycle that accepts strings whose length is divisible by 3.
- The empty string is also accepted since 0 is divisible by both 2 and 3.

### Redesigned NFA (One-Cycle)
- Removes nondeterminism and the epsilon-transition.
- Uses **6 states**, each representing a remainder when dividing the string length by 6.
- Accepting states are q0, q2, q3, and q4, corresponding to lengths divisible by 2 or 3.
- This redesign captures both divisibility conditions in one unified cycle.

---

## Code Demonstration
A Python script is provided to test equivalence between the original and redesigned NFAs.

```python
def original_accepts(k):
    return (k % 2 == 0) or (k % 3 == 0)

def one_cycle_accepts(k):
    return (k % 6) in {0, 2, 3, 4}

for i in range(21):
    print(i, original_accepts(i), one_cycle_accepts(i))
```

### Sample Output
```
0 True True
1 False False
2 True True
3 True True
4 True True
5 False False
6 True True
7 False False
8 True True
9 True True
10 True True
...
```

This confirms both NFAs accept exactly the same strings.

---

## Empirical Comparison
Every integer length falls into one of six remainder classes modulo 6: 0, 1, 2, 3, 4, 5.

| Remainder | Divisible By? | Accept/Reject |
|-----------|---------------|---------------|
| 0         | 2 and 3       | Accept        |
| 1         | Neither       | Reject        |
| 2         | 2             | Accept        |
| 3         | 3             | Accept        |
| 4         | 2             | Accept        |
| 5         | Neither       | Reject        |

This table explains why the six-state machine works: all possible lengths are covered.

---

## Proof Summary
1. **State tracking:** By induction, after reading *k* symbols, the redesigned NFA is in state q(k mod 6).
2. **Acceptance condition:** The machine accepts if the state is in {q0, q2, q3, q4}.
3. **Arithmetic connection:** If *k* is divisible by 2 or 3, then k mod 6 ∈ {0, 2, 3, 4}, and vice versa.

Together, these steps prove the redesigned automaton recognizes the same language as the original.

---

## How to Run

### Requirements
- **Python 3** (https://www.python.org/downloads/)
- **Graphviz** (https://graphviz.org) for generating automaton diagrams
- **Homebrew** (macOS/Linux only) for installing dependencies easily:  
  ```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  brew install graphviz
  ```
- **Visual Studio Code** (optional, for editing/running Python code)

### Running the Code
1. Save the Python snippet to a file, e.g. `nfa_compare.py`.
2. Run in terminal:
   ```bash
   python3 nfa_compare.py
   ```
3. Check that both outputs match for all tested string lengths.

---

## References
Sipser, M. (2012). *Introduction to the Theory of Computation* (3rd ed.). Cengage Learning.  
Graphviz. (2025). *Graph Visualization Software*. Retrieved from https://graphviz.org  
Python Software Foundation. (2025). *Python 3 Documentation*. Retrieved from https://www.python.org/doc/  
Microsoft. (2025). *Visual Studio Code*. Retrieved from https://code.visualstudio.com  
GeeksforGeeks. (2024). *Modular Arithmetic and Applications*. Retrieved from https://www.geeksforgeeks.org/modular-arithmetic/  
Homebrew. (2025). *The Missing Package Manager for macOS (or Linux)*. Retrieved from https://brew.sh  
W3Schools. (2025). *Python % Operator*. Retrieved from https://www.w3schools.com/python/ref_mod.asp  
