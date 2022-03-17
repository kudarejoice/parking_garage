class parkingLot():
    # intitializes the objects to be used. Capacity of 10 tickets and starts with 0 tickets that have been given or spots taken.
    def __init__(self):
        self.capacity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.tickets = 0
        self.currentTicket = {}

    # Gurantees that the garage will not accept more than 10 tickets. Takes a ticket from the capacity and adds a ticket.
    def takeTicket(self):
        if self.tickets >= 10:
            print("The Parking Garage is full.")
        else:
            print(f"Your ticket number is {self.capacity[0]}")
            self.currentTicket[self.capacity[0]]=False
            self.capacity.pop(0)
            self.tickets += 1
    # Checks to see if the ticket is valid or not and if it's paid.
    def payForParking(self):
        while True:
            answer = input("Enter ticket number you would like to pay: (Enter 'quit') ")
            if answer.lower() == 'quit':
                break
            if int(answer) not in self.currentTicket.keys():
                print("Please enter a valid ticket number.")
                self.payTicket()
                break
            elif self.currentTicket[int(answer)] == True:
                print("This ticket has already been paid for. You may exit.")
                break
            else:
                print("Thank you for paying for your ticket. You have 15 minutes to leave.")
                self.currentTicket[int(answer)] = True
                self.capacity.append(int(answer))
                self.tickets -=1
                break

    def leaveGarage(self):
        while True:
            response = input("Ready to exit? Enter your ticket number:(Enter 'quit') ")
            if response.lower() == 'quit':
                break
            if int(response) not in self.currentTickect.keys():
                print("Please enter a valid ticket number. ")
            elif self.currentTicket[int(response)] == False:
                print("Please pay your ticket to exit. ")
                self.payTicket()
            else:
                print("Thank you, have a nice day!")
                self.currentTicket.pop(int(response))
                break
parking_lot = parkingLot()

def choices():
    while True:
        action = input("What would you like to do?" "\n Take Ticket" "\n \t Pay Ticket" "\n \t Exit Garage" "\n \t Quit" "\n")
        if action.lower() == 'quit':
            print("Thank you, have a nice day!")
            break
        elif action.lower() == 'take ticket':
            parking_lot.takeTicket()
        elif action.lower() == 'pay ticket':
            parking_lot.payForParking()
        elif action.lower() == 'exit garage':
            parking_lot.leaveGarage()
choices()