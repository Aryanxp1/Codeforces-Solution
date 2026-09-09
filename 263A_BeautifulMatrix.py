# Codeforces 263A - Beautiful Matrix
# https://codeforces.com/problemset/problem/263/A
# Rating: 800 (Easy)

row = 0
col = 0

for i in range(1, 6):
    values = list(map(int, input().split()))
    for j in range(1, 6):
        if values[j - 1] == 1:
            row = i
            col = j

moves = abs(row - 3) + abs(col - 3)
print(moves)

# --------------------------- FULL EXPLANATION ---------------------------
#
# PROBLEM STATEMENT
# ----------------
# We have a 5x5 matrix containing exactly 24 zeroes and a single 1.
# In ONE move, we can swap two ADJACENT rows or two ADJACENT columns
# (row i with row i+1, or column j with column j+1).
#
# The matrix is called "beautiful" if the 1 is exactly in the
# middle of the matrix — row 3, column 3 (1-indexed).
#
# Task: output the MINIMUM number of moves needed to make the
# matrix beautiful.
#
# Input format:
#   5 lines, each with 5 integers (each 0 or 1, exactly one 1 total).
# Output format:
#   One integer — the minimum number of moves.
#
# KEY INSIGHT — MANHATTAN DISTANCE
# --------------------------------
# Swapping adjacent rows moves the 1 up/down by exactly one row.
# Swapping adjacent columns moves the 1 left/right by exactly one column.
#
# So each move changes the 1's position by ONE step in one of the
# four directions — like walking on a grid.
#
# Therefore the minimum number of moves is exactly the MANHATTAN
# distance from the 1's cell (row, col) to the center (3, 3):
#
#       answer = |row - 3| + |col - 3|
#
# Why is this both achievable AND optimal?
#   Achievable: move the 1 vertically to row 3 (|row - 3| swaps),
#   then horizontally to column 3 (|col - 3| swaps). Every swap is
#   a legal adjacent-row/adjacent-column swap.
#   Optimal: each move changes |row - 3| + |col - 3| by at most 1
#   (a single swap shifts the 1 one step in one axis), so we can
#   never do better than this distance.
#
# ALGORITHM
# ---------
# 1. Scan the 5x5 grid with nested loops (i = rows, j = columns,
#    both 1-indexed so they line up with the problem's coordinates).
# 2. Remember the cell (row, col) where the value equals 1.
# 3. Print abs(row - 3) + abs(col - 3).
#
# SAMPLE WALKTHROUGH
# ------------------
# Statement example:
#   0 0 0 0 0
#   0 0 0 0 1
#   0 0 0 0 0
#   0 0 0 0 0
#   0 0 0 0 0
# The 1 is at (row 2, col 5).
#   |2 - 3| + |5 - 3| = 1 + 2 = 3.
# Check by hand: swap columns (4,5) -> 1 at (2,4); swap columns
# (3,4) -> 1 at (2,3); swap rows (2,3) -> 1 at (3,3). Total 3 ✓
#
# Another example: 1 already at center (3,3) -> answer 0.
#
# EDGE CASES / DETAILS
# --------------------
#   - 1 at the exact center      -> 0 moves (|0| + |0|).
#   - 1 at a corner (1,1)        -> |1-3| + |1-3| = 4 moves (max).
#   - There is ALWAYS exactly one 1, so row/col are always set.
#   - No matrix storage needed — we read values on the fly and only
#     keep two integers, which keeps memory constant.
#
# COMPLEXITY
# ----------
#   Time : O(25) = O(1) — the grid is a fixed 5x5, so scanning it
#          is constant work regardless of any input variation.
#   Space: O(1) — we never store the full matrix; only row & col ints.
#
# LESSON
# ------
#   Many grid problems reduce to MANHATTAN DISTANCE: |x1 - x2| +
#   |y1 - y2|. Whenever each move shifts something exactly one cell
#   along one axis, the answer is the Manhattan distance between
#   start and target. Also note the "read and process on the fly"
#   pattern — storing input you don't need again wastes memory.
#
# PYTHON NOTES
# ------------
#   - range(1, 6) gives 1, 2, 3, 4, 5 (the end is exclusive).
#   - list(map(int, input().split())) reads a line of space-separated
#     integers and converts them to a list of ints.
#   - abs() is Python's built-in absolute value function.
#   - Python uses 0-based indexing, so values[j-1] accesses the j-th
#     element when j starts at 1.