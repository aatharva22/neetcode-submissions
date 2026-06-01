class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        lastTime = 0
        cars = sorted(zip(position,speed), reverse = True)

        for pos,speed in cars:
            
            time = (target - pos) / speed

            if time > lastTime:
                fleet += 1
                lastTime = time
            
        return fleet
