class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country
    def myLocation(self):
        print("Hi, my name is " + self.name + " and I live in " + self.country + ".")

    
#loc = Location("Carlos", "Brasil")
#print(loc.name)
#print(loc.country)
#print(type(loc))

loc1 = Location("Tomas","Portugal")
loc1.myLocation()

loc2 = Location("Ying", "China")
loc3 = Location("Amare", "Kenya")

loc2.myLocation()
loc3.myLocation()

Carlos_loc = Location("Carlos", "Brasil")
Carlos_loc.myLocation()