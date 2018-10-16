"""
Tests all led functions 
"""
from led_board import LedBoard
from time import sleep

lb = LedBoard()
for i in range(6):
    lb.light_led(i,1)

lb.power_up()
lb.random_blink(3)
lb.flash_all_leds(2)
