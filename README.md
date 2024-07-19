# fleet_scheduling
FLEET SCHEDULING 

OVERVIEW:
A python based application designed to manage the charging of trucks at various charging stations.
The system aims to optimize the charging process by efficiently allocating trucks to availabe charging stations.

Features:
 assign trucks to availabe charging stations
 manage charging station capacity and availability
 optimize truck charging schedules to  minimize wait times 

Technical Details:
system is build using Python 3.x
The application uses a simple text based interface for input and output
the system is designed to be modular , with seperate componoent for trucks management, charging station management, and scheduling

Files:
'fleet.py' contains the truck management logic, including truck assignment and scheduling
'test_cases.py' includes sample test cases for the system

Classes:
Truck
Charger
Schedular
SimpleSchedular
SchedularFactory
TruckSchedular

Code Format:
class definitions - defined class including several methods and attributed in order to initiate the process
Method implementaions - implement methods in their respective classes
Example Usage - create a list with varying attributes
Output - print the output of the method calls to demonstrate the charging process

Algorithm Used: GREEDY ALGORITHM
•	This approach was chosen because we want to maximize the number of trucks that can be fully charged within a given time frame. Often greedy algorithm is used to solve the optimization problems.
•	Also no backtracking helps it to be more efficient as once the truck is assigned to a charger , it is not re-assigned again.
•	Apart from the other approaches it is easy to implement and follow and also helped in getting the optimal solution to the given problem.

Getting Started:
1 clone the repository using 'git clone <repository_url>
2 install the required dependendcies using 'pip install -r requirements.txt'
3 run the application using 'python fleet.py'

Contributing:
if you'd like to contribute, please fork the repository and submit a pull request with your changes. Please include detailed description of your changes and any relevent testing or documentation updates

Author:
Paridhii
