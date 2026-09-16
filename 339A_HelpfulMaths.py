# Codeforces 339A - Helpful Maths
# https://codeforces.com/problemset/problem/339/A
# Rating: 800 (Easy) — Parsing / Sorting

s = input().strip()

nums = s.split('+')     # ["3", "2", "1"]
nums.sort()             # ["1", "2", "3"]  (strings "1","2","3" sort correctly)
print('+'.join(nums))   # "1+2+3"

# --------------------------- FULL EXPLANATION ---------------------------
#
# PROBLEM STATEMENT
# ----------------
# Xenia was given an expression like "a+b+a+..." where every term is
# one of the digits 1, 2 or 3, joined by '+'. She moved the terms
# around so the digits are IN NON-DECREASING ORDER, keeping the '+'
# separators between them.
#
# Task: given the original (unsorted) expression, output the sorted
# one.
#
# Input format:
#   One line: the expression (e.g. "3+2+1"). Length <= 100.
# Output format:
#   The same expression with terms sorted increasingly, '+' joined.
#
# KEY INSIGHT — STRINGS SORT LIKE NUMBERS HERE
# --------------------------------------------
# Because every term is a SINGLE digit 1, 2 or 3, the strings "1",
# "2", "3" compare in exactly the same order as the numbers 1, 2, 3.
# So we never need to convert to int: sort the string tokens directly.
#
# The whole job is three standard operations:
#   1. s.split('+')  -> split the line into a list of tokens.
#   2. nums.sort()   -> sort them in place (lexicographic == numeric).
#   3. '+'.join(nums)-> glue them back together with '+' separators.
#
# (If the terms could be multi-digit like "12", we WOULD need
#  int() conversion before sorting — but not for this problem.)
#
# ALGORITHM
# ---------
# 1. Read s.
# 2. tokens = s.split('+').
# 3. tokens.sort().
# 4. Print '+'.join(tokens).
#
# SAMPLE WALKTHROUGH
# ------------------
# s = "3+2+1"    -> ["3","2","1"] -> sort -> ["1","2","3"] -> "1+2+3" ✓
# s = "1+1+3+1+3"-> ["1","1","3","1","3"] -> sort
#                   -> ["1","1","1","3","3"] -> "1+1+1+3+3" ✓
# s = "2"        -> ["2"] -> "2" (single term, unchanged) ✓
#
# EDGE CASES / DETAILS
# --------------------
#   - Single term "2" -> no '+' at all; split/join handle it fine.
#   - Repeated digits -> sort keeps duplicates adjacent ("1+1+3").
#   - Already sorted   -> sort is a no-op, output equals input.
#   - The list is sorted IN PLACE (nums.sort() modifies the list,
#     returns None) — unlike sorted(nums) which returns a new list.
#
# COMPLEXITY
# ----------
#   Let k = number of terms (<= 50).
#   Time : O(k log k) — dominated by the sort.
#   Space: O(k) — the token list.
#
# LESSON
# ------
#   "Parse -> transform -> serialize" is the skeleton of countless
#   easy problems: split the input into tokens, do the work on the
#   tokens, then join/format them back. Also remember: digit strings
#   sort like their numeric values ONLY while every token has the
#   same length (single digits here) — otherwise compare as ints.
#
# PYTHON NOTES
# ------------
#   - str.split(sep) splits on the separator (default: whitespace).
#   - list.sort() sorts in place; sorted(list) returns a copy.
#   - 'sep'.join(list) produces ONE string with sep inserted between
#     elements — the inverse of split. Pairing them round-trips
#     tokenized data.
#   - Whole program: 4 lines of Python.