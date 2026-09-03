// Codeforces 71A - Way Too Long Words
// https://codeforces.com/problemset/problem/71/A
// Rating: 800 (Easy)

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    while (n--) {
        string s;
        cin >> s;

        int len = (int)s.size();

        if (len > 10)
            cout << s[0] << len - 2 << s[len - 1] << '\n';
        else
            cout << s << '\n';
    }

    return 0;
}

// --------------------------- FULL EXPLANATION ---------------------------
//
// PROBLEM STATEMENT
// ----------------
// Sometimes words are too long to be convenient, so we abbreviate them.
// Given n words, for EVERY word we apply this rule:
//   - If the word's length is strictly greater than 10
//     (i.e. length >= 11), replace it with:
//         first letter + (length - 2) + last letter
//   - Otherwise, print the word exactly as it is.
//
// Examples from the statement:
//   "word"            -> len 4  <= 10  -> "word"
//   "localization"    -> len 12 >  10  -> "l10n"   (l + 10 + n)
//   "internationalization"            -> "i18n"   (i + 18 + n)
//   "pneumonoultramicroscopicsilicovolcanoconiosis" -> "p43s"
//
// APPROACH
// --------
// This is a pure implementation / string-manipulation problem.
// 1. Read n (number of words).
// 2. For each word, read it as a std::string.
// 3. Compute len = s.size().
// 4. If len > 10, print:
//        s[0] << (len - 2) << s[len-1]
//    Note: s[0] is first char, s[len-1] is last char, and the
//    integer (len - 2) is printed as a number (the count of the
//    letters we removed from the middle).
// 5. Else print the whole word unchanged.
//
// WHY len - 2?
//    The original word has len letters. We keep 2 letters
//    (first + last), so exactly (len - 2) letters were "taken out"
//    of the middle — that number is what appears in the abbreviation.
//    Example: "internationalization" has 20 letters -> i 18 n, "i18n".
//
// EDGE CASES / DETAILS
// --------------------
//   - A word of length exactly 10 stays unchanged
//     ("pneumonoult..." style long words only kick in at len >= 11).
//   - Words are lowercase English letters, so position s[0] and
//     s[len-1] are always safe to access (strings are never empty).
//   - Using '\n' instead of endl avoids flushing the buffer on every
//     line, which matters for n up to 100.
//
// COMPLEXITY
// ----------
//   Let L = length of the longest word (<= 100).
//   Time : O(n * L)  — we read each string and do O(L) work
//          reading/printing it. The check itself is O(1) per word.
//   Space: O(L)  — only one string held in memory at a time.
//
// LESSON
// ------
//   Easy string problems are mostly about careful reading of the
//   rule ("strictly more than 10") and knowing string indexing.
//   No fancy algorithm — just convert the rule into code exactly.
//