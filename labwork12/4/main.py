
from simulation import TicketCounterSimulation

print("Welcome the Simulator")
agents_num = int(input("Enter the agents number: "))
lenth = int(input("Enter lenth of the process: "))
between_time = int(input("Enter a between time per customer: "))
service = float(input("Enter the the service time: "))
model = TicketCounterSimulation(agents_num, lenth, between_time, service)

model.run()
