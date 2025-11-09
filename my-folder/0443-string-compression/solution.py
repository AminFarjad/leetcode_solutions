class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 1
        if len(chars)<2:
            return len(chars)
        starting = chars[0]
        count = 1

        while i < len(chars):
            if chars[i]==starting:
                count +=1
                chars.pop(i)
                continue
            if count > 1:
                count = str(count)
                counts = list(count)
                for count in counts:
                    chars.insert(i,str(count))
                    i+=1
                
                count=1
            starting = chars[i]
            i+=1
        if count>1:
            count = str(count)
            counts = list(count)
            for count in counts:
                chars.append(count)
        return len(chars)
        
