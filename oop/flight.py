class Flight():
    def __init__(self, capacite):
        self.capacite = capacite
        self.passagers = []

    def add_passager(self, name):
        if not self.open_sets():
            print(f"Maximum capacity reached! {name} has not added")
        else:
            self.passagers.append(name)
            print(f"Passager {name} has successfuly added!")

    def open_sets(self):
        return (self.capacite) - len(self.passagers)

    def get_passagers(self):
        return self.passagers

    def get_maximum_capacity(self):
        return self.capacite


flight = Flight(3)
print(f"Maximum capacity of the flight is {flight.get_maximum_capacity()}")
peoples = ["Denis", "Lucas", "Kayque", "Kelvyn"]

for people in peoples:
    flight.add_passager(people)

print(f"List of passagers: {flight.get_passagers()}")
