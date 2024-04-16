class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            num = str(-(num))
            num = sorted(num , key=lambda x:x*10, reverse =True)
            num = "-"+"".join(num)
            return int(num)
        else:
            num = str(num)
            num = sorted(num , key=lambda x: x*10)
            if num[0]=='0':
                i=0
                while i < len(num) and num[i]=='0':
                    i+=1
                if i < len(num):
                    num.insert(0,num.pop(i))
            num = "".join(num)
            return int(num)
            
        