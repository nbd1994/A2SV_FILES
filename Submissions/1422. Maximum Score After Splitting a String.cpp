class Solution {
public:
    int maxScore(string s) {
        int maxCount=0, right, left, leftCount,rightCount,count;
       for(int i=1; i<=s.length()-1; i++){
           right=s.length()-i;
           left=s.length()-right;
           leftCount =0;
           rightCount =0;
           for(int j=0; j<left;j++) if(s[j]=='0') leftCount++;
           for(int k=s.length()-right; k<=s.length()-1;k++) if(s[k]=='1') rightCount++;
           count = rightCount+leftCount;
           if(count>maxCount) maxCount=count;
       }
       return maxCount; 
    }
};