# Codeforces 110A - Nearly Lucky Number
# https://codeforces.com/problemset/problem/110/A
# Rating: 800 (Easy) — Digit counting

s = input().strip()

lucky_digits = sum(1 for c in s if c in '47')

# A number is "lucky" if it consists ONLY of digits 4 and 7.
is_lucky_count = all(c in '47' for c in str(lucky_digits))

print("YES" if is_lucky_count else "NO")

# --------------------------- FULL EXPLANATION ---------------------------
#
# PROBLEM STATEMENT
# ----------------
# Petya calls a number a LUCKY NUMBER if it consists only of digits
# 4 and 7 (e.g. 4, 7, 47, 7444).
# A number is called NEARLY LUCKY if the NUMBER OF lucky digits it
# contains (i.e. how many of its digits are 4 or 7) is ITSELF a lucky
# number.
#
# Task: print "YES" if the given number is nearly lucky, else "NO".
#
# Input format:
#   One line: a positive integer n (1 <= n < 10^18, so at most 18-19
#   digits).
# Output format:
#   "YES" or "NO".
#
# KEY INSIGHT — TWO-LEVEL CHECK
# -----------------------------
# Level 1: count the lucky digits in the input string: lucky_digits =
#   number of characters that are '4' or '7'.
# Level 2: check whether lucky_digits is itself a lucky number,
#   i.e. whether str(lucky_digits) contains only '4' and '7'.
#
# For the given bounds lucky_digits <= 19, so the only possible lucky
# counts are 4 and 7 — but writing the check as a string test
# (str(lucky_digits) uses only 4/7) is both simpler and correct for
# any input size, with no hard-coded constants.
#
# ALGORITHM
# ---------
# 1. Read the number as a string s.
# 2. lucky_digits = count of chars in s that are in "47".
# 3. is_lucky_count = every char of str(lucky_digits) in "47".
# 4. Print "YES" / "NO".
#
# Treating the input as a STRING (not an int) makes "count the 4s and
# 7s among the digits" trivial — exactly why we never convert to int.
#
# SAMPLE WALKTHROUGH
# ------------------
# s = "40047":
#   lucky digits: '4','0','0','4','7' -> three ('4','4','7') -> count=3
#   str(3) = "3" -> contains '3' -> not lucky -> "NO" ✓
#
# s = "7747774":
#   every digit is 4 or 7 -> count = 7
#   str(7) = "7" -> only '7' -> lucky -> "YES" ✓
#
# s = "1000000000000000":
#   no 4s or 7s -> count = 0; str(0)="0" -> not lucky -> "NO" ✓
#
# EDGE CASES / DETAILS
# --------------------
#   - count = 0   -> "0" contains '0' -> NO.
#   - count = 4   -> "4" only '4'     -> YES.
#   - count = 7   -> "7" only '7'     -> YES.
#   - count = 9..19 -> contains other digits -> NO.
#   - For larger hypothetical inputs (e.g. count=47) the string test
#     stays correct automatically — no magic numbers.
#   - Input read as string: leading zeros are technically preserved,
#     which matches the problem (n is a positive integer without
#     leading zeros anyway).
#
# COMPLEXITY
# ----------
#   Let m = number of digits (<= 19).
#   Time : O(m) — one pass to count + a tiny check on the count.
#   Space: O(1) extra — only the integer counter.
#
# LESSON
# ------
#   "Count of X" followed by "is that count special" is a two-step
#   check. Write the special-check GENERALLY (string of the count
#   consists of lucky digits) instead of enumerating possibilities
#   by hand — it costs the same, reads better, and never goes stale.
#   Also: read digit-centric input as a string, not an int.
#
# PYTHON NOTES
# ------------
#   - '4' in "47" is a substring test; c in '47' tests membership of a
#     single char — handy for "is this digit allowed".
#   - all(cond for x in xs) returns True iff every element satisfies
#     cond; all([]) is True (empty case never bites here).
#   - sum(1 for c in s if c in '47') is the count-matching idiom
#     again (see 158A).