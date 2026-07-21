class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort()

        stack = []

        for position,speed in reversed(cars):
            time = (target - position) / speed
            if len(stack) == 0:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)
            else:
                continue

        return len(stack)