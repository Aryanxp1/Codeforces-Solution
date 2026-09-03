// Codeforces 4A - Watermelon
// https://codeforces.com/problemset/problem/4/A
// Rating: 800 (Easy)

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int w;
    cin >> w;

    if (w % 2 == 0 && w > 2)
        cout << "YES\n";
    else
        cout << "NO\n";

    return 0;
}

// --------------------------- FULL EXPLANATION ---------------------------
//
// PROBLEM STATEMENT
// ----------------
// There is a watermelon weighing w kilograms (1 <= w <= 100).
// We want to split it into two parts so that BOTH parts weigh an
// even (and positive) number of kilograms. If that split exists,
// print "YES", otherwise print "NO".
//
// When is a split possible?
// ------------------------
// Let the two parts weigh a and b kilograms, with a + b = w.
//
// Requirement 1: w must be even.
//   If w is odd, then a + b is odd, so no matter how we split,
//   one part is even and the other is odd. -> Impossible.
//   (Even + Even = Even, Odd + Odd = Even, so an odd sum can
//    only be Even + Odd.)
//
// Requirement 2: w must be > 2.
//   If w = 2, the only split is 1 + 1, but both parts are odd.
//   The smallest positive EVEN part is 2 kg, so the lightest
//   watermelon we can split correctly is 2 + 2 = 4 kg.
//
// So the answer is YES  <=>  (w is even) AND (w > 2).
//
// Is every even w > 2 really splittable?
//   Yes. Pick a = 2 and b = w - 2:
//     - a = 2 is positive and even.  ✓
//     - b = w - 2 >= 2 (since w > 2) and b is even.  ✓
//   Example: w = 8  ->  2 + 6, both even.   w = 100 -> 2 + 98.
//
// EDGE CASES
// ----------
//   w = 1  -> NO  (can't split at all / not even)
//   w = 2  -> NO  (1 + 1 = odd parts)
//   w = 3  -> NO  (even + odd always)
//   w = 4  -> YES (2 + 2)
//
// COMPLEXITY
// ----------
//   Time : O(1)  — a single O(1) check after reading one integer.
//   Space: O(1)  — no extra data structures used.
//
// LESSON
// ------
//   At rating 800, the trick is usually a simple mathematical
//   observation. Here, one modulo + one comparison solves the
//   whole problem — no loops, no arrays.
//