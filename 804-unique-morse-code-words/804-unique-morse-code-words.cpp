class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        string array[] = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        vector<string> myarray(words.size());
        string temp = "";
        for(int j = 0; j < words.size() ; j++){
            for(int i = 0; i < words[j].size(); i++){
                temp += array[words[j][i]-'a'];
            }
            myarray[j] = temp;
            temp = "";
        }
        for(int i = 0; i < myarray.size(); i++){
            for(int j = 0; j < myarray.size(); j++){
                if(i != j && myarray[i] == myarray[j]){
                    myarray.erase(myarray.begin() + j);
                    j--;
                }
            }
        }
        return myarray.size();
    }
};