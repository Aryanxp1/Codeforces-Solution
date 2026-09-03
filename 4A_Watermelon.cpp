// Codeforces 4A - Watermelon
// https://codeforces.com/problemset/problem/4/A
// Rating: 800 (Easy)
//
// A watermelon weighs w kg. We want to split it into two parts,
// each weighing a positive even number of kg.
//
// This is possible iff w is even and w > 2.
//   - w must be even so both halves can be even.
//   - w > 2 guarantees each half is at least 2 (i.e., positive and even),
//     since the smallest even positive part is 2 kg.

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