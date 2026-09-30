# Codeforces 228A - Is your horseshoe on the other hoof?
# https://codeforces.com/problemset/problem/228/A
# Rating: 800 (Easy) — Sets / counting distinct

colors = list(map(int, input().split()))

distinct = len(set(colors))          # how many DIFFERENT colors he owns
print(4 - distinct)                  # shortfall to reach 4 unique colors

# --------------------------- FULL EXPLANATION ---------------------------
#
# PROBLEM STATEMENT
# ----------------
# Valera has exactly four horseshoes, given as four colors s1 s2 s3 s4.
# He wants to wear four horseshoes of DIFFERENT colors. He can buy any
# number of additional horseshoes (in any colors) from the store.
# Find the MINIMUM number of horseshoes he must buy so that he can end
# up with four horseshoes of four distinct colors.
#
# Input format:
#   One line: four space-separated integers (1 <= si <= 10^9).
# Output format:
#   A single integer — the minimum number to buy.
#
# KEY INSIGHT — DISTINCT COUNT IS ALL THAT MATTERS
# ------------------------------------------------
# Start with the four horseshoes he already owns. Let d be the number
# of DISTINCT colors among them. He can keep one horseshoe of each
# distinct color (that's d colors already usable), but to reach four
# distinct colors he is missing exactly
#       (4 - d)
# colors — and the store sells every color, so he buys exactly one
# horseshoe for each missing color. Buying is one-per-missing-color
# because a color he lacks is not represented at all yet.
#
# So the answer is simply 4 minus the number of distinct colors.
#
# ALGORITHM
# ---------
# 1. Read the four colors.
# 2. Count distinct colors d = size of the set.
# 3. Print 4 - d.
#
# SAMPLE WALKTHROUGH
# ------------------
# Colors 1 7 3 3:
#   set = {1, 7, 3} -> d = 3 -> 4 - 3 = 1  ✓
#   (he owns colors 1,7,3; buy one more, e.g. color 5)
#
# Colors 7 7 7 7:
#   set = {7} -> d = 1 -> 4 - 1 = 3  ✓
#   (keeps one '7', buys three different new colors)
#
# EDGE CASES / DETAILS
# --------------------
#   - All four different (e.g. 1 2 3 4): d = 4 -> answer 0 (buy none).
#   - Three equal, one different (a a a b): d = 2 -> answer 2.
#   - Two pairs (a a b b): d = 2 -> answer 2.
#   - One pair (a a b c):  d = 3 -> answer 1.
#   - Colors reach 10^9, but Python ints are unbounded, and sets hash
#     them fine — no overflow concerns.
#
# COMPLEXITY
# ----------
#   Fixed 4 elements, so effectively O(1) time and O(1) space
#   (building a set of at most 4 items).
#
# LESSON
# ------
#   "How many must be added so all are distinct?" reduces to
#   target_size - distinct_count, when additions can be any fresh
#   value. The set is the canonical tool for "how many different
#   values are there?".
#
# PYTHON NOTES
# ------------
#   - set(colors) removes duplicates; len(...) gives the distinct count.
#   - input().split() -> list of 4 strings; map(int, ...) converts them.
#   - Answer is always between 0 and 3 here.