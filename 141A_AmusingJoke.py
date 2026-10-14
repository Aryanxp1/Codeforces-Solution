# Codeforces 141A - Amusing Joke
# https://codeforces.com/problemset/problem/141/A
# Rating: 800 (Easy) — Anagram / frequency equality

from collections import Counter

guest = input().strip()
host = input().strip()
pile = input().strip()

# The pile must be EXACTLY the letters of guest+host (same multiset).
print("YES" if Counter(pile) == Counter(guest + host) else "NO")

# --------------------------- FULL EXPLANATION ---------------------------
#
# PROBLEM STATEMENT
# ----------------
# Two strings were hung on the door: the GUEST's name and the HOST's
# name (each on its own line). Overnight someone stole all those
# letters and dumped them into a pile at the door (third line).
#
# Task: decide whether the pile can be rearranged to exactly spell out
# BOTH names (guest's name + host's name) — using every letter in the
# pile exactly once, with nothing left over and no new letters needed.
#
# Input format (3 lines, uppercase Latin, each 1..100 chars):
#   line 1: guest name
#   line 2: host name
#   line 3: the pile of letters
# Output format:
#   "YES" if the pile is exactly a rearrangement of guest+host, else "NO".
#
# KEY INSIGHT — "CAN BE REARRANGED INTO" MEANS ANAGRAM / EQUAL MULTISET
# ---------------------------------------------------------------------
# "Exactly usable, no more and no less" means the pile and the
# concatenation (guest + host) must contain the SAME letters with the
# SAME multiplicities. Order is irrelevant; counts are everything.
#
# So:  YES  <=>  Counter(pile) == Counter(guest + host)
#
# Counter equality compares BOTH keys and counts, which automatically
# enforces the two failure modes from the statement's notes:
#   - a letter is missing   -> that count is lower -> not equal;
#   - a letter is extra     -> that count is higher (or a new key)
#                              -> not equal.
# It also catches total-length mismatches (shorter/longer pile) without
# needing a separate length check.
#
# ALGORITHM
# ---------
# 1. Read guest, host, pile.
# 2. Compare Counter(pile) with Counter(guest + host).
# 3. Print "YES" if equal, else "NO".
#
# EXAMPLE WALKTHROUGH
# -------------------
# guest = "Petya", host = "Vasya", pile = "PetyaVasya"
#   guest + host = "PetyaVasya"
#   Counter(pile) == Counter("PetyaVasya") -> same counts -> "YES"
#   (order differs, but that's allowed — we only rearrange.)
#
# pile = "..., missing a P, extra a L"
#   counts for 'P' differ and 'L' appears unexpectedly -> "NO".
#
# pile shorter than both names:
#   some letter's count is too low -> not equal -> "NO".
#
# ALTERNATIVE
# -----------
# Sorting works too: sorted(pile) == sorted(guest + host). Both are
# O(L log L); Counter is O(L) and reads as "same letter frequencies".
#
# EDGE CASES / DETAILS
# --------------------
#   - Lengths differ at all -> answer NO (Counter equality detects it).
#   - Duplicated letters in names (e.g. "aa" vs "a" vs "aaa") -> handled
#     exactly by counts, not just presence.
#   - Guest and host may contain the same letters; we concatenate first
#     so all letters are pooled together.
#   - Input is uppercase only, so no case normalization is needed.
#
# COMPLEXITY
# ----------
#   Let L = len(pile) (<= 100).
#   Time : O(L) to build both Counters and compare them.
#   Space: O(distinct letters) <= O(26) — tiny.
#
# LESSON
# ------
#   "Can it be rearranged to form ...?" is the anagram test, and the
#   cleanest anagram test is comparing letter FREQUENCIES (Counter),
#   not comparing sorted strings by eye. Remember to concatenate the
#   two source strings FIRST so you compare against the whole target.
#
# PYTHON NOTES
# ------------
#   - guest + host concatenates the two strings in Python (+ on str).
#   - Counter equality is structural: equal keys AND equal counts.
#   - Alternative one-liner: print("YES" if sorted(pile) ==
#     sorted(guest + host) else "NO").