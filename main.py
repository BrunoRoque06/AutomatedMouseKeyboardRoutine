from src.AutomatedMouseKeyboardRoutine import AutomatedMouseKeyboardRoutine

print("Left Control: ")

timeInSecondsBetweenEvents = 1
numberOfTimesToRepeatRoutine = 2

automatedGuiRoutine = AutomatedMouseKeyboardRoutine(timeInSecondsBetweenEvents, numberOfTimesToRepeatRoutine)
automatedGuiRoutine.Process()
