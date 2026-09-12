# Codeforces 50A - Domino piling
# https://codeforces.com/problemset/problem/50/A
# Rating: 800 (Easy)

m, n = map(int, input().split())
print(m * n // 2)

# --------------------------- FULL EXPLANATION ---------------------------
#
# PROBLEM STATEMENT
# ----------------
# You are given a rectangular board of M x N squares (1 <= M, N <= 16).
# A domino covers exactly two ADJACENT squares (1x2 or 2x1).
# Dominoes cannot overlap.
#
# Question: what is the MAXIMUM number of dominoes that can be
# placed on the board?
#
# Input format:
#   One line: two integers M N.
# Output format:
#   One integer — the maximum number of dominoes.
#
# KEY INSIGHT — FLOOR DIVISION
# ----------------------------
# Each domino covers exactly 2 squares, and the board has M*N
# squares total. So we can never place more than (M*N)/2 dominoes.
#
# And this bound is ALWAYS achievable: tile the board row by row
# with horizontal dominoes. If a row has an even width, it fills
# perfectly; if odd, one square per row is left over — and those
# leftover squares pair up vertically with the row below
# (except possibly one row if M is also odd, or one column if N
# is also odd). In every case exactly the M*N mod 2 = at most ONE
# square stays empty. So the maximum is:
#
#       answer = (M * N) // 2      (integer / floor division)
#
# ALGORITHM
# ---------
# 1. Read M and N with map(int, input().split()).
# 2. Print (M * N) // 2.
#    That's it — one line of logic!
#
# SAMPLE WALKTHROUGH
# ------------------
# Example 1: M = 2, N = 4
#   2*4 = 8 squares -> 8 // 2 = 4 dominoes ✓
#   (two rows, each row fits two horizontal dominoes)
#
# Example 2: M = 3, N = 3
#   3*3 = 9 squares -> 9 // 2 = 4 dominoes ✓
#   (9 is odd, so one square must stay empty: 4 dominoes cover
#   8 squares, leaving 1 uncovered — and no arrangement beats that)
#
# EDGE CASES / DETAILS
# --------------------
#   - 1x1 board  -> 1 // 2 = 0 dominoes (nothing fits) ✓
#   - 1xN strip  -> N // 2 dominoes laid end to end ✓
#   - Even area  -> board tiles perfectly, zero waste.
#   - Odd area   -> exactly one square left empty, always.
#   - M, N <= 16 -> M*N <= 256, tiny numbers, no overflow possible.
#
# COMPLEXITY
# ----------
#   Time : O(1) — a single multiplication + division.
#   Space: O(1) — two integers.
#
# LESSON
# ------
#   Some problems look geometric (tiling! shapes!) but collapse
#   into pure arithmetic once you find the invariant: each domino
#   eats 2 squares, so the answer is bounded by area/2, and the
#   bound is always reachable. Always ask: "what is the absolute
#   upper bound, and can I achieve it?"
#
# PYTHON NOTES
# ------------
#   - // is FLOOR (integer) division: 9 // 2 = 4 (vs / which gives
#     4.5 as a float). Using // keeps the result an int directly.
#   - m, n = map(int, input().split()) reads two ints from one line.
#   - The whole solution is 2 lines — Python shines at expressing
#     pure-math answers with zero boilerplate.