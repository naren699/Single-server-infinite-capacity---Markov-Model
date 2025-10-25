# Getting Inputs
ArrivalTime = int(input("Enter the mean inter arrival time of objects from feeder (in secs) : "))
ServiceTime = int(input("Enter the mean inter service time of the Lathe Machine (in secs) : "))
TimeByRobot = int(input("Enter the time taken by the Robot (in secs) : "))

# Calculating Lambda and Mu
Lambda = 1 / ArrivalTime
Mu = 1 / ServiceTime

print(f"Value of Lambda λ : {Lambda:.3f}")
print(f"Value of Mu μ : {Mu:.3f}")

# Single Server with Infinite Capacity - (M/M/1):(∞/FIFO)
if Lambda < Mu:
    Ls = Lambda / (Mu - Lambda)
    Lq = Ls - (Lambda / Mu)
    Ws = Ls / Lambda
    Wq = Lq / Lambda
    print("Average number of objects in the system : %0.2f " % Ls)
    print("Average number of objects in the conveyor :  %0.2f " % Lq)
    print("Average waiting time of an object in the system : %0.2f secs" % Ws)
    print("Average waiting time of an object in the conveyor : %0.2f secs" % Wq)
    print("Probability that the system is busy : %0.2f " % (Lambda / Mu))
    print("Probability that the system is empty : %0.2f " % (1 - Lambda / Mu))
else:
    print("Warning! Objects Over flow will happen in the conveyor")
