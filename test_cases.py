# test_cases.py
from fleet import Truck, Charger, SchedulerFactory, TruckScheduler

def test_case_1_more_chargers_than_trucks():
    trucks = [
        Truck(1, 100, 50),
        Truck(2, 200, 100),
        Truck(3, 300, 150),
    ]

    chargers = [
        Charger(1, 50),
        Charger(2, 100),
        Charger(3, 150),
        Charger(4, 200)
    ]

    time_hours = 4

    scheduler = SchedulerFactory.create_scheduler("simple")
    scheduler.schedule(trucks, chargers, time_hours)
    print("Test Case 1: More chargers than trucks")
    print()


def test_case_2_fully_charged_in_time():
    trucks = [
        Truck(1, 100, 50),
        Truck(2, 200, 100),
        Truck(3, 300, 150),
        Truck(4, 400, 200),
        Truck(5, 500, 250)
    ]

    chargers = [
        Charger(1, 100),
        Charger(2, 75),
        Charger(3, 50)
    ]

    time_hours = 3

    scheduler = SchedulerFactory.create_scheduler("simple")
    scheduler.schedule(trucks, chargers, time_hours)
    print("Test Case 2: Fully charged in time")
    print()


def test_case_3_equal_number_of_trucks_and_chargers():
    trucks = [
        Truck(1, 100, 50),
        Truck(2, 200, 100),
        Truck(3, 300, 150),
    ]

    chargers = [
        Charger(1, 50),
        Charger(2, 100),
        Charger(3, 150),
    ]

    time_hours = 4

    scheduler = SchedulerFactory.create_scheduler("simple")
    scheduler.schedule(trucks, chargers, time_hours)
    print("Test Case 3: Equal number of trucks and chargers")
    print()


def test_case_4_more_trucks_than_chargers():
    trucks = [
        Truck(1, 100, 50),
        Truck(2, 200, 100),
        Truck(3, 300, 150),
        Truck(4, 400, 200),
    ]

    chargers = [
        Charger(1, 50),
        Charger(2, 100),
    ]

    time_hours = 4

    scheduler = SchedulerFactory.create_scheduler("simple")
    scheduler.schedule(trucks, chargers, time_hours)
    print("Test Case 4: More trucks than chargers")
    print()


def test_case_5_fully_charged_trucks():
    trucks = [
        Truck(1, 100, 100),
        Truck(2, 200, 200),
        Truck(3, 300, 300),
        Truck(4, 400, 400),
        Truck(5, 500, 500)
]

    chargers = [
        Charger(1, 100),
        Charger(2, 75),
]

    time_hours = 2

    Truckscheduler = TruckScheduler()
    Truckscheduler.schedule(trucks, chargers, time_hours)
    print("Test Case 5: Fully charged trucks")
    print()

def main():
    test_case_1_more_chargers_than_trucks()
    test_case_2_fully_charged_in_time()
    test_case_3_equal_number_of_trucks_and_chargers()
    test_case_4_more_trucks_than_chargers()
    test_case_5_fully_charged_trucks()


if __name__ == "__main__":
    main()