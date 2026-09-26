# Codeforces 118A - String Task
# https://codeforces.com/problemset/problem/118/A
# Rating: 800 (Easy) — String filtering / transform

VOWELS = set("aoyeui")   # a, o, y, e, u, i (case-insensitive)

s = input().strip().lower()

result = ''.join('.' + c for c in s if c not in VOWELS)
print(result)

# --------------------------- FULL EXPLANATION ---------------------------
#
# PROBLEM STATEMENT
# ----------------
# Given a string s of upper/lowercase Latin letters, transform it:
#   1. delete every VOWEL — the vowels are a, o, y, e, u, i
#      (case-insensitive; yes, 'y' counts as a vowel here);
#   2. insert a '.' before each remaining (consonant) letter;
#   3. write all remaining letters in LOWERCASE.
#
# Task: print the resulting string.
#
# Input format:
#   One line: the string s (length 1..100).
# Output format:
#   The transformed string.
#
# KEY INSIGHT — ONE PASS, TWO OPERATIONS
# --------------------------------------
# The rule is purely local: for each character,
#   - if it is a vowel -> drop it,
#   - otherwise        -> emit '.' + its lowercase form.
# So it is a "filter + map" over the characters:
#       keep c if c not in vowels;  replace c by '.' + c
#
# Implementation shortcut: s.lower() FIRST, then compare against a
# lowercase vowel set — this removes all case handling from the loop.
#
# ALGORITHM
# ---------
# 1. Read s, convert to lowercase.
# 2. For each char c:
#      if c not in {a,o,y,e,u,i}: append '.' + c.
# 3. Join and print.
#
# SAMPLE WALKTHROUGH
# ------------------
# "tour":
#   t -> ".t",  o (vowel, skipped),  u (vowel, skipped),  r -> ".r"
#   result ".t.r" ✓
#
# "Codeforces" -> lowercase "codeforces":
#   c.o.d.e.f.o.r.c.e.s
#   keep c,d,f,r,c,s  -> ".c.d.f.r.c.s" ✓
#
# "aBAcAba" -> "abacaba":
#   keep b,c,b -> ".b.c.b" ✓
#
# EDGE CASES / DETAILS
# --------------------
#   - All vowels "aEiOuY" -> empty output (print an empty line).
#   - No vowels          -> every char dotted: "bcd" -> ".b.c.d".
#   - 'Y'/'y' is treated as a vowel (easy to forget!).
#   - Mixed case input    -> handled by the .lower() normalization.
#
# COMPLEXITY
# ----------
#   Let n = length of s (<= 100).
#   Time : O(n) — one pass over the characters.
#   Space: O(n) — the output string (plus the small vowel set).
#
# LESSON
# ------
#   "Filter + map" is the go-to shape for transformations. Doing the
#   case normalization ONCE up front (s.lower()) and then comparing
#   against a plain lowercase set keeps the per-character logic tiny.
#   Prefer the set for membership — O(1) lookup and self-documenting.
#
# PYTHON NOTES
# ------------
#   - set("aoyeui") builds a membership set from a string literal.
#   - ''.join(expr for c in s ...) builds a string from a generator
#     efficiently (instead of repeated +=).
#   - c not in VOWELS is the O(1) set-membership test.