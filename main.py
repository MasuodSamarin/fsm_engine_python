#!/usr/bin/python3
from fsm import State
from fsm import StateMachine
from mouseTrap import Waiting, Luring, Trapping, Holding
import os, sys


class Quit(State):
    def enter(self):
        print("Preparing to Exit..")
    def execute(self):
        print("thank you using Simple FSM")
        sys.exit(self)
    def exit():
        pass

def getUserInput(sm):
    return str(input("enter new event({}):".format(
                    sm.getCurrentState().getValidEvents())))

def clearScreen():
    #for windows
    #os.system("cls")
    #for linux 
    os.system("clear")

def printInfo(sm):
    print("="*40)
    print("State object information")
    curState = sm.getCurrentState()
    print("object: ", curState)
    print("events: ", curState.getValidEvents())
    print("dests: ", curState.getValidDests())
    print("="*40)

w = Waiting()
l = Luring()
t = Trapping()
h = Holding()
q = Quit()

wTable = {"appear":l, "quit": q}
lTable = {"enter":t, "runaway":w, "quit":q}
tTable = {"trapped":h, "escape":w, "quit":q}
hTable = {"removed":w, "quit":q}

w.tableRegister(wTable)
l.tableRegister(lTable)
t.tableRegister(tTable)
h.tableRegister(hTable)

sm = StateMachine(w)

def main():
    
    clearScreen()

    while True:
        printInfo(sm)
        newEvent = getUserInput(sm)
        clearScreen()
        sm.eventHandler(newEvent)
        input("hit a key..")
        clearScreen()
if __name__ == "__main__":
    main()
