# Codeforces 59A - Word
# https://codeforces.com/problemset/problem/59/A
# Rating: 800 (Easy) — Case counting / string transform

s = input().strip()

uppercase = sum(1 for c in s if c.isupper())
lowercase = len(s) - uppercase

# Strictly more uppercase -> upper; otherwise (incl. ties) -> lower.
print(s.upper() if uppercase > lowercase else s.lower())

# --------------------------- FULL EXPLANATION ---------------------------
#
# PROBLEM STATEMENT
# ----------------
# Vasya wants each word to be all-uppercase or all-lowercase, choosing
# the form that changes as FEW letters as possible.
#
# Rule (equivalently):
#   - If the word has STRICTLY more uppercase letters than lowercase,
#     make the WHOLE word uppercase.
#   - Otherwise (lowercase >= uppercase), make the WHOLE word
#     lowercase.
# Ties therefore go to LOWERCASE.
#
# Input format:
#   One line: word s (length 1..100), mixed-case Latin letters.
# Output format:
#   The corrected word.
#
# KEY INSIGHT — ONLY COMPARE THE TWO COUNTS
# ----------------------------------------
# We don't need to track which letters to change; converting the whole
# string is equivalent. So the entire problem reduces to:
#     count uppercase letters (U) and lowercase letters (L)
#     if U > L  -> print s.upper()
#     else      -> print s.lower()
# Note the counts are complementary (U + L = len(s)), so counting one
# count gives the other for free.
#
# ALGORITHM
# ---------
# 1. Read s.
# 2. Count uppercase letters U.
# 3. L = len(s) - U.
# 4. Print s.upper() if U > L else s.lower().
#
# SAMPLE WALKTHROUGH
# ------------------
# "HoUse": U = {H, U} = 2,  L = {o, s, e} = 3  -> 2 > 3 is FALSE
#         -> lower -> "house" ✓
# "ViP":   U = {V, P} = 2,  L = {i} = 1        -> 2 > 1 is TRUE
#         -> upper -> "VIP" ✓
# "maTRIx":U = {T, R, I} = 3, L = {m, a, x} = 4 -> 3 > 4 is FALSE
#         -> lower -> "matrix" ✓
#
# EDGE CASES / DETAILS
# --------------------
#   - Tie (e.g. "abCD"): U = 2, L = 2 -> not strictly more -> LOWER,
#     as the statement requires.
#   - Length 1: a single letter; "A" -> upper (1>0) -> "A";
#     "a" -> lower (0>1 false) -> "a" (unchanged).
#   - Already uniform word (all lower / all upper) -> stays the same.
#   - Note: this problem says NOTHING about non-letters, so a simple
#     c.isupper() test is safe (input is guaranteed to be letters only).
#
# COMPLEXITY
# ----------
#   Let n = length of s (<= 100).
#   Time : O(n) — one pass to count, one pass to convert.
#   Space: O(n) — the converted output string.
#
# LESSON
# ------
#   Many "minimize the changes to make it uniform" problems collapse
#   to a simple majority vote. Choosing the direction by comparing
#   counts (with the tie going lowercase) avoids mutating letter by
#   letter — Python's .upper()/.lower() rebuild the whole string at
#   once, which is both simpler and faster.
#
# PYTHON NOTES
# ------------
#   - str.isupper() / str.lower() / str.upper() handle ASCII letters
#     directly.
#   - sum(1 for c in s if c.isupper()) counts matching characters
#     (equivalently, sum(c.isupper() for c in s), since bool == 1).
#   - s.upper() if U > L else s.lower() is Python's inline ternary.