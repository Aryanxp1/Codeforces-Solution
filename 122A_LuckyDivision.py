# Codeforces 122A - Lucky Division
# https://codeforces.com/problemset/problem/122/A
# Rating: 1000 (Easy) — Brute force / number theory

# All "lucky numbers" (digits only 4 and 7) that are <= 1000:
LUCKY = [4, 7, 44, 47, 74, 77,
         444, 447, 474, 477, 744, 747, 774, 777]

n = int(input())

almost_lucky = any(n % lucky == 0 for lucky in LUCKY)
print("YES" if almost_lucky else "NO")

# --------------------------- FULL EXPLANATION ---------------------------
#
# PROBLEM STATEMENT
# ----------------
# A "lucky number" is a positive integer whose decimal representation
# uses ONLY the digits 4 and 7 (e.g. 4, 7, 44, 47, 74, 77, ...).
#
# A number n is "almost lucky" if it is evenly divisible by SOME lucky
# number (n % lucky == 0). Since every number divides itself, every
# lucky number is automatically almost lucky.
#
# Task: given n (1 <= n <= 1000), print "YES" if n is almost lucky,
# otherwise "NO".
#
# KEY INSIGHT — only check the lucky numbers up to n
# --------------------------------------------------
# n <= 1000, so the only lucky numbers that can divide n are those not
# exceeding n. Enumerating ALL lucky numbers <= 1000 is tiny:
#
#   1-digit: 4 7                              (2)
#   2-digit: 44 47 74 77                      (4)
#   3-digit: 444 447 474 477 744 747 774 777  (8)
#
# That's just 14 numbers. Testing n against each is trivial, so we can
# brute-force: if ANY of them divides n, the answer is "YES".
#
# (A divisor larger than n can never divide n, so the fixed list is
# complete for the given constraints.)
#
# ALGORITHM
# ---------
# 1. Read n.
# 2. For each lucky number L in the fixed list, test n % L == 0.
# 3. Print "YES" if at least one test succeeds, else "NO".
#
# SAMPLE WALKTHROUGH
# ------------------
# n = 47: 47 % 47 == 0 -> "YES" ✓ (it is itself lucky)
# n = 16: 16 % 4 == 0  -> "YES" ✓ (16 = 4 * 4)
# n = 78: 78 % 4 != 0, % 7 != 0, % 44 != 0, ..., none -> "NO" ✓
#
# EDGE CASES / DETAILS
# --------------------
#   - n itself lucky (4, 7, 44, ...) -> divisible by itself -> YES.
#   - n = 1 -> 1 % 4 != 0, none divide 1 -> NO.
#   - Small multiples of 4 or 7 (8, 12, 14, 16, ...) -> YES via 4 or 7.
#   - We include ALL lucky numbers up to 1000, so nothing is missed.
#   - "Evenly divided" means integer divisibility (remainder 0).
#
# COMPLEXITY
# ----------
#   Time : O(14) = O(1) — a fixed list of 14 lucky numbers.
#   Space: O(1) — the constant list.
#
# LESSON
# ------
#   When the input range is tiny, HARD-CODING the complete set of
#   special values turns a number-theory task into a simple loop.
#   "Divisible by some special value" -> generate/collect all special
#   values up to the bound and test divisibility one by one.
#
# PYTHON NOTES
# ------------
#   - any(gen) short-circuits: stops at the first divisor found.
#   - The list is written across two lines for readability; Python
#     brackets let a list literal span multiple lines.
#   - Alternatively you could generate: [i for i in range(1,1001) if
#     set(str(i)) <= {'4','7'}] — but the explicit list is clearer.