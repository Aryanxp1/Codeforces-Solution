# Codeforces 133A - HQ9+
# https://codeforces.com/problemset/problem/133/A
# Rating: 800 (Easy) — Simple search / set membership

s = input()

# Output-producing instructions: 'H', 'Q', '9'.
# '+' only bumps the accumulator and prints nothing.
produces_output = any(c in "HQ9" for c in s)

print("YES" if produces_output else "NO")

# --------------------------- FULL EXPLANATION ---------------------------
#
# PROBLEM STATEMENT
# ----------------
# HQ9+ is a joke language with four one-character instructions:
#   'H' -> prints "Hello, World!"
#   'Q' -> prints the program's own source code
#   '9' -> prints the "99 Bottles of Beer" lyrics
#   '+' -> increments an internal accumulator (prints NOTHING)
# Instructions are CASE-SENSITIVE: only uppercase 'H' and 'Q' count.
# Every other character is simply ignored.
#
# Task: decide whether running the given program produces ANY output.
# Print "YES" or "NO".
#
# Input format:
#   One line p (1..100 chars; printable ASCII 33..126, so no spaces).
# Output format:
#   "YES" if the program outputs something, else "NO".
#
# KEY INSIGHT — '+' IS A TRAP
# ---------------------------
# Only H, Q and 9 print. '+' does produce a side effect (the
# accumulator), but it is NOT output — so a program made of only '+'
# must answer "NO".
#
# Therefore: the program prints something iff the string contains at
# least one of the characters 'H', 'Q', '9'. That's it — no need to
# simulate anything.
#
# ALGORITHM
# ---------
# 1. Read the program string s.
# 2. Check if ANY character of s is in the set {'H','Q','9'}.
# 3. Print "YES" or "NO" accordingly.
#
# SAMPLE WALKTHROUGH
# ------------------
# p = "Hi!"       -> contains 'H' -> "YES" ✓
# p = "Codeforces"-> C,o,d,e,f,r,c,e,s — none of H/Q/9 -> "NO" ✓
# p = "+++"       -> only accumulator increments -> "NO"
# p = "+Q"        -> contains 'Q' -> "YES"
# p = "hq9"       -> lowercase: 'h','q' are NOT instructions; '9' IS
#                    (digits have no case) -> "YES"
#
# EDGE CASES / DETAILS
# --------------------
#   - '+' alone or repeated -> NO (no printing instruction).
#   - Lowercase 'h'/'q'     -> NOT instructions -> don't count.
#   - The digit '9' counts  -> any '9' anywhere makes it YES.
#   - Other printable chars (e.g. '!', 'x') are ignored.
#
# COMPLEXITY
# ----------
#   Let n = length of the program (<= 100).
#   Time : O(n) — a single scan through the characters.
#   Space: O(1) extra — just the constant instruction set.
#
# LESSON
# ------
#   Distinguish "has an effect" from "produces output": side effects
#   without printing don't count here. Checking membership against a
#   small set of interesting characters (any(c in SET for c in s)) is
#   the standard one-liner for "does the string contain any of these".
#
# PYTHON NOTES
# ------------
#   - any(gen) short-circuits at the first True — stops scanning early.
#   - c in "HQ9" is a substring/membership test for a single char.
#   - We read with plain input() (no .strip() needed; the chars are
#     printable ASCII with no spaces per the constraints).