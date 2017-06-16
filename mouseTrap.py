from fsm import State

class Waiting(State):
    def enter(self):
        print("enter to Waiting State")

    def execute(self):
        print("Waiting: Broadcasting chess smell... ")

    def exit(self):
        print("exit from Waiting State")

class Luring(State):
    def enter(self):
        print("enter to Luring State")

    def execute(self):
        print("Luring: Presenting chess, door open")

    def exit(self):
        print("exit from Luring State")

class Trapping(State):
    def enter(self):
        print("enter to Trapping State")

    def execute(self):
        print("Trapping: Closing door!")

    def exit(self):
        print("exit from Trapping State")

class Holding(State):
    def enter(self):
        print("enter to Holding State")

    def execute(self):
        print("Holding: Mouse caught..")

    def exit(self):
        print("exit from Holding State")

