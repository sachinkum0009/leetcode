/**
 * Rotate Image
 *
 * Given an `nxn` 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
 */

#include <vector>
#include <stdio.h>

using namespace std;

class Solution
{
public:
    void rotate(vector<vector<int>> &matrix)
    {
        size_t n = matrix.size();
        // Step 1: Transpose the matrix
        for (size_t i = 0; i < n; i++)
        {
            for (size_t j = i+1; j < n; j++)
            {
                swap(matrix[i][j], matrix[j][i]);
            }
        }

        // Step 2: Reverse the matrix
        for (size_t i = 0; i < n; i++)
        {
            size_t left = 0;
            size_t right = n - 1;
            while (left < right)
            {
                swap(matrix[i][left], matrix[i][right]);
                left++;
                right--;
            }
        }
    }
};

int main()
{
    vector<vector<int>> matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    Solution my_solution;
    my_solution.rotate(matrix);

    for (size_t i = 0; i < matrix.size(); i++)
    {
        for (size_t j = 0; j < matrix[0].size(); j++)
        {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }

    return 0;
}
