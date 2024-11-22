// By: Kevin Xia
#include <bits/stdc++.h>
using namespace std;

vector<vector<vector<vector<int>>>> states(31, vector<vector<vector<int>>>(31, vector<vector<int>>(31, vector<int>(31, -1)))); // 4D array to represent all possible states for optimization since we know n < 31

bool solve(int a, int b, int c, int d) { // we'll be assuming that we are Patrick playing against Roland and will return values accordingly
    if (a < 0 || b < 0 || c < 0 || d < 0) {
        return true; // if we're at a position in which we've won, return that it's a winning position
    }
    if (states[a][b][c][d] != -1) { // if we've seen this position before
        return states[a][b][c][d];
    }
    bool inWinningPos = false;
    
    // if we can force a losing position from this position, we can win (if we can't, then we're in a losing position)
    inWinningPos = inWinningPos || !solve(a - 2, b - 1, c, d - 2);
    inWinningPos = inWinningPos || !solve(a - 1, b - 1, c - 1, d - 1);
    inWinningPos = inWinningPos || !solve(a, b, c - 2, d - 1);
    inWinningPos = inWinningPos || !solve(a, b - 3, c, d);
    inWinningPos = inWinningPos || !solve(a - 1, b, c, d - 1);

    return (states[a][b][c][d] = inWinningPos); // updating the states array to include whether the current state is winning or losing
}

int main() {
    int n; // getting inputs
    cin >> n;
    int a, b, c, d;
    for (int i = 0; i < n; i ++) {
        cin >> a >> b >> c >> d;
        if (solve(a, b, c, d)) {
            cout << "Patrick" << endl;
        } else {
            cout << "Roland" << endl;
        }
    }
    return 0;
}