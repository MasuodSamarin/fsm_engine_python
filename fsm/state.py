from abc import ABCMeta, abstractmethod, abstractproperty

class State(metaclass=ABCMeta):
    '''for each state you can define a subclass which inherit from State
       it have to has three method (enter, executes, exit)'''
    def __init__(self):
        '''transTable holds event to destinition table'''
        self._transTable = {}

    def tableRegister(self, table):
        '''add an event and destinition 
           event must be string, int or enum and the dest must be
           inherit from State base class
           in dictionry:
               key is event,
                value is destinition
            ex: map={"toStateA" : stateA}
        '''
        for event, dest in table.items():
            if isinstance(dest, State):
                self._transTable[event] = dest
            else:
                raise ValueError("{} must be inherit from State base class".format(dest))

    def getValidEvents(self):
        '''get the all events which is valid '''
        return list(self._transTable.keys())

    def getValidDests(self):
        '''get all destinition which the state can go'''
        return list(self._transTable.values())

    def nextState(self, event):
        '''if the given event is valid for State its return the destinition state 
            if not this simply return None value'''
        return self._transTable.get(event, None)
 
    def can(self, event):
        '''the given event is can occure or not'''
        if event in self.getValidEvents():
            return True
        else:
            return False

    '''abstractmethod which must be override in subclasses'''
    @abstractmethod
    def enter(self):
        '''executes once when machien enter to state'''
        print("default enter")

    @abstractmethod
    def execute(self):
        '''executes until machine is in the state'''
        print("default execute")

    @abstractmethod
    def exit(self):
        '''executes once when machine exit from state'''
        print("default exit")

 

   


