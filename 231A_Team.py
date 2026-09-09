# Codeforces 231A - Team
# https://codeforces.com/problemset/problem/231/A
# Rating: 800 (Easy)

n = int(input())
implemented = 0

for _ in range(n):
    a, b, c = map(int, input().split())
    if a + b + c >= 2:
        implemented += 1

print(implemented)

# --------------------------- FULL EXPLANATION ---------------------------
#
# PROBLEM STATEMENT
# ----------------
# Three friends — Petya, Vasya and Tonya — take part in a contest.
# There are n problems. For each problem, each friend says whether
# they are sure about the solution: 1 = sure, 0 = not sure.
# The friends will IMPLEMENT a solution to a problem only if at
# least TWO of them are sure about it.
#
# Task: count how many problems the friends will implement.
#
# Input format:
#   Line 1: n (1 <= n <= 1000)  — number of problems
#   Next n lines: three integers a b c, each 0 or 1
# Output format:
#   One integer — the number of problems they will implement.
#
# KEY OBSERVATION
# ---------------
# Each value is either 0 or 1, so "at least two friends are sure"
# is equivalent to:   a + b + c >= 2
#
# Why? The sum a + b + c simply counts how many friends are sure:
#   0 -> nobody sure        -> skip
#   1 -> only one sure      -> skip
#   2 -> two sure           -> implement   ✓
#   3 -> all three sure     -> implement   ✓
# No conditionals like (a==1 and b==1) or ... are needed — the
# sum does all the work. This is a common trick when flags are 0/1.
#
# ALGORITHM
# ---------
# 1. Read n.
# 2. Repeat n times:
#      a. Read the three values a, b, c using map(int, input().split()).
#      b. If a + b + c >= 2, increment a counter.
# 3. Print the counter.
#
# Sample walkthrough (statement example):
#   "1 1 0"  -> sum 2 -> implement
#   "1 1 1"  -> sum 3 -> implement
#   "1 0 0"  -> sum 1 -> skip
#   Answer: 2 ✓
#
# EDGE CASES / DETAILS
# --------------------
#   - All zeros rows          -> never counted.
#   - All ones rows           -> always counted (sum = 3).
#   - n up to 1000            -> an int counter is more than enough;
#     maximum possible answer is 1000.
#   - Values are only 0/1     -> no validation needed per constraints.
#
# COMPLEXITY
# ----------
#   Time : O(n)  — constant work (3 reads + 1 add + 1 compare) per line.
#   Space: O(1)  — just a few counters; input is consumed line by line,
#          nothing is stored.
#
# LESSON
# ------
#   When binary flags are involved, SUMMING them is a clean way to
#   count "how many are true". Recognizing such tiny math tricks
#   keeps easy problems genuinely easy.
#
# PYTHON NOTES
# ------------
#   - map(int, input().split()) reads multiple integers from one line.
#     input().split() splits by whitespace, map(int, ...) converts each.
#   - a, b, c = ... unpacks the three values into separate variables.
#   - implemented += 1 is Python's increment (no ++ operator exists).
#   - for _ in range(n): is the Python idiom for repeating n times.