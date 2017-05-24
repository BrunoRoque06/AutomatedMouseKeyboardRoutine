from time import sleep
from InputListener import InputListener

timeInSecondsBetweenEvents = 1
IsRoutineComplete = False

inputListener = InputListener()
while not IsRoutineComplete:
    inputListener.ListenOneMouseClick()
    IsRoutineComplete = inputListener.ListenOneKeyPressed()

for event in inputListener.events:
    event.process()
    sleep(timeInSecondsBetweenEvents)

print('Jobs done.')
