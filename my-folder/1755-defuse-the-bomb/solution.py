class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k==0:
            return [0] * len(code)
        arr = []
        if k > 0:
            num_sum = sum(code[1:k+1])
            arr.append(num_sum)
            i = 1
            le = len(code)
            while i < le:
                arr.append(arr[-1]-code[i]+code[(i+k)%le])
                i+=1
            
        else:
            num_sum = sum(code[k:])
            # print(num_sum)
            arr.append(num_sum)
            le = len(code)
            i=1
            while i < le:
                arr.append(arr[-1]-code[(k+i-1)]+code[i-1])
                i+=1
            # print(arr)
        return arr

        
        
