# Codeforces 71A - Way Too Long Words
# https://codeforces.com/problemset/problem/71/A
# Rating: 800 (Easy)

n = int(input())

for _ in range(n):
    s = input()
    length = len(s)

    if length > 10:
        print(s[0] + str(length - 2) + s[-1])
    else:
        print(s)

# --------------------------- FULL EXPLANATION ---------------------------
#
# PROBLEM STATEMENT
# ----------------
# Sometimes words are too long to be convenient, so we abbreviate them.
# Given n words, for EVERY word we apply this rule:
#   - If the word's length is strictly greater than 10
#     (i.e. length >= 11), replace it with:
#         first letter + (length - 2) + last letter
#   - Otherwise, print the word exactly as it is.
#
# Examples from the statement:
#   "word"            -> len 4  <= 10  -> "word"
#   "localization"    -> len 12 >  10  -> "l10n"   (l + 10 + n)
#   "internationalization"            -> "i18n"   (i + 18 + n)
#   "pneumonoultramicroscopicsilicovolcanoconiosis" -> "p43s"
#
# APPROACH
# --------
# This is a pure implementation / string-manipulation problem.
# 1. Read n (number of words).
# 2. For each word, read it as a string.
# 3. Compute length = len(s).
# 4. If length > 10, print:
#        s[0] + str(length - 2) + s[-1]
#    Note: s[0] is first char, s[-1] is last char (Python negative
#    indexing), and str(length - 2) converts the integer to a string
#    so it concatenates properly (in Python you can't add str + int).
# 5. Else print the whole word unchanged.
#
# WHY length - 2?
#    The original word has length letters. We keep 2 letters
#    (first + last), so exactly (length - 2) letters were "taken out"
#    of the middle — that number is what appears in the abbreviation.
#    Example: "internationalization" has 20 letters -> i 18 n, "i18n".
#
# EDGE CASES / DETAILS
# --------------------
#   - A word of length exactly 10 stays unchanged
#     ("pneumonoult..." style long words only kick in at len >= 11).
#   - Words are lowercase English letters, so position s[0] and
#     s[-1] are always safe to access (strings are never empty).
#   - Using print() adds a newline automatically.
#
# COMPLEXITY
# ----------
#   Let L = length of the longest word (<= 100).
#   Time : O(n * L)  — we read each string and do O(L) work
#          reading/printing it. The check itself is O(1) per word.
#   Space: O(L)  — only one string held in memory at a time.
#
# LESSON
# ------
#   Easy string problems are mostly about careful reading of the
#   rule ("strictly more than 10") and knowing string indexing.
#   No fancy algorithm — just convert the rule into code exactly.
#
# PYTHON NOTES
# ------------
#   - len(s) gives the string length (vs s.size() in C++).
#   - s[-1] accesses the last character (Python negative indexing).
#   - str(x) converts integer x to string for concatenation.
#   - print() handles output with automatic newline.
#   - for _ in range(n): is the Python idiom for repeating n times.