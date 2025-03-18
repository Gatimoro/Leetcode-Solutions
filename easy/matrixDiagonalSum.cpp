class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int ans = 0;
        int last = mat.size()-1;
        for(int i = 0; i<=last; i++){
            ans += mat[i][i] + mat[i][last-i];
        }return (mat.size() % 2 == 1) ? ans - mat[(int)mat.size()/2][(int)mat.size()/2] : ans;
    }
};
