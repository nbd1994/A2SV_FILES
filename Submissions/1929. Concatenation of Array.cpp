class Solution
{
public:
    vector<int> getConcatenation(vector<int> &nums)
    {
        vector<int> arr(nums.size() * 2);
        for (int i = 0; i < nums.size(); i++)
        {
            arr[i] = arr[i + nums.size()] = nums[i];
        }
        return arr;
    }
};