# Codeforces 617A - Elephant
# https://codeforces.com/problemset/problem/617/A
# Rating: 800 (Easy) — Greedy / Math

x = int(input())

steps = (x + 4) // 5
print(steps)

# --------------------------- FULL EXPLANATION ---------------------------
#
# PROBLEM STATEMENT
# ----------------
# An elephant is standing at point 0 on the x-axis and wants to reach
# his friend at point x (1 <= x <= 10^6). In one stride he can move
# exactly 1, 2, 3, 4 or 5 units forward. Movement is only rightward.
#
# Question: what is the MINIMUM number of strides to reach point x
# exactly?
#
# Input format:
#   One line: the friend's position x.
# Output format:
#   One integer — the minimum number of strides.
#
# KEY INSIGHT — GREEDY WITH THE LARGEST STRIDE
# --------------------------------------------
# Since every stride length 1..5 is available, the optimal strategy is
# to take as many length-5 strides as possible and finish with one
# shorter stride (or none).
#
# Maximizing stride length minimizes count:
#   - x = 12  -> 5 + 5 + 2            -> 3 strides
#   - x = 26  -> 5+5+5+5+5+1          -> 6 strides
#   - x = 10  -> 5 + 5                -> 2 strides (exact)
#
# So the answer is ceil(x / 5), which in integer arithmetic is:
#       (x + 4) // 5
#
# (Adding 5-1 = 4 before floor-dividing implements ceil division for
#  positive integers: (x + d - 1) // d == ceil(x / d).)
#
# ALGORITHM
# ---------
# 1. Read x.
# 2. Print (x + 4) // 5.
#
# SAMPLE WALKTHROUGH
# ------------------
# Input: 12  -> (12 + 4) // 5 = 16 // 5 = 3   (5+5+2) ✓
# Input: 5   -> (5  + 4) // 5 =  9 // 5 = 1   (one 5-stride) ✓
# Input: 26  -> (26 + 4) // 5 = 30 // 5 = 6   ✓
#
# EDGE CASES / DETAILS
# --------------------
#   - x = 1    -> 1 stride of length 1.
#   - x = 5    -> 1 stride (exact multiple).
#   - x = 10^6 -> (10^6 + 4) // 5 = 200000; fits easily in `int`.
#   - No division precision issues: Python's // is exact integer math.
#
# COMPLEXITY
# ----------
#   Time : O(1)  — one addition and one division after reading a number.
#   Space: O(1)  — one variable.
#
# LESSON
# ------
#   When movements come in sizes 1..k and any size is usable at any
#   time, the greedy "use the largest available size" is optimal, so
#   the answer is simply ceil(x / largest). The (n + d - 1) // d
#   trick for computing ceil(n / d) with integers is a must-know
#   idiom for competitive programming.
#
# PYTHON NOTES
# ------------
#   - int(input()) reads an integer from a single line.
#   - // is floor division; combining it with +4 implements ceil(x/5).
#   - Whole problem fits in 2 lines of code — Python shines here.