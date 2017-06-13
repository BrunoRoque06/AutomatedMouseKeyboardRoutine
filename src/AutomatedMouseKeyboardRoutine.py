from src.InputListener import InputListener
from time import sleep


class AutomatedMouseKeyboardRoutine(object):
    def __init__(self, timeInSecondsBetweenEvents: float, numberOfTimesToRepeatRoutine: int):
        self.timeInSecondsBetweenEvents = timeInSecondsBetweenEvents
        self.numberOfTimesToRepeatRoutine = numberOfTimesToRepeatRoutine

    def Process(self):
        inputListener = self.ListenInputs()
        for numberOfTimes in range(0, self.numberOfTimesToRepeatRoutine):
            self.RepeatInputs(inputListener)

    def ListenInputs(self) -> InputListener:
        inputListener = InputListener()
        isRoutineComplete = False
        while not isRoutineComplete:
            inputListener.ListenOneMouseClick()
            isRoutineComplete = inputListener.ListenOneKeyPressed()
        return inputListener

    def RepeatInputs(self, inputListener: InputListener):
        for event in inputListener.events:
            event.process()
            sleep(self.timeInSecondsBetweenEvents)
