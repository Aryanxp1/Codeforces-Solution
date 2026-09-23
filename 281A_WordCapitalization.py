# Codeforces 281A - Word Capitalization
# https://codeforces.com/problemset/problem/281/A
# Rating: 800 (Easy) — String manipulation

s = input().strip()

print(s[0].upper() + s[1:])

# --------------------------- FULL EXPLANATION ---------------------------
#
# PROBLEM STATEMENT
# ----------------
# Given a word w (length 1..1000, Latin letters, mixed case allowed),
# capitalize its FIRST letter and leave the rest unchanged.
#
# Input format:
#   One line: the word.
# Output format:
#   The same word with the first letter uppercase.
#
# KEY INSIGHT — PYTHON STRINGS ARE IMMUTABLE, SO SLICE AND CONCATENATE
# -------------------------------------------------------------------
# We cannot modify an existing Python string in place. The idiomatic
# approach is to build a NEW string:
#       first_char.upper()  +  the rest of the word
# i.e.    s[0].upper()      +  s[1:]
#
# Notice we do NOT need an "if" for words that are already capitalized:
# 'A'.upper() == 'A', so upper() is idempotent on uppercase letters.
# The rest is preserved exactly (other characters are not touched).
#
# ALGORITHM
# ---------
# 1. Read w.
# 2. Print w[0].upper() + w[1:].
#
# SAMPLE WALKTHROUGH
# ------------------
# s = "konjac"  -> 'k'.upper()='K', s[1:]="onjac" -> "Konjac"  ✓
# s = "Konjac"  -> 'K'.upper()='K', s[1:]="onjac" -> "Konjac"  ✓
# s = "apPLe"   -> 'a'.upper()='A', s[1:]="pPLe"  -> "ApPLe"   ✓
#
# EDGE CASES / DETAILS
# --------------------
#   - Single letter "a"  -> s[1:] == ""  -> "A" (empty slice is fine).
#   - Already uppercased -> upper() is a no-op -> unchanged word.
#   - Non-lowercase following letters stay exactly as-is (we only
#     transform index 0).
#   - Only the FIRST character is changed — never .lower() the rest.
#
# COMPLEXITY
# ----------
#   Let n = length of the word (<= 1000).
#   Time : O(n) — upper() on one char is O(1); slicing s[1:] copies
#          the tail once.
#   Space: O(n) — the result string.
#
# LESSON
# ------
#   In Python, "modify a string" always means "build a new string".
#   The pattern <prefix> + <middle> + <suffix> with slices is the
#   universal building block for string edits (capitalize, insert,
#   delete, swap) — combine slices and str methods instead of loops.
#
# PYTHON NOTES
# ------------
#   - s[0]        -> first character.
#   - s[1:]       -> substring from index 1 to the end.
#   - str.upper() -> new uppercase string ('A'.upper()=='A').
#   - Concatenation with + is fine for these sizes.