class Solution {
public:
    int countAsterisks(string s) {
        bool flag = true;
        int counter = 0;
        for(int i = 0; i < s.size(); i++){
            if(s[i] == '|'){
                flag = not flag;
            }
            if(flag == true && s[i] == '*'){
                counter++;
            }
        }
        return counter;
    }
};