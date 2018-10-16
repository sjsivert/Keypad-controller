import RPi.GPIO as GPIO
from time import time, sleep


class Keyboard:
    key_dic = {
        (0, 0): "1",
        (0, 1): "2",
        (0, 2): "3",
        (1, 0): "4",
        (1, 1): "5",
        (1, 2): "6",
        (2, 0): "7",
        (2, 1): "8",
        (2, 2): "9",
        (3, 0): "*",
        (3, 1): "0",
        (3, 2): "#",
        }

    def __init__(self, row_pins=[18, 23, 24, 25], column_pins=[17, 27, 22]):
        """ Set pins to right modes """
        GPIO.setmode(GPIO.BCM)
        for row_pin in row_pins:
            GPIO.setup(row_pin, GPIO.OUT)
        for column_pin in column_pins:
            GPIO.setup(column_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        self.row_pins = row_pins
        self.column_pins = column_pins

    def check_if_keypress(self, column_pin):
        """ Makes sure that a key pressed is an actual keypress and not static electricity """
        start_time = time()
        while time() - start_time < 0.2:
            if GPIO.input(column_pin) == GPIO.LOW:
                return False  # The keypress lasted for less than 0.2 seconds
        while True:
            if GPIO.input(column_pin) == GPIO.LOW:
                sleep(0.1)  # make sure the key is stabilized
                return True  # The keypress lasted for more than 0.2 seconds and the key is now released

    def do_polling(self):
        """
        Reads the input of the keypad
        Returns coordinates of the form (row, colum) if a key is pressed
        Returns None otherwise
        """
        for i, row_pin in enumerate(self.row_pins):
            GPIO.output(row_pin, GPIO.HIGH)
            for j, column_pin in enumerate(self.column_pins):
                if GPIO.input(column_pin) == GPIO.HIGH:
                    if self.check_if_keypress(column_pin):
                        return (i, j)
            GPIO.output(row_pin, GPIO.LOW)
        return None

    def get_next_signal(self):
        """ returns the next key pressed on the keypad """
        while True:
            poll_result = self.do_polling()
            if poll_result:
                return Keyboard.key_dic[poll_result]
