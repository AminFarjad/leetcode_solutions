import heapq
class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        pq = []
        i = 0
        for server in servers:
            heapq.heappush(pq, (server, i))
            i+=1
        po = []
        i = 1
        item = heapq.heappop(pq)
        heapq.heappush(po, (tasks[0], item))
        l = max(tasks)
        le = len(tasks)
        out = [item[1]]
        j = 1

        while i < l or j < le:
            if po and po[0][0]==i:
                item = heapq.heappop(po)
                heapq.heappush(pq, (item[1][0],item[1][1]))
                continue
            elif pq and j < le:
                item = heapq.heappop(pq)
                heapq.heappush(po, (tasks[j]+i, item))
                j+=1
                out.append(item[1])
                if j < le and j <= i:
                    continue
                i+=1
            else:
                i=po[0][0]
        return out


        
