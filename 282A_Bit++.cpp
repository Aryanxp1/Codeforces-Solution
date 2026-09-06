// Codeforces 282A - Bit++ 
// https://codeforces.com/problemset/problem/282/A
// Rating: 800 (Easy)

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    int counter = 0;

    while (n--) {
        string s;
        cin >> s;

        if (s == "X++" || s == "++X") 
            counter++;
        else if (s == "X--") 
            counter--;
    }

    cout << counter << '\n';

    return 0;
}

// --------------------------- FULL EXPLANATION ---------------------------
//
// PROBLEM STATEMENT
// ----------------
// The problem involves a variable (initially 0) that starts at 0.
// There are n operations (1 <= n <= 100), each being one of three types:
//   "X++"  -> increment the variable by 1
//   "++X"  -> increment the variable by 1
//   "X--"  -> decrement the variable by 1
// 
// Task: after processing all n operations, output the final value of the variable.
//
// Input format:
//   Line 1: n (number of operations)
//   Next n lines: one of "X++", "++X", or "X--"
//
// Output format:
//   One integer - the final value of the variable.
//
// KEY INSIGHT
// -----------
// The variable is incremented if the string contains "++", 
// and decremented if it contains "X--". The trick is that "++X" 
// and "X++" are both increment operations - the position of "++" 
// doesn't matter, only that it appears somewhere in the string.
//
// ALGORITHM
// ---------
// 1. Read n (number of operations)
// 2. Initialize counter = 0
// 2. Repeat n times:
//      a. Read string s
//      2a. If s is "X++" or "++X", increment counter
//      2b. If s is "X--", decrement counter
// 3. Print counter
//
// SAMPLE WALKTHROUGH
// ------------------
// Input:
//   3
//   X++
//   ++X
//   X--
// 
// Steps:
//   - Read "X++" → counter becomes 1
//   - Read "++X" → counter becomes 2
//   - Read "X--" → counter becomes 0
// Output: 0 ✓
//
// EDGE CASES & DETAILS
// --------------------
//   - The string is always exactly 3 characters long (no spaces)
//   - Operations are guaranteed to be one of the three types
//   - n is at most 100, so a simple loop is sufficient
//   - Initial value is 0 (as per problem statement)
//   - No need for complex parsing - direct string comparison works
//
// COMPLEXITY
// ----------
//   Time : O(n) - constant time per operation (string comparison)
//   Space: O(1) - only a few variables used
//
// LESSON
// ------
//   This problem teaches string comparison and how to parse simple 
//   command patterns. The key insight is that "++" always means 
//   increment regardless of position, and "X--" always means 
//   decrement. Recognizing this pattern makes the solution trivial.
//   Also note the compact while (n--) loop - a common idiom for 
//   counting down from n to 0.
//