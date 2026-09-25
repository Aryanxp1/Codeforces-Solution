# Codeforces 69A - Young Physicist
# https://codeforces.com/problemset/problem/69/A
# Rating: 800 (Easy) — Vector sums

n = int(input())

sx = sy = sz = 0

for _ in range(n):
    x, y, z = map(int, input().split())
    sx += x
    sy += y
    sz += z

print("YES" if sx == sy == sz == 0 else "NO")

# --------------------------- FULL EXPLANATION ---------------------------
#
# PROBLEM STATEMENT
# ----------------
# A point body is at rest. n force vectors are applied to it; the
# i-th vector has components (x_i, y_i, z_i). If the SUM of all the
# vectors is the zero vector, the body remains at rest.
#
# Task: print "YES" if the body stays at rest, otherwise "NO".
#
# Input format:
#   Line 1: n (1 <= n <= 100).
#   Next n lines: three integers x y z, each in [-100, 100].
# Output format:
#   "YES" or "NO".
#
# KEY INSIGHT — SUM THE COMPONENTS SEPARATELY
# -------------------------------------------
# Vector addition is component-wise, so the total force is
#       X = sum of all x_i,   Y = sum of all y_i,   Z = sum of all z_i
# The body stays at rest iff X = 0 AND Y = 0 AND Z = 0.
#
# No geometry is needed — just three accumulators and a final check.
#
# ALGORITHM
# ---------
# 1. Initialize sx = sy = sz = 0.
# 2. For each of the n vectors: add x to sx, y to sy, z to sz.
# 3. Print "YES" if sx == 0 and sy == 0 and sz == 0, else "NO".
#
# SAMPLE WALKTHROUGH
# ------------------
# Vectors: (4,1,7) (-2,4,-1) (1,-5,-3)
#   X = 4 - 2 + 1 = 3,  Y = 1 + 4 - 5 = 0,  Z = 7 - 1 - 3 = 3
#   X != 0 -> "NO" ✓
#
# Vectors: (3,-1,7) (-5,2,-4) (2,-1,-3)
#   X = 3 - 5 + 2 = 0,  Y = -1 + 2 - 1 = 0,  Z = 7 - 4 - 3 = 0
#   all zero -> "YES" ✓
#
# EDGE CASES / DETAILS
# --------------------
#   - All zero vectors   -> sums stay 0 -> YES.
#   - Some components are negative -> they cancel correctly through
#     plain addition (no absolute values!).
#   - n can be 1: a single vector is "at rest" only if it is (0,0,0).
#   - Bounds: |component| <= 100, n <= 100 -> sums stay within
#     [-10000, 10000]; a plain int easily holds them.
#
# COMPLEXITY
# ----------
#   Let n = number of vectors (<= 100).
#   Time : O(n) — read and sum each vector once.
#   Space: O(1) — only three running sums.
#
# LESSON
# ------
#   "Is the total vector zero?" is "are all component sums zero?".
#   Problems that sound like physics/math usually collapse into
#   simple per-component accumulation. Chained comparisons in Python
#   (sx == sy == sz == 0) make the final check read exactly like
#   the intended condition.
#
# PYTHON NOTES
# ------------
#   - sx = sy = sz = 0 initializes all three in one statement.
#   - x, y, z = map(int, input().split()) unpacks a line into three.
#   - sx == sy == sz == 0 is Python's chained comparison: true iff
#     all three are equal to each other AND to 0 (three-way check).