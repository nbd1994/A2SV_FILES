class Solution
{
public:
    int maxWidthOfVerticalArea(vector<vector<int>> &points)
    {
        int max = 0, area;
        sort(points.begin(), points.end());
        for (int i = 0; i < points.size() - 1; i++)
        {
            area = points[i + 1][0] - points[i][0];
            if (area > max)
                max = area;
        }
        return max;
    }
};