# Codeforces 2255A - Hot Potatoes at the Fairy Warehouse
# https://codeforces.com/problemset/problem/2255/A
# Rating: Div 1 A (Game Theory / Greedy)

import sys


def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    pos = 1
    out = []

    for _ in range(t):
        n = int(data[pos])
        k = int(data[pos + 1])          
        pos += 2
        s = data[pos]
        pos += 1

        m = 2 * n                      
        red = 0

        for i in range(m):
            if s[i] != '1':
                continue
            nxt = s[(i + 1) % m]        
            if nxt == '0':
               
                if i % 2 == 0:         
                    red += 1
            else:
                
                if i % 2 == 1:         
                    red += 1

        total = s.count('1')
        out.append(f"{red} {total - red}")

    sys.stdout.write("\n".join(out))


main()

# --------------------------- FULL EXPLANATION ---------------------------
#
# PROBLEM STATEMENT
# ----------------
# 2n leprechauns sit on a circle, numbered 1..2n clockwise.
#   Odd numbers  -> Red Team
#   Even numbers -> Blue Team
# Some of them initially hold potatoes (string s, s_i = 1 means a potato).
# The game lasts k rounds. Each round, every potato holder simultaneously
# either KEEPS the potato or passes it clockwise to the next leprechaun —
# but ONLY if that next leprechaun did not hold a potato at the START of
# the round (so no two potatoes ever collide).
#
# After k rounds, everyone still holding a potato is eliminated. A team's
# score = the number of eliminated leprechauns of the OTHER team.
# Both teams cooperate internally and play optimally.
#
# Task: print the scores of the Red and Blue teams.
#
# KEY OBSERVATIONS
# ----------------
# 1) The game is ZERO-SUM with total = number of potatoes.
#    - Red score  = (# potatoes that end on EVEN positions)  [blue eliminated]
#    - Blue score = (# potatoes that end on ODD  positions)  [red eliminated]
#    Every potato ends somewhere, so Red + Blue = P (potato count) always.
#
# 2) Structure of a MAXIMAL RUN of consecutive potatoes.
#    Look at a maximal block "...1 1 1 0..." — inside the block, every
#    holder is blocked (its clockwise neighbour is occupied), EXCEPT the
#    LAST one which has an empty cell in front.
#
# 3) Moving EARLY is a mistake.
#    If the last potato moves before the final round, it lands on the
#    opponent's side AND leaves an empty cell behind, which unblocks the
#    potato behind it. Both of those newly-empowered players belong to the
#    OPPONENT, who can then use their next turn to cancel the point.
#    -> The strictly optimal play is: WAIT, and only the last potato of
#       each run moves — exactly ONE step — in the very LAST round.
#
# 4) Therefore k is IRRELEVANT (as long as k >= 1).
#    The final round is the only round that matters. (Editorial confirms:
#    "the exact value of k is irrelevant".)
#
# FINAL RULE (per potato, scanning the circle)
# ------------------------------------------
# For every cell i with s[i] == '1', look at the cell in front (i+1, cyclic):
#   * if s[i+1] == '0'  -> the potato CAN move in the final round.
#     Moving it transfers the potato to the opponent's side, so the team
#     that OWNS cell i scores the point.
#   * if s[i+1] == '1'  -> the potato is BLOCKED forever.
#     It stays on cell i, so the OTHER team scores the point
#     (the potato remains on a cell of team i, hence eliminates one
#      of team i's players -> a point for the opposing team).
#
# In 0-indexed code as in the editorial: even indices = Red, odd = Blue.
#   - next empty & i even  -> Red point
#   - next blocked & i odd -> Red point
# Blue's points = total potatoes - Red points (zero-sum).
#
# SAMPLE WALKTHROUGH
# ------------------
# Sample 3: n=3, k=2, s = 1 0 1 1 1 0  (indices 0..5)
#   i=0 (even, s='1', next='0') -> Red   (+1)
#   i=2 (even, s='1', next='1') -> Blue
#   i=3 (odd,  s='1', next='1') -> Red   (+1)
#   i=4 (even, s='1', next='0') -> Red   (+1)
#   Red = 3, Blue = 4 - 3 = 1   -> output "3 1" ✓
#
# Sample 6: n=7, k=4, s=10011110101011
#   Counts: Red gets a point on indices 0,3,6,8,10,12... (computed) -> 7,
#   Blue = 9 - 7 = 2 -> output "7 2" ✓
#
# EDGE CASES / DETAILS
# --------------------
#   - Empty board (all '0')       -> Red = Blue = 0.
#   - Full board (all '1')        -> every potato blocked; even idx -> Blue,
#     odd idx -> Red -> exactly n / n.
#   - A single potato             -> it moves +1 in the final round; who scores
#     depends only on whether it starts on red or blue.
#   - The circular wrap: s[2n-1]'s neighbour is s[0] (mod m).
#   - k can be up to 1e9 but is never used — n can be up to 1e5,
#     sum of n over tests <= 1e5, so a single O(n) scan is plenty.
#
# COMPLEXITY
# ----------
#   Time : O(n) per test case (one pass over the 2n cells).
#   Space: O(1) extra per test case (we only count).
#
# LESSON
# ------
#   Zero-sum games reward finding the "equilibrium simplification": here,
#   everything collapses to one final round and a single local rule
#   (10 -> 01 for each run's tail). Spotting that moving early hands the
#   initiative to the opponent kills the whole game tree. Always ask:
#   "which is the LAST thing that can affect the answer?"
#
# PYTHON NOTES
# ------------
#   - sys.stdin.read().split() reads all tokens fast (good for many tests).
#   - s[(i+1) % m] handles the circular neighbour without special cases.
#   - Only Red is counted in the loop; Blue = total - Red (zero-sum).