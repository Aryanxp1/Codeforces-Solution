# Codeforces 791A - Bear and Big Brother
# https://codeforces.com/problemset/problem/791/A
# Rating: 800 (Easy)

a, b = map(int, input().split())

years = 0
while a <= b:
    a *= 3
    b *= 2
    years += 1

print(years)

# --------------------------- FULL EXPLANATION ---------------------------
#
# PROBLEM STATEMENT
# ----------------
# Limak (bear a) weighs a kg, his brother Bob (bear b) weighs b kg
# (1 <= a <= b <= 10). Every year, Limak's weight TRIPLES
# (a -> 3*a) while Bob's weight DOUBLES (b -> 2*b).
#
# Question: after how many whole years will Limak become strictly
# heavier than Bob (a > b)?
#
# Input format:
#   One line: two integers a b.
# Output format:
#   One integer — the number of years needed.
#
# KEY INSIGHT — SIMULATION IS FINE
# --------------------------------
# Because Limak's multiplier (3x) is bigger than Bob's (2x), the
# gap a/b grows by a factor of 3/2 every year, so Limak ALWAYS
# overtakes Bob eventually. Starting with a >= 1 and b <= 10,
# the worst case is a = 1, b = 10:
#   1v10 -> 3v20 -> 9v40 -> 27v80 -> 81v160 -> 243v320 -> 729v640
#   -> overtakes in year 6.
# So the loop runs at most ~6 times — we can simply SIMULATE
# year by year instead of solving any math formula.
#
# ALGORITHM
# ---------
# 1. Read a and b with map(int, input().split()).
# 2. Set years = 0.
# 3. While a <= b (Limak not heavier yet):
#      a *= 3   (triple Limak)
#      b *= 2   (double Bob)
#      years += 1
# 4. Print years.
#
# SAMPLE WALKTHROUGH
# ------------------
# Example 1: a = 4, b = 9
#   Year 1: 4*3=12, 9*2=18   -> 12v18 (still lighter)
#   Year 2: 12*3=36, 18*2=36 -> 36v36 (tied, not strictly heavier)
#   Year 3: 36*3=108, 36*2=72 -> 108v72 (heavier!)
#   -> answer 3 ✓
#
# Example 2: a = 4, b = 7
#   4v7 -> 12v14 -> 36v28 -> answer 2 ✓
#
# Example 3: a = 1, b = 1
#   1v1 -> 3v2 -> answer 1 ✓ (one year is all it takes: 3 > 2)
#
# EDGE CASES / DETAILS
# --------------------
#   - a == b at start (e.g. "1 1") -> exactly 1 year (3 > 2).
#   - Constraint a <= b guarantees the loop runs at least once.
#   - Values stay tiny (max a ~729), so no overflow concerns at all.
#   - The loop ALWAYS terminates because 3/2 > 1 forces a/b to grow.
#
# COMPLEXITY
# ----------
#   Let k = number of years (at most ~6 for these constraints).
#   Time : O(k) — constant work per year, k tiny.
#   Space: O(1) — just three integers (a, b, years).
#
# LESSON
# ------
#   Not every problem needs a formula. When the state space is
#   tiny and each step is cheap, SIMULATE the process directly —
#   it is easier to write, easier to verify, and plenty fast.
#   The "while condition-not-met: update state" pattern is the
#   workhorse of simulation problems.
#
# PYTHON NOTES
# ------------
#   - a, b = map(int, input().split()) reads and converts two
#     space-separated integers in one line (unpacking).
#   - a *= 3 / b *= 2 are in-place multiply-assign operators.
#   - while a <= b: keeps looping until Limak is heavier.
#   - No fixed loop count needed — the condition controls it; this
#     is the key difference from for _ in range(n) problems.
