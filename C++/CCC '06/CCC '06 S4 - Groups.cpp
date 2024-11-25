// By: Kevin Xia

#include <bits/stdc++.h>
using namespace std;

bool testGroup(vector<vector<int>> test) {
    bool met;
    int identity = -1;
    int size = test.size();

    // finding the identity
    for (int i = 0; i < size; i++) {
        bool is_identity = true;
        for (int j = 0; j < size; j++) {
            if (test[i][j] != j || test[j][i] != j) { // assuming i is the identity
                is_identity = false;
                break;
            }
        }
        if (is_identity) {
            identity = i;
            break;
        }
    }

    // if identity wasn't found
    if (identity == -1) {
        return false;
    }

    // checking associativity and inverse
    for (int i = 0; i < size; i ++) { // the y value
        met = false;
        for (int j = 0; j < size; j ++) { // the x value
            for (int k = 0; k < size; k ++) { // k is just for associativity, tested at the same time
                if (test[i][test[j][k]] != test[test[i][j]][k]) {
                    return false;
                }
            }
            if (test[i][j] == identity && test[j][i] == identity) { // if we've found a case for inverse
                met = true;
            }
        }
        if (!met) { // if we didn't find one for all values of j
            return false;
        }
    }
    return true; // if no checks were failed, then yes it works
}

int main() {
    int n; // getting inputs
    while (true) {
        cin >> n;
        vector<vector<int>> test(n, vector<int>(n, 0));
        if (n == 0) {
            return 0;
        }
        for (int i = 0; i < n; i ++) {
            for (int j = 0; j < n; j ++) {
                cin >> test[i][j];
                test[i][j] -= 1;
            }
        }
        if (testGroup(test)) {
            cout << "yes" << endl;
        } else {
            cout << "no" << endl;
        }
    }
    return 0;
}