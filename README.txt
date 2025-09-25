# Redesigning Sipser’s NFA into a One-Cycle Form

## Overview
This repo contains the deliverables for our project in automata theory.  
The goal was to take Sipser’s original NFA (which checks divisibility by 2 or 3) and redesign it into a cleaner 6-state cycle using modular arithmetic.  
The full explanation and proof are in the PowerPoint — this README just explains how to use the files here.  

---

## Files in this repo
- **Assignment1_Presentation.pptx** – main slides with all explanations, diagrams, and proof.  
- **Assignment1_NFA.py** – Python script that compares the original and redesigned NFAs.  
- **original_nfa.dot** / **redesigned_nfa.dot** – Graphviz files describing both automata.  
- **README.txt** – this file.  

---

## How to run the Python code
1. Make sure you have Python 3 installed.  
2. From terminal, run:  
   ```bash
   python3 Assignment1_NFA.py
   ```  
3. The program prints results for string lengths 0–20, showing that both NFAs always agree.  

---

## How to render the diagrams
To turn the `.dot` files into images, install [Graphviz](https://graphviz.org).  

### macOS (Homebrew)
```bash
brew install graphviz
```

### Ubuntu/Debian Linux
```bash
sudo apt-get install graphviz
```

### Windows
Download from: https://graphviz.org/download/  

### Generate images
```bash
dot -Tpng original_nfa.dot -o original_nfa.png
dot -Tpng redesigned_nfa.dot -o redesigned_nfa.png
```

---

## Notes
- All the detailed explanations and the proof are in the PowerPoint.  
- The code and `.dot` files are here to make the project reproducible.  

---

## References
- Sipser, M. (2012). *Introduction to the Theory of Computation* (3rd ed.). Cengage Learning. (Source of Figure 1.34 and the original NFA example)
- Graphviz. (2025). *Graph Visualization Software*. Retrieved from https://graphviz.org (Used to generate automaton diagrams)
- Python Software Foundation. (2025). *Python 3 Documentation*. Retrieved from https://www.python.org/doc/ (Used for simulation code of the redesigned NFA)
- Microsoft. (2025). *Visual Studio Code*. Retrieved from https://code.visualstudio.com
- GeeksforGeeks. (2024). *Modular Arithmetic and Applications*. Retrieved from https://www.geeksforgeeks.org/modular-arithmetic/ (Background reference on modular arithmetic applied in automata design)
- Homebrew. (2025). *The Missing Package Manager for macOS (or Linux)*. Retrieved from https://brew.sh (Used as a package manager to install Graphviz via MacOS terminal)
- W3Schools. (2025). *Python % Operator*. Retrieved from https://www.w3schools.com/python/ref_mod.asp (Modulo operator explanation)
