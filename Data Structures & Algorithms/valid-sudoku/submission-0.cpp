class Solution {
public:
    bool isvalidArr(vector<char>& arr){
        map <char, bool> nbs;
        for (int i = 1; i <= 9; i++)
            nbs[i+'0'] = false;
        for (char x : arr){
            if (x == '.')
            continue;
            if (nbs[x])
            return false;
            nbs[x] = true;
        }
        return true;
    }
    bool isValidSudoku(vector<vector<char>>& board) {
        for (vector<char> arr : board){
            if (!isvalidArr(arr))
            return false;
        }
        for (int i = 0; i < 9; i++){
            vector<char> arr;
            for (int j = 0; j < 9; j++){
                arr.push_back(board[j][i]);
            }
            if (!isvalidArr(arr))
            return false;
        }
        vector <pair<int, int>> index;
        for (int i = 0; i < 9; i += 3){
            for (int j = 0; j < 9; j+= 3)
                 index.push_back({i,j});
        }
        for (int k = 0; k < 9; k++){
            vector<char> arr;
            auto [i, j] = index[k];
            for (int t = 0; t < 3; t++){
                for (int y = 0; y < 3; y++)
                     arr.push_back(board[i+t][j+y]);
            }
            if (!isvalidArr(arr))
            return false;
        }
        return true;

    }
};
