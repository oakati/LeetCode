class Solution {
public:
    bool isBoomerang(vector<vector<int>>& points) {
        cout << (points[0][0]-points[1][0]) << endl;
        cout << (points[0][1]-points[1][1]) << endl;
        cout << (points[1][0]-points[2][0]) << endl;
        cout << (points[1][1]-points[2][1]) << endl;
        return !((points[0][1]-points[1][1])*(points[1][0]-points[2][0])==(points[0][0]-points[1][0])*(points[1][1]-points[2][1]));
    }
};