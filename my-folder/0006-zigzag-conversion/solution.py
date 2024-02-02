class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if len(s) < 2 or numRows<2:
            return s
        
        temp = []
        #  [
        #    []
        #    []
        #   ]
        for i in range(numRows):
            temp.append([])
        i=0
        flag = False
        for char in s: 
            if flag:
                temp[i].append(char)
                i=i-1
                if i==0:
                    flag = False
                continue

            temp[i].append(char)
            i = (i+1)
            if i == numRows:
                flag = True
                i = i-2
                if i<=0:
                    i=0
                    flag = False

        temp_str=''
        for t in temp:
            for char in t:
                temp_str += char
        return temp_str
                

