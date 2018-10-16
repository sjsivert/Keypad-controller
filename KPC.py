
class KPC:
    def __init__(self):
        pass

    def init_passcode_entry(self): # power up method
        pass

    def get_next_signal(self): # return override-signal or get next keypress from keypad
        pass

    def verify_login(self, pw): # check user-entered password with correct password (in a file)
        pass

    def validate_passcode_change(self, pw): # check that newly-entered password is legal
        pass

    def light_one_led(self, led_id): # Call LED boards light_led method
        pass

    def flash_leds(self): # call LED boards flash_all_leds method
        pass

    def twinkle_leds(self): # call LED boards twinkle all leds
        pass

    def exit_action(self): # Call LED boards power down method
        pass
