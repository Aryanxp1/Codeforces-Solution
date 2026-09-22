# Codeforces 116A - Tram
# https://codeforces.com/problemset/problem/116/A
# Rating: 800 (Easy) — Running maximum / Simulation

n = int(input())

on_board = 0      # passengers currently on the tram
capacity = 0      # maximum needed so far

for _ in range(n):
    a, b = map(int, input().split())
    on_board -= a  # a passengers get off
    on_board += b  # b passengers get on
    if on_board > capacity:
        capacity = on_board

print(capacity)

# --------------------------- FULL EXPLANATION ---------------------------
#
# PROBLEM STATEMENT
# ----------------
# A one-way tram line has n stops. At each stop the information
# "a b" says: a passengers get OFF the tram, then b passengers get ON.
# The tram's capacity must be big enough that nobody is ever left
# standing at a stop (i.e. passengers never exceed capacity).
#
# Task: the MINIMUM capacity that suffices = the MAXIMUM number of
# passengers on the tram at any moment.
#
# Input format:
#   Line 1: n (number of stops, 1 <= n <= 1000).
#   Next n lines: two integers a_i b_i (the off/on counts; off never
#   exceeds current passengers, totals are small).
# Output format:
#   One integer — the required minimum capacity.
#
# KEY INSIGHT — TRACK THE RUNNING TOTAL AND KEEP THE MAX
# -----------------------------------------------------
# The passenger count evolves step by step:
#       current = current - a + b      (a leave, then b board)
# The largest value current ever reaches is exactly the capacity
# the tram must have (passengers never jump over it).
# This is the classic "running maximum of a prefix-sum-style array":
#   ans = max over stops of (passengers after that stop).
#
# ALGORITHM
# ---------
# 1. capacity = 0, on_board = 0.
# 2. For each stop:
#      read a, b
#      on_board = on_board - a + b
#      capacity = max(capacity, on_board)
# 3. Print capacity.
#
# SAMPLE WALKTHROUGH
# ------------------
# Stops: (0,3) (2,5) (4,2) (4,0)
#   start       : 0        max=0
#   after stop1 : 0-0+3=3  max=3
#   after stop2 : 3-2+5=6  max=6
#   after stop3 : 6-4+2=4  max=6
#   after stop4 : 4-4+0=0  max=6
#   Answer: 6 ✓  (once 6 people are aboard, the tram needs 6 seats)
#
# EDGE CASES / DETAILS
# --------------------
#   - Single stop            -> max = b (only boardings matter).
#   - Somebody boards last   -> peak mid-line, tracked correctly.
#   - a is guaranteed <= current (valid input) so on_board never
#     goes negative.
#   - n up to 1000, values small — int is plenty.
#
# COMPLEXITY
# ----------
#   Let n = number of stops (<= 1000).
#   Time : O(n) — one pass over the stops.
#   Space: O(1) — two integers (plus a,b per iteration).
#
# LESSON
# ------
#   "What's the minimum capacity/buffer so nothing overflows?" maps
#   to "what's the maximum of the running total?" Carefully maintain
#   the current value exactly as the story describes (off THEN on),
#   update the maximum, and move on — do not try to be clever with
#   formulas; simulation is O(n) anyway.
#
# PYTHON NOTES
# ------------
#   - on_board = on_board - a + b is just that: reassignment with a
#     mixed expression; Python has no ++/-- operators.
#   - capacity = max(capacity, on_board) uses the built-in max.
#   - a, b = map(int, input().split()) unpacks the line into two ints.