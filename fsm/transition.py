

class Transition:
    def __init__(self, stateMachine):
        self._sm = stateMachine

    def transition(self, event):
        curState = self._sm.getCurrentState()
        nextState = curState.nextState(event)
        
        if nextState:
            self._sm.getCurrentState().exit()
            self._sm.setCurrentState(nextState)
            self._sm.getCurrentState().enter()

