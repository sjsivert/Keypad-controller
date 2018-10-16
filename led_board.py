import RPi.GPIO as GPIO
from time import sleep, time
from random import randint


class LedBoard:
    """ A class for handling lightning of the leds in the arduino """
    pin_led_states = [
        (1, 0, -1),  # 1
        (0, 1, -1),  # 2
        (-1, 1, 0),  # 3
        (-1, 0, 1),  # 4
        (1, -1, 0),  # 5
        (0, -1, 1)   # 6
    ]  # the corresponding pin configuration for each pin

    def __init__(self, led_pins=(18, 23, 24)):
        self.led_pins = led_pins  # the pins used to control the leds (charlieplexed)
        GPIO.setmode(GPIO.BCM)

    def set_pin(self, pin_index, pin_state):
        if pin_state == -1:
            GPIO.setup(self.ledpins[pin_index], GPIO.IN)
        else:
            GPIO.setup(self.ledpins[pin_index], GPIO.OUT)
            GPIO.output(self.ledpins[pin_index], pin_state)

    def turn_on_led(self, led_number):
        for pin_index, pin_state in enumerate(LedBoard.pin_led_states(self.led_number)):
            LedBoard.set_pin(pin_index, pin_state)

    def turn_off_leds(self):
        for pin_index in self.led_pins:
            LedBoard.set_pin(pin_index, 0)

    def light_led(self, led_number, seconds):
        """ Turns on the light specified for the specified number of seconds """
        self.turn_on_led(led_number)
        sleep(seconds)
        self.turn_off_leds()

    def flash_all_leds(self, seconds):
        """ Makes all leds light up for the specified number of seconds """
        start_time = time()
        while time() - start_time < seconds:
            for i in range(6):
                self.turn_on_led(i)
        self.turn_off_leds()

    def twinkle_all_leds(self, seconds):
        """ Makes all leds twinkle for the specified number of seconds """
        start_time = time()
        while time() - start_time < seconds:
            self.flash_all_leds(0.2)
            sleep(0.2)

    def random_blink(self, seconds):
        """ Lights up random leds in sequence for the specified number of seconds """
        start_time = time()
        while time() - start_time < seconds:
            self.turn_on_led(randint(0, 5), 0.1)
            self.turn_off_leds()

    def power_up(self):
        self.twinkle_all_leds(1)
        self.random_blink(0.6)

    def power_down(self):
        self.twinkle_all_leds(1)
        self.random_blink(0.6)
