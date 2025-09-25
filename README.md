# Redesigning Sipser’s NFA into a One-Cycle Form

## What this repo is
This repo has the work for our COMP382 Group Assignment 1, Question 9.
The original NFA accepts strings of `0`s where the length is divisible by 2 or 3. Sipser’s version uses an epsilon transition to “split” into two cycles.  
We redesigned it into a single 6-state cycle that uses modular arithmetic (mod 6) to handle both divisibility checks at once.  

The full explanation, diagrams, and proof are in the PowerPoint.  
This repo contains everything in one place; the slides, the Python code, and the Graphviz files we used.  

---

## Files in this repo
- **Assignment1_Presentation.pptx** – our main presentation with explanations, diagrams, and proof.  
- **Assignment1 NFA.py** – Python file that runs both the original and redesigned automata for different string lengths and shows the results.  
- **original_nfa.dot** / **redesigned_nfa.dot** – Graphviz files that describe both automata, which can be turned into diagrams.  
- **README.md** – this file.  

---

## How to use the Python file
1. Make sure you have Python 3 installed.  
2. Run the program from terminal:  
   ```bash
   python3 nfa_compare.py
   ```  
3. It will print out lengths 0–20 and show whether each automaton accepts or rejects. You can see that both machines always match.  

---

## How to install and run Graphviz
Graphviz is the tool we used to generate the automata diagrams from `.dot` files.  

### Install Graphviz (macOS with Homebrew)
```bash
brew install graphviz
```

### Install Graphviz (Linux Debian/Ubuntu)
```bash
sudo apt-get install graphviz
```

### Install Graphviz (Windows)
Download the installer from: https://graphviz.org/download/  
Then add Graphviz to your PATH so the `dot` command works in terminal.  

---

## Render the diagrams
Once Graphviz is installed, run these commands inside the repo folder:  
```bash
dot -Tpng original_nfa.dot -o original_nfa.png
dot -Tpng redesigned_nfa.dot -o redesigned_nfa.png
```

This will create PNG images of both NFAs that you can open for yourself.  

---

## Notes
- All the in-depth explanations and the full proof are in the PowerPoint, not here.  
- We used GitHub Projects to track tasks (backlog, in progress, in review, done).  
- This repo is a clean way combine all applicable material and files together.
