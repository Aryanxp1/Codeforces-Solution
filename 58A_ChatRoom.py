# Codeforces 58A - Chat Room
# https://codeforces.com/problemset/problem/58/A
# Rating: 1000 (Easy-Medium)

s = input().strip()
target = "hello"

i = 0  # pointer into target: how many chars of "hello" we've matched

for ch in s:
    if i < len(target) and ch == target[i]:
        i += 1
    if i == len(target):
        break

print("YES" if i == len(target) else "NO")

# --------------------------- FULL EXPLANATION ---------------------------
#
# PROBLEM STATEMENT
# ----------------
# Vasya wants to say "hello" to a girl. He types a string s
# (lowercase Latin letters, length <= 100). Some letters may be
# typed in the wrong order, so he can DELETE any characters from s
# and keep the rest in their original order.
#
# Question: can "hello" be obtained from s this way?
#   YES -> print "YES"
#   No  -> print "NO"
#
# Input format:
#   One line: the string s.
# Output format:
#   "YES" or "NO".
#
# KEY INSIGHT — SUBSEQUENCE CHECKING (GREEDY TWO-POINTERS)
# --------------------------------------------------------
# "hello" must appear as a SUBSEQUENCE of s: not necessarily
# contiguous, but in order. Deleting characters == taking a
# subsequence.
#
# Check it greedily with two pointers:
#   - i points at the NEXT character of "hello" we still need.
#   - Walk through s once; every time the current char equals
#     target[i], we've matched one more letter, so i += 1.
#   - If i reaches 5 (len("hello")), all letters matched -> YES.
#
# WHY GREEDY WORKS
# ----------------
# Matching the earliest possible occurrence of the next needed
# letter is never worse than matching a later one: any solution
# that used a later position for target[i] could be switched to
# the earlier one and still leave everything after it available.
# So one left-to-right pass finds a match if one exists.
#
# ALGORITHM
# ---------
# 1. Read s, set target = "hello", i = 0.
# 2. For each character ch in s:
#      if ch == target[i] (and we still need letters): i += 1
#      if i == len(target): break (already matched everything)
# 3. Print YES if i == len(target), else NO.
#
# SAMPLE WALKTHROUGH
# ------------------
# Example 1: s = "ahhellllloou"
#   h(->h)  e(->e)  l(->l)  l(skip, need l? yes! -> l) ...
#   step by step: 'a' no, 'h' -> i=1, 'h' no (need e),
#   'e' -> i=2, 'l' -> i=3, 'l' -> i=4, 'l' -> i=5 = "hello" done.
#   -> YES ✓
#
# Example 2: s = "hlelo"
#   'h' -> i=1, 'l' no, 'e' -> i=2, 'l' -> i=3, 'o' no.
#   i = 3 != 5 -> NO ✓  (the two l's of "hello" can't both be found
#   after 'e' — s has only one 'l' after its 'e')
#
# EDGE CASES / DETAILS
# --------------------
#   - s shorter than 5 chars -> can never hold "hello" -> NO.
#     (the loop simply ends with i < 5)
#   - Extra letters between matches are simply skipped.
#   - Letters of "hello" that repeat: 'l' appears twice, and the
#     two-pointer handles repeats naturally (each match advances i,
#     so the second 'l' must come strictly after the first).
#   - i < len(target) guard prevents index-out-of-range after a
#     full match; the break also stops early once done.
#
# COMPLEXITY
# ----------
#   Let n = len(s) (<= 100).
#   Time : O(n) — single pass over s; each char advances i at most
#          once, and i can grow at most 5 times total.
#   Space: O(1) — just the pointer i and the constant "hello".
#
# LESSON
# ------
#   "Can string T be found as a subsequence of string S?" is a
#   hugely common pattern, and the two-pointer greedy scan is THE
#   standard solution: walk S once, advance a pointer into T on
#   each match. You will reuse this exact idea in many problems
#   (e.g., checking sequences, merging, matching).
#
# PYTHON NOTES
# ------------
#   - for ch in s: iterates over characters directly — no index
#     loop needed like in C++.
#   - "YES" if cond else "NO" is Python's ternary (inline if/else).
#   - .strip() removes accidental trailing spaces/newlines from input.
#   - len(target) is used instead of hard-coding 5 — cleaner and
#     generalizes to any target string.
