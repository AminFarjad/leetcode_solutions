class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:

        su = 0
        i = 1
        prev = sum([int(x) for x in bank[0]])
        print(prev)
        while i < len(bank):
            next = sum([int(x) for x in bank[i]])
            i+=1
            if next ==0:
                continue
            else:
                su += (next * prev)
                prev = next
            # i+=1
        return su


        
