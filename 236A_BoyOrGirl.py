# Codeforces 236A - Boy or Girl
# https://codeforces.com/problemset/problem/236/A
# Rating: 800 (Easy) — Sets / Counting

s = input().strip()

distinct = len(set(s))

if distinct % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

# --------------------------- FULL EXPLANATION ---------------------------
#
# PROBLEM STATEMENT
# ----------------
# Vasya wants to decide whether the owner of a username is a boy or
# a girl, using this (silly) rule:
#   - count the number of DIFFERENT characters in the username.
#   - if that count is EVEN  -> the user is a girl.
#   - if that count is ODD   -> the user is a boy.
#
# Task: given a username s (lowercase Latin letters, 1..100 chars),
# print "CHAT WITH HER!" (girl) or "IGNORE HIM!" (boy).
#
# Input format:
#   One line: the username.
# Output format:
#   One of the two exact strings above.
#
# KEY INSIGHT — A SET INSTANTLY REMOVES DUPLICATES
# ------------------------------------------------
# "Number of different characters" = the size of the set of the
# string's characters. A Python set stores only ONE copy of each
# value, so len(set(s)) is exactly the distinct-character count.
#
# No manual "have I seen this letter?" bookkeeping is needed — the
# set does the work, and it generalizes to any characters.
#
# ALGORITHM
# ---------
# 1. Read s.
# 2. distinct = len(set(s)).
# 3. If distinct is even -> print "CHAT WITH HER!", else
#    print "IGNORE HIM!".
#
# SAMPLE WALKTHROUGH
# ------------------
# s = "wjmzbmr":
#   characters: w j m z b m r
#   distinct = {w, j, m, z, b, r} = 6  -> even -> "CHAT WITH HER!" ✓
#
# s = "xiaodao":
#   characters: x i a o d a o
#   distinct = {x, i, a, o, d} = 5     -> odd  -> "IGNORE HIM!" ✓
#
# s = "sevenkplus":
#   characters: s e v e n k p l u s
#   distinct = {s, e, v, n, k, p, l, u} = 8 -> even -> "CHAT WITH HER!" ✓
#
# EDGE CASES / DETAILS
# --------------------
#   - Single repeated letter, e.g. "aaa"   -> distinct = 1 (odd) -> boy.
#   - All letters distinct, e.g. "abc"     -> distinct = 3 (odd) -> boy.
#   - 26-letter max distinct set (alphabet) -> 26 even -> girl.
#   - .strip() removes any trailing newline from input().
#
# COMPLEXITY
# ----------
#   Let n = len(s) (<= 100).
#   Time : O(n)  — building the set touches each character once.
#   Space: O(distinct) = O(26) at most — the set holds unique letters.
#
# LESSON
# ------
#   "How many DIFFERENT ...?" questions are set questions. Whenever
#   you need distinctness, reach for a set (or a hash map) instead
#   of nested loops — converting from an O(n^2) boolean matrix to
#   an O(n) set is a classic easy-win refactor.
#
# PYTHON NOTES
# ------------
#   - set(iterable) builds a set from any iterable — even a string
#     (it iterates over characters).
#   - len(set(s)) → distinct count in one expression.
#   - % 2 parity check: even -> CHAT, odd -> IGNORE.