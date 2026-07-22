class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleet = []
        cars = sorted(zip(position,speed), reverse = True)

        for pos,speed in cars:

            time = (target - pos) / speed

            if len(fleet) == 0 or time > fleet[-1]:
                fleet.append(time)
        
        return len(fleet)