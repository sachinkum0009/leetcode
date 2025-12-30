#include <vector>
#include <stdio.h>

using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        
        vector<int> result;
        size_t n = matrix.size();
        size_t p = matrix[0].size();
        if (n == 1 || p == 1) {
            for (size_t i=0; i < n; i++) {
                for (size_t j=0; j<p; j++) {
                    result.push_back(matrix[i][j]);
                }
            }
            return result;
        }
        int row_size = n-1;
        int col_size = p-1;
        vector<int> indexes = {0, 0};
        bool direction = true;
        bool upper = true;
        for (size_t i = 0; i < n*p; i++) {
            result.push_back(matrix[indexes[0]][indexes[1]]);

            if (upper && (indexes[0] + indexes[1]) == col_size) { // row+col=n-1
                direction = !direction;
            }

            if (!upper && (indexes[0] + indexes[1]) == row_size) {
                direction = !direction;
            }

            // if (abs(indexes[0] - indexes[1]) == abs(row_size - col_size)) { // row = col
            if (indexes[0] == row_size && indexes[1] == col_size) { // row = col
                direction = !direction; 
                upper = !upper;
            }
            if (!direction && (indexes[0] - indexes[1] == 1)) {
                // start new spiral
                upper = true;
                direction = !direction;
                row_size--;
                // col_size--;
            }
            if (upper) {
                indexes[direction]++;
            }
            else {
                indexes[direction]--;
            }
        }
        return result;
    }
};

int main() {
    // vector<vector<int>> matrix = {{1,2,3},{4,5,6},{7,8,9}};
    // vector<vector<int>> matrix = {{1,2,3,4},{5,6,7,8},{9,10,11,12}};
    // vector<vector<int>> matrix = {{7},{9},{6}};
    vector<vector<int>> matrix = {{1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16},{17,18,19,20},{21,22,23,24}};
    Solution solution;
    vector<int> result = solution.spiralOrder(matrix);
    for (int val : result) {
        printf("%d ", val);
    }
    printf("\n");
    return 0;
}