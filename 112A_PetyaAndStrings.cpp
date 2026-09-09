// Codeforces 112A - Petya and Strings
// https://codeforces.com/problemset/problem/112/A
// Rating: 800 (Easy)

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    cin >> a >> b;

    // Convert both strings to lowercase for case-insensitive comparison
    transform(a.begin(), a.end(), a.begin(), ::tolower);
    transform(b.begin(), b.end(), b.begin(), ::tolower);

    if (a < b)
        cout << -1 << '\n';
    else if (a > b)
        cout << 1 << '\n';
    else
        cout << 0 << '\n';

    return 0;
}

// --------------------------- FULL EXPLANATION ---------------------------
//
// PROBLEM STATEMENT
// ----------------
// Petya is happy if he receives two strings that are the SAME
// when case is ignored. Given two non-empty strings a and b
// (same length, 1..100 chars, Latin letters only), compare them
// CASE-INSENSITIVELY:
//   - print -1 if a < b
//   - print  0 if a == b
//   - print  1 if a > b
//
// Input format:
//   Line 1: string a
//   Line 2: string b
// Output format:
//   One integer: -1, 0, or 1.
//
// KEY INSIGHT — CASE-INSENSITIVE COMPARISON
// -----------------------------------------
// "a" and "A" should be treated as equal. Direct string comparison
// uses ASCII order where 'A' (65) < 'a' (97), so "A" < "a" in
// raw ASCII — but for this problem they must be considered equal.
//
// Solution: convert BOTH strings to the SAME case (all lowercase
// or all uppercase), then compare. Now identical letters map to
// identical characters, so normal string comparison gives the
// correct answer.
//
// ALGORITHM
// ---------
// 1. Read strings a and b.
// 2. Transform a and b to lowercase using std::transform + ::tolower.
// 3. Compare:
//      a < b  -> print -1
//      a > b  -> print  1
//      a == b -> print  0
//
// Note: C++ std::string already supports <, >, == operators with
// lexicographic comparison, so no manual loop is needed.
//
// SAMPLE WALKTHROUGH
// ------------------
// Statement example 1:
//   a = "aaa",  b = "aaa"   -> both become "aaa"  -> equal -> 0 ✓
// Statement example 2:
//   a = "aaa",  b = "aab"   -> "aaa" < "aab"        -> -1 ✓
// Statement example 3:
//   a = "aAa",  b = "AaA"   -> both become "aaa"    -> equal -> 0 ✓
// Statement example 4:
//   a = "abcd",  b = "abc"  -> "abcd" > "abc"       -> 1 ✓
//
// EDGE CASES / DETAILS
// --------------------
//   - Mixed case like "AbCd" vs "aBcD" -> both -> "abcd" -> 0 ✓
//   - Strings already all lowercase/uppercase -> transform is safe.
//   - Single-character strings -> works fine (transform handles 1 char).
//   - All uppercase vs all lowercase of same letters -> equal -> 0.
//   - Maximum length 100 -> well within string limits.
//
// COMPLEXITY
// ----------
//   Let n = length of the strings (1..100).
//   Time : O(n) — transform touches each character once (O(n) each,
//          two strings), then comparison is O(n).
//   Space: O(1) extra — transform modifies in-place; no extra copies.
//
// LESSON
// ------
//   When you need case-insensitive comparison, normalize the case
//   first (lowercase OR uppercase — doesn't matter which, just be
//   consistent). This is a common pattern in string problems.
//   Also, C++ std::string has built-in lexicographic operators,
//   so prefer them over manual character-by-character loops.
//   std::transform + ::tolower/toupper is the idiomatic way to
//   change case for a whole string at once.
//