class Solution(object):
    def convert(self, s, numRows):
        if numRows < 2:
            return s
        elif numRows == 2:
            temp = ''
            temp2 = ''
            for i in range(0,len(s)):
                if i%2 == 0:
                    temp +=s[i]
                else:
                    temp2+=s[i]
            return temp+temp2
        else:
            temp = []
            for i in range(0,numRows):
                temp.append([])
            i = 0
            flag = False
            for cha in s:
                temp[i].append(cha)
                if i+1 == numRows:
                    flag = True
                elif i-1 == 0 and flag:
                    flag = False
                    i = -1
                if flag:
                    i-=1
                else:
                    i+=1
            print(temp)
            temp1 = ''
            for row in temp:
                for char in row:
                    temp1+=char
            return temp1




        
