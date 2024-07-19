class Truck:
    #Represents a truck with a battery that needs to be charged.
    def __init__(self, id, max_battery, current_battery):
        #initialize a truck objrct with attributes 
        self.id = id
        self.max_battery = max_battery
        self.current_battery = current_battery

    def needs_charging(self):
        #returns true if the truck needs charging
        return self.current_battery < self.max_battery

    def time_to_full(self, charger_rate):
        #returns the time it takes to charge the truck to full
        return (self.max_battery - self.current_battery) / charger_rate


class Charger:
    #Represents a charger that can charge a truck
    def __init__(self, id, rate):
        #initialize a charger object with attributes
        self.id = id
        self.rate = rate
        self.trucks = []

    def add_truck(self, truck):
        #adds a truck to the charger
        self.trucks.append(truck)

    def __str__(self):
        #returns a string representation of the charger
        return f"Charger {self.id}: {', '.join(str(t.id) for t in self.trucks)}"


class Scheduler:
    #Represents a scheduler that schedules trucks to chargers
    def schedule(self, trucks, chargers, time_hours):
        #schedules trucks to chargers 
        raise NotImplementedError


class SimpleScheduler(Scheduler):
    #A simple scheduler that schedules trucks to chargers in the order they are received
    def schedule(self, trucks, chargers, time_hours):
        chargers.sort(key=lambda c: c.rate) 
         # Sort chargers by rate in ascending order
        trucks.sort(key=lambda t: t.time_to_full(chargers[0].rate))

        for truck in trucks:
            for charger in chargers:
                if len(charger.trucks) < len(chargers) and truck.time_to_full(charger.rate) <= time_hours:
                    charger.add_truck(truck)
                    break
            else:
                print(f"Truck {truck.id} cannot be fully charged within {time_hours} hours.")

        for charger in chargers:
            print(charger)


class SchedulerFactory:
    #A factory that creates schedulers based on the input parameters
    @staticmethod
    def create_scheduler(algorithm):
        #creates a scheduler based on the input algorithm
        if algorithm == "simple":
            return SimpleScheduler()
        # Add more algorithms here
        else:
            raise ValueError(f"Unknown algorithm: {algorithm}")


class TruckScheduler:
    #Represents a scheduler that schedules trucks to chargers based on truck battery level
    def __init__(self):
        pass

    def schedule(self, trucks, chargers, time_hours):
        #schedules trucks to chargers based on truck battery level
        trucks_copy = trucks.copy()
        for charger in chargers:
            if charger.rate <= 0:
                print(f"Charger {charger.id} has a rate of 0. Skipping.")
                continue
            available_trucks = [truck for truck in trucks_copy if truck.needs_charging()]
            if available_trucks:
                truck = self.select_truck(available_trucks)
                self.charge_truck(truck, charger, time_hours)
                trucks_copy.remove(truck)
            else:
                print(f"No trucks need charging at charger {charger.id}. Moving on.")

    def select_truck(self, available_trucks):
        if not available_trucks:
            return None
        return min(available_trucks, key=lambda truck: truck.current_battery)

    def charge_truck(self, truck, charger, time_hours):
        if not truck.needs_charging():
            print(f"Truck {truck.id} is already fully charged. Skipping.")
            return
        charge_amount = charger.rate * time_hours
        truck.current_battery = min(truck.max_battery, truck.current_battery + charge_amount)
        print(f"Charged truck {truck.id} at charger {charger.id} for {time_hours} hours. New battery level: {truck.current_battery}")
