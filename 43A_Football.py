# Codeforces 43A - Football
# https://codeforces.com/problemset/problem/43/A
# Rating: 800 (Easy) — Frequency counting

from collections import Counter

n = int(input())
goals = Counter(input().strip() for _ in range(n))

print(goals.most_common(1)[0][0])

# --------------------------- FULL EXPLANATION ---------------------------
#
# PROBLEM STATEMENT
# ----------------
# Vasya wants to know who won a football final. He does NOT have the
# total score, but he has a line-by-line description of the match:
# n lines, each line naming the team that scored that goal.
#
# Task: print the name of the WINNING team (the team with more goals).
#
# Guarantees from the statement:
#   - The match does NOT end in a draw (one team scored strictly more).
#   - At most TWO distinct team names appear in the description.
#   - Names are uppercase Latin letters, length <= 10, n <= 100.
#
# Input format:
#   Line 1: n (number of goals).
#   Next n lines: one team name per goal.
# Output format:
#   The name of the team that scored more goals.
#
# KEY INSIGHT — JUST COUNT AND PICK THE LARGEST
# --------------------------------------------
# Each line is one goal, so the number of times a name appears IS that
# team's goal count. With no draw and at most two teams, the winner is
# simply the name with the higher count — no tie-breaking logic needed.
#
# Using Counter gives us the frequency map directly, and
# most_common(1)[0] returns the (name, count) pair with the highest
# count, so the name at [0] is the winner.
#
# ALGORITHM
# ---------
# 1. Read n.
# 2. Build a Counter over the n team names.
# 3. Print the most frequent name.
#
# SAMPLE WALKTHROUGH
# ------------------
# Goals: Red, Blue, Red
#   Counter = {"Red": 2, "Blue": 1}
#   most_common(1)[0] = ("Red", 2)  -> print "Red" ✓
#
# (Another typical case: goals Blue x5, Red x4 -> "Blue" wins 5:4.)
#
# EDGE CASES / DETAILS
# --------------------
#   - Only ONE team scored (n goals all same) -> that team is the
#     winner; Counter has a single entry -> works.
#   - The weaker team appears first -> order doesn't matter, counts do.
#   - No draw is guaranteed, so we never have to handle equality.
#   - Only ONE of the two teams is printed — not both counts.
#
# COMPLEXITY
# ----------
#   Let n = number of goals (<= 100).
#   Time : O(n) — building the Counter counts each line once;
#          most_common(1) on a tiny map is O(k) (k <= 2 teams).
#   Space: O(k) — the two-entry frequency map.
#
# LESSON
# ------
#   "Who/what appears most often?" is a frequency-counting problem.
#   collections.Counter is the go-to tool: feed it an iterable and
#   you get a dict-like object with counts plus handy methods
#   (most_common, elements, total). Prefer it over hand-rolling a
#   dict loop.
#
# PYTHON NOTES
# ------------
#   - Counter(iterable) returns a mapping of value -> count.
#   - most_common(1) -> a list of the top (value, count) pairs;
#     [0][0] is the winning team name.
#   - input().strip() removes the trailing newline from each line.