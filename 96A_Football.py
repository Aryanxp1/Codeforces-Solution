# Codeforces 96A - Football
# https://codeforces.com/problemset/problem/96/A
# Rating: 900 (Easy) — Runs of consecutive characters

s = input().strip()

count = 1          # current run length (first char starts a run of length 1)
dangerous = False

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
        if count >= 7:
            dangerous = True
            break
    else:
        count = 1   # run broken — reset

print("YES" if dangerous else "NO")

# --------------------------- FULL EXPLANATION ---------------------------
#
# PROBLEM STATEMENT
# ----------------
# Football players stand in a single row; a 0 means one team's player
# and a 1 means the other team's player (a binary string s).
# The situation is called DANGEROUS if there are at least 7 players of
# the SAME team in a ROW one after another.
#
# Task: print "YES" if dangerous, otherwise "NO".
#
# Input format:
#   One line: the string s (1..100 chars).
# Output format:
#   "YES" or "NO".
#
# KEY INSIGHT — TRACK THE CURRENT RUN LENGTH
# ------------------------------------------
# A "run" is a maximal block of equal consecutive characters. Instead
# of checking every window of 7, keep ONE counter: as we walk the
# string, if the next char equals the previous one we extend the run
# (count += 1); otherwise the run breaks and we reset it to 1.
# The moment count reaches 7 we can stop and answer YES.
#
# This is the classic "longest run / first run of length k" pattern,
# useful in endless variations (streaks, consecutive days, etc.).
#
# ALGORITHM
# ---------
# 1. count = 1 (the first character starts a run of length 1).
# 2. For i in 1..len(s)-1:
#      if s[i] == s[i-1]: count += 1; if count >= 7: answer YES, done.
#      else: count = 1.
# 3. If we finish the loop without reaching 7 -> answer NO.
#
# Note: we never double-count — the run resets exactly when the char
# changes, so count always equals the length of the current run.
#
# SAMPLE WALKTHROUGH
# ------------------
# s = "001001":
#   0(1) 0(2) 1(reset 1) 0(1) 0(2) 1(reset 1)  -> max run 2  -> NO ✓
#
# s = "1000000001":
#   1(1) 0(1) 0(2) 0(3) 0(4) 0(5) 0(6) 0(7) -> found -> YES ✓
#   (the run of seven 0s makes it dangerous)
#
# EDGE CASES / DETAILS
# --------------------
#   - Exactly 7 in a row       -> YES (>= 7, not just 7+).
#   - All same char "111..." (len>=7) -> YES early (break at 7).
#   - Length < 7               -> can never reach 7 -> NO.
#   - Alternating "010101..."  -> every run stays length 1    -> NO.
#
# COMPLEXITY
# ----------
#   Let n = len(s) (<= 100).
#   Time : O(n) — one pass; worst case we scan all characters.
#   Space: O(1) — a single counter integer.
#
# LESSON
# ------
#   Consecutive-character/event problems reduce to RUN LENGTH
#   TRACKING: one variable that grows on equality and resets on
#   change. It generalizes from strings to arrays (streaks of equal
#   numbers, identical signs, same direction, etc.).
#
# PYTHON NOTES
# ------------
#   - In Python you can also shortcut this exact problem in one line:
#       print("YES" if "0000000" in s or "1111111" in s else "NO")
#     The `in` operator does substring search — cute for this task,
#     but the run-counter version is the technique that scales to
#     harder problems where you also need the run's position/length.
#   - break exits the loop early (like in C++).
#   - "YES" if c else "NO" is Python's ternary expression.