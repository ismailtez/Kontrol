class Bus():
    def __init__(self, speed, capasity, maxSpeed, passengers, hasEmptySeats, seats):
        self.speed = speed
        self. capasity = capasity
        self.maxSpeed = maxSpeed
        self.passangers = passengers
        self.hasEmptySeats = hasEmptySeats
        self.seats = [43]
    def passengers(self,value):
        self.seats[0] -= 1
        self.value -= value
    def visadka_posadka(self):
        self.seats[0] +=1





