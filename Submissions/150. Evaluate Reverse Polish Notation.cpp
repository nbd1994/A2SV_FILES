class Solution
{
public:
    int evalRPN(vector<string> &tokens)
    {
        stack<int> stack;
        for (const string &token : tokens)
        {
            if (isNumber(token))
            {
                stack.push(stoi(token));
            }
            else
            {
                int operand2 = stack.top();
                stack.pop();
                int operand1 = stack.top();
                stack.pop();
                switch (token[0])
                {
                case '+':
                    stack.push(operand1 + operand2);
                    break;
                case '-':
                    stack.push(operand1 - operand2);
                    break;
                case '*':
                    stack.push(operand1 * operand2);
                    break;
                case '/':
                    stack.push(operand1 / operand2);
                    break;
                }
            }
        }
        return stack.top();
    }

private:
    bool isNumber(const string &token)
    {
        return (token != "+" && token != "-" && token != "*" && token != "/");
    }
};