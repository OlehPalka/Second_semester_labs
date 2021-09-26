"""
Implementation of the main simulation class.
"""
import random
from arrays import Array
from llistqueue import Queue
from people import TicketAgent, Passenger


class TicketCounterSimulation:
    """
    Create a simulation object.
    """

    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
        self._arriveProb = float(1.0 / betweenTime)
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes
        self._passengerQ = Queue()
        self._theAgents = Array(numAgents)
        for i in range(numAgents):
            self._theAgents[i] = TicketAgent(i+1)
        # Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0

    def run(self):
        """
        Run the simulation using the parameters supplied earlier.
        """
        for curTime in range(self._numMinutes + 1):

            self._handleArrive(curTime)

            self._handleBeginService(curTime)

            self._handleEndService(curTime)
            self.printResults()

    def printResults(self):
        """
        Print the simulation results.
        """
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float(self._totalWaitTime) / numServed
        print("")
        print("Number of passengers served = ", numServed)
        print("Number of passengers remaining in line = %d" %
              len(self._passengerQ))
        print("The average wait time was %4.2f minutes." % avgWait)

    def _handleArrive(self, curTime):
        """
        Handles simulation rule #1.
        """
        prob = float(random.random())
        if prob <= self._arriveProb:
            self._numPassengers += 1
            print(self._numPassengers)
            self._passengerQ.enqueue(Passenger(self._numPassengers, curTime))

    def _handleBeginService(self, curTime):
        """
        Handles simulation rule #2.
        """
        for agent in self._theAgents:
            if agent.isFree():
                try:
                    agent.startService(self._passengerQ.dequeue(),
                                       curTime + self._serviceTime)
                except AssertionError:
                    break
        print(len(self._passengerQ))
        print("lenth")
        self._totalWaitTime += float(len(self._passengerQ))

    def _handleEndService(self, curTime):
        """
        Handles simulation rule #3.
        """
        for agent in self._theAgents:
            if not agent.isFree():
                if agent.isFinished(curTime):
                    agent.stopService()
