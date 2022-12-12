class Bus():
    def __init__(self, speed, capasity, maxSpeed, passengers, hasEmptySeats, seats):
        self.speed = speed
        self. capasity = capasity
        self.maxSpeed = maxSpeed
        self.passangers = passengers
        self.hasEmptySeats = hasEmptySeats
        self.seats = [43]
    def passengers(self,value):
        self.seats[0] -= value

    def visadka_posadka(self,value):
        self.seats[0] += value
    def speedup(self,value):
        self.speedup[0] += value
    def speeddown(self,value):
        self.speeddown[0] -= value






