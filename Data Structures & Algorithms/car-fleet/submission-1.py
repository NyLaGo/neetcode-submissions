class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        road = []

        for i in range(n):
            road.append((position[i], speed[i]))
        
        road.sort(reverse=True)

        for i in range(n):
            p, s = road[i]
            road[i] = (target - p) / s

        stack = []
        for i in range(n):
            if stack and road[i] <= stack[-1]:
                continue
            
            stack.append(road[i])

        return len(stack)
        