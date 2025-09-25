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
- **README.md** – this file.  

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
