# Codeforces 61A - Ultra-Fast Mathematician
# https://codeforces.com/problemset/problem/61/A
# Rating: 800 (Easy) — Bitwise XOR / char-wise operation

a = input().strip()
b = input().strip()

result = ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))
print(result)

# --------------------------- FULL EXPLANATION ---------------------------
#
# PROBLEM STATEMENT
# ----------------
# Two binary strings are given (only characters '0' and '1'), and both
# have the SAME length (up to 100; leading zeros are allowed and must
# be preserved in the output).
#
# Build a result string of the same length where for each position i:
#   - if the two digits DIFFER -> result[i] = '1'
#   - if the two digits are the SAME -> result[i] = '0'
#
# Task: print the result string.
#
# KEY INSIGHT — THIS IS EXACTLY BITWISE XOR
# -----------------------------------------
# The rule "1 when they differ, 0 when they match" is the definition
# of the XOR operation on single bits:
#
#   x ^ y
#   -----
#   0 ^ 0 = 0      same  -> 0
#   1 ^ 1 = 0      same  -> 0
#   0 ^ 1 = 1      differ -> 1
#   1 ^ 0 = 1      differ -> 1
#
# So we convert each character to an int, apply ^, and convert back
# to a character — one XOR per position.
#
# ALGORITHM
# ---------
# 1. Read a and b.
# 2. For each index (zip walks both strings in lockstep):
#      emit str(int(a[i]) ^ int(b[i]))
# 3. Print the joined result.
#
# EXAMPLE WALKTHROUGH
# -------------------
# a = "1010", b = "1101":
#   pos0: 1 ^ 1 = 0
#   pos1: 0 ^ 1 = 1
#   pos2: 1 ^ 0 = 1
#   pos3: 0 ^ 1 = 1
#   -> "0111"
#
# a = "000", b = "110":
#   0^1, 0^1, 0^0 -> "110"
#
# EDGE CASES / DETAILS
# --------------------
#   - Leading zeros MUST be kept: "0010" stays length 4. We never
#     convert the whole string to an int, only per-character, so no
#     leading zeros are lost.
#   - Equal lengths are guaranteed, so zip() pairs every character
#     exactly (no ragged tails).
#   - All-same strings -> all '0's in the result.
#   - Length up to 100 -> tiny; no performance concerns.
#
# COMPLEXITY
# ----------
#   Let n = length of the strings (<= 100).
#   Time : O(n) — one XOR per position.
#   Space: O(n) — the result string.
#
# LESSON
# ------
#   "1 when different, 0 when same" is the signature of XOR — once
#   you see it, the solution is a one-liner instead of branching
#   if/else. XOR also shows up in parity, toggling, and problems
#   asking for the "difference" between two states.
#
# PYTHON NOTES
# ------------
#   - ^ is Python's bitwise XOR operator (applies to ints).
#   - zip(a, b) yields aligned pairs (a[i], b[i]).
#   - Purely-string alternative (no int conversion needed):
#         ''.join('1' if x != y else '0' for x, y in zip(a, b))
#     Both are equivalent for this problem; the XOR version makes the
#     mathematical idea explicit.