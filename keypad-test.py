from keypad import Keyboard

print("Getting signals from raspberry pi. Exit with ctrl-c")
kb = Keyboard()
while True:
    print(kb.get_next_signal()) #  prints out the received signal to the console
