# Codeforces 158A - Next Round
# https://codeforces.com/problemset/problem/158/A
# Rating: 800 (Easy) — Filtering / Counting

n, k = map(int, input().split())
scores = list(map(int, input().split()))

threshold = scores[k - 1]                       # k-th participant's score
advancers = sum(1 for s in scores if s >= threshold and s > 0)

print(advancers)

# --------------------------- FULL EXPLANATION ---------------------------
#
# PROBLEM STATEMENT
# ----------------
# A contest has n participants. Their scores are given in a list in
# NON-INCREASING order (scores[0] >= scores[1] >= ... >= scores[n-1]),
# exactly as the official results row looks.
#
# Rule: every participant whose score is STRICTLY GREATER THAN ZERO
# AND at least as large as the score of the participant ranked k-th
# advances to the next round.
#
# Task: how many participants advance?
#
# Input format:
#   Line 1: n k   (1 <= k <= n <= 50)
#   Line 2: n space-separated integers (the scores, non-increasing).
# Output format:
#   One integer — the number of advancing participants.
#
# KEY INSIGHT — THE THRESHOLD IS FIXED BY THE K-TH SCORE
# -----------------------------------------------------
# The set of advancing participants is exactly those with
#       score >= scores[k-1]   AND   score > 0
# (0-indexed, so the k-th in the input is at index k-1).
#
# Because the list is already sorted in non-increasing order, this
# is equivalent to "a prefix of the list" — but we don't even need
# to exploit that: a simple filter-and-count works and is robust to
# any ordering.
#
# ALGORITHM
# ---------
# 1. Read n, k and the scores list.
# 2. threshold = scores[k - 1].
# 3. Count elements s with s >= threshold and s > 0.
# 4. Print the count.
#
# SAMPLE WALKTHROUGH
# ------------------
# n=8 k=5, scores = 10 9 8 7 7 7 5 5
#   threshold = scores[4] = 7
#   elements >= 7 : 10, 9, 8, 7, 7, 7  -> 6 (all > 0)
#   Answer: 6 ✓
#
# n=4 k=2, scores = 0 0 0 0
#   threshold = scores[1] = 0
#   elements >= 0 could be all 4, BUT they must be > 0 as well:
#   none qualify -> Answer: 0 ✓
#
# EDGE CASES / DETAILS
# --------------------
#   - All scores zero  -> 0 advance (the strict s > 0 filter kills all).
#   - Ties at the boundary count (>=, not >): every competitor tied
#     with the k-th score advances, even past position k.
#   - k == n -> the LAST participant's score is the threshold; anyone
#     at or above it (a prefix) advances.
#   - Positive scores all the way down -> the prefix up to the last
#     score >= threshold is exactly a prefix; count by comparison.
#
# COMPLEXITY
# ----------
#   Let n = number of participants (<= 50).
#   Time : O(n) — one pass over the scores.
#   Space: O(n) — storing the score list.
#
# LESSON
# ------
#   Translate the English rule into TWO boolean conditions and count
#   with a single pass (a list comprehension + sum does it in one
#   expression). Also, always keep an eye on strict vs non-strict
#   inequalities — "greater than zero" vs "at least as large" are
#   both strict in different directions and both matter here.
#
# PYTHON NOTES
# ------------
#   - map(int, input().split()) -> reads ints; list(...) materializes
#     them into a list.
#   - sum(1 for x in xs if cond) is the idiomatic "count matching".
#   - scores[k - 1] uses 0-based indexing: input position k is index
#     k-1 in the list.