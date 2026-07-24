class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position,speed), reverse = True )

        fleet = []

        for pos, sp in cars:

            time = (target- pos) / sp

            if fleet:
                if time > fleet[-1]:
                    fleet.append(time)
            else:
                fleet.append(time)
        
        return len(fleet)
            