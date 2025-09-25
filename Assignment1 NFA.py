# Original NFA acceptance: divisible by 2 or 3
def original_accepts(k):
    return (k % 2 == 0) or (k % 3 == 0)

# Redesigned NFA acceptance: divisible by 2 or 3 via mod 6 residues
def redesigned_accepts(k):
    return (k % 6) in {0, 2, 3, 4}

# Compare results for 0 to 20
print("Length | Original | Redesigned")
for k in range(21):
    print(f"{k:6} | {original_accepts(k)}     | {redesigned_accepts(k)}")
