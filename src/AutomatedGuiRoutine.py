from src.InputListener import InputListener
from time import sleep


class AutomatedGuiRoutine(object):
    def __init__(self, timeInSecondsBetweenEvents: float, numberOfTimesToRepeatRoutine: int):
        self.timeInSecondsBetweenEvents = timeInSecondsBetweenEvents
        self.numberOfTimesToRepeatRoutine = numberOfTimesToRepeatRoutine

    def Process(self):
        isRoutineComplete = False

        inputListener = InputListener()
        while not isRoutineComplete:
            inputListener.ListenOneMouseClick()
            isRoutineComplete = inputListener.ListenOneKeyPressed()

        for event in inputListener.events:
            event.process()
            sleep(self.timeInSecondsBetweenEvents)
