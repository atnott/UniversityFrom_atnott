#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

void show2d(vector<vector<int>> a) {
    for (int i = 0; i < a.size(); i++) {
        for (int j = 0; j < a[i].size(); j++) {
            cout << a[i][j] << ' ';
        }
        cout << endl;
    }
}

void show(vector<int> a) {
    for (int i = 0; i < a.size(); i++) {
        cout << a[i] << " ";
    }
}

float distanceBetween(vector<int> p1, vector<int> p2) {
    int dx = p1[0] - p2[0];
    int dy = p1[1] - p2[1];
    return sqrt(dx * dx + dy * dy);
}

float findMinSum(vector<vector<int>> reds, vector<vector<int>> blues,
                 vector<bool> used, int redIndex, float currentSum, float bestSum) {
    int n = reds.size();
    if (currentSum >= bestSum) {
        return bestSum;
    }
    if (redIndex == n) {
        if (currentSum < bestSum) {
            bestSum = currentSum;
        }
        return bestSum;
    }

    for (int i = 0; i < n; i++) {
        if (!used[i]) {
            used[i] = true;
            float dist = distanceBetween(reds[redIndex], blues[i]);
            float newSum = currentSum + dist;
            float result = findMinSum(reds, blues, used, redIndex + 1, newSum, bestSum);
            if (result < bestSum) {
                bestSum = result;
            }
            used[i] = false;
        }
    }

    return bestSum;
}

int main() {
    int n;
    cin >> n;
    vector<vector<int>> blue;
    vector<vector<int>> red;

    for (int i = 0; i < n; i++) {
        char color;
        cin >> color;
        vector<int> l;
        if (color == 'r') {
            int x, y;
            cin >> x >> y;
            l.push_back(x);
            l.push_back(y);
            red.push_back(l);
        }
        else {
            int x, y;
            cin >> x >> y;
            l.push_back(x);
            l.push_back(y);
            blue.push_back(l);
        }
    }

    int pointsCount = red.size();
    vector<bool> used(pointsCount, false);
    float bestSum = 1e9;
    float minDistance = findMinSum(red, blue, used, 0, 0.0, bestSum);
    cout << minDistance << endl;
}