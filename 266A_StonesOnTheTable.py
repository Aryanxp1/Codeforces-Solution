# Codeforces 266A - Stones on the Table
# https://codeforces.com/problemset/problem/266/A
# Rating: 800 (Easy) — Adjacent comparisons / Counting

n = int(input())
s = input().strip()

ans = sum(1 for i in range(1, n) if s[i] == s[i - 1])
print(ans)

# --------------------------- FULL EXPLANATION ---------------------------
#
# PROBLEM STATEMENT
# ----------------
# n stones lie in a row; each stone is colored R, G or B. Rules of the
# game "Stones on the Table" require that NO two adjacent stones have
# the SAME color. To fix a given row we may REMOVE stones (keeping the
# remaining stones in their original order).
#
# Task: the MINIMUM number of stones that must be removed.
#
# Input format:
#   Line 1: n (1 <= n <= 50).
#   Line 2: the string s of length n over {R, G, B}.
# Output format:
#   One integer — the minimum removals.
#
# KEY INSIGHT — COUNT BAD ADJACENT PAIRS
# --------------------------------------
# Consider every pair of NEIGHBORING stones (s[i], s[i+1]).
#   - If they are different, nothing needs to be done about that pair.
#   - If they are the SAME, one of the two must go.
#
# Greedy argument: scanning left to right, whenever s[i] == s[i-1],
# remove s[i] (the current one). Removing the LEFT stone instead
# would be equally fine for this pair, but might create a NEW bad
# pair with the previous stone — so it is never better. Hence each
# pair that is currently equal forces exactly ONE removal, and
# removals for different pairs never conflict.
#
# Therefore:  answer = number of i with s[i] == s[i-1].
#
# ALGORITHM
# ---------
# 1. Read n and s.
# 2. For each i in 1..n-1:
#      if s[i] == s[i-1]: answer += 1.
# 3. Print answer.
#
# SAMPLE WALKTHROUGH
# ------------------
# n=3, s = "RRG":
#   i=1: 'R' == 'R' -> bad -> +1
#   i=2: 'G' != 'R' -> ok
#   Answer: 1 ✓  (remove one R; "RG" remains)
#
# n=5, s = "RRRRR":
#   every neighbor pair equal -> 4 distinct adjacent pairs -> 4.
#   Keep a single R and remove the other 4 -> "R" ✓
#
# n=4, s = "BRBG":
#   B-R, R-B, B-G all different -> 0 ✓ (already valid)
#
# EDGE CASES / DETAILS
# --------------------
#   - n = 1          -> loop body never runs -> 0 (a lone stone is fine).
#   - All same color -> answer = n - 1 (keep exactly one stone).
#   - Already valid  -> 0.
#   - We COUNT pairs, not stones: each equal pair contributes 1.
#
# COMPLEXITY
# ----------
#   Let n = number of stones (<= 50).
#   Time : O(n) — one single pass comparing neighbours.
#   Space: O(1) extra — just the running answer counter.
#
# LESSON
# ------
#   "Fix adjacent conflicts with min removals" reduces to counting
#   the pairs that are ALREADY in conflict — a greedy argument shows
#   each such pair costs exactly one removal and they don't interfere.
#   When a condition is about neighbours, the first instinct should
#   be a linear scan of adjacent pairs, not nested loops.
#
# PYTHON NOTES
# ------------
#   - Range starts at 1 so s[i-1] is always valid.
#   - sum(1 for ... if cond) counts matches in one expression.
#   - n is technically not even needed for the loop (len(s) would do),
#     but reading it keeps the solution faithful to the input format.