from fsm.transition import Transition

class StateMachine:
    def __init__(self, currentState):
        self._newEvent = None
        self._curState = currentState
        self._trans = Transition(self)

    def eventHandler(self, event):
        self.setNewEvent(event)
        self.run()
        
    def setNewEvent(self, event):
        self._newEvent = event
   
    def getCurrentState(self):
        return self._curState

    def setCurrentState(self, state):
        self._curState = state

    def run(self):
        if self._newEvent:
            self._trans.transition(self._newEvent)
            self._newEvent = None

        self._curState.execute()



