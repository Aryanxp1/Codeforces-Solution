# Codeforces 282A - Bit++
# https://codeforces.com/problemset/problem/282/A
# Rating: 800 (Easy)

n = int(input())
counter = 0

for _ in range(n):
    s = input()

    if s == "X++" or s == "++X":
        counter += 1
    elif s == "X--":
        counter -= 1

print(counter)

# --------------------------- FULL EXPLANATION ---------------------------
#
# PROBLEM STATEMENT
# ----------------
# The problem involves a variable (initially 0) that starts at 0.
# There are n operations (1 <= n <= 100), each being one of three types:
#   "X++"  -> increment the variable by 1
#   "++X"  -> increment the variable by 1
#   "X--"  -> decrement the variable by 1
#
# Task: after processing all n operations, output the final value of the variable.
#
# Input format:
#   Line 1: n (number of operations)
#   Next n lines: one of "X++", "++X", or "X--"
#
# Output format:
#   One integer - the final value of the variable.
#
# KEY INSIGHT
# -----------
# The variable is incremented if the string contains "++",
# and decremented if it contains "X--". The trick is that "++X"
# and "X++" are both increment operations - the position of "++"
# doesn't matter, only that it appears somewhere in the string.
#
# ALGORITHM
# ---------
# 1. Read n (number of operations)
# 2. Initialize counter = 0
# 3. Repeat n times:
#      a. Read string s
#      b. If s is "X++" or "++X", increment counter
#      c. If s is "X--", decrement counter
# 4. Print counter
#
# SAMPLE WALKTHROUGH
# ------------------
# Input:
#   3
#   X++
#   ++X
#   X--
#
# Steps:
#   - Read "X++" -> counter becomes 1
#   - Read "++X" -> counter becomes 2
#   - Read "X--" -> counter becomes 1
# Output: 1
#
# EDGE CASES & DETAILS
# --------------------
#   - The string is always exactly 3 characters long (no spaces)
#   - Operations are guaranteed to be one of the three types
#   - n is at most 100, so a simple loop is sufficient
#   - Initial value is 0 (as per problem statement)
#   - No need for complex parsing - direct string comparison works
#
# COMPLEXITY
# ----------
#   Time : O(n) - constant time per operation (string comparison)
#   Space: O(1) - only a few variables used
#
# LESSON
# ------
#   This problem teaches string comparison and how to parse simple
#   command patterns. The key insight is that "++" always means
#   increment regardless of position, and "X--" always means
#   decrement. Recognizing this pattern makes the solution trivial.
#
# PYTHON NOTES
# ------------
#   - Python uses 'and' / 'or' / 'not' for logical operators.
#   - counter += 1 and counter -= 1 are the Python increment/decrement.
#   - input() reads the line; no need for cin >> extraction.
#   - for _ in range(n): is the Python loop idiom.