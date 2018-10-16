
class KPC:
    def __init__(self, keypad, led_board):
        self.keypad = keypad
        self.led_board = led_board

        #---Password---
        self.pw = "123"
        self.pw_1st_cache = None
        self.pw_accumulator = ""
        self.verify_attempt = False
        self.verify_result = "N"

        #---Led---
        self.led_select = None
        self.led_time = ""

        #--shutdown--
        self.shutdown_1st = False

    def init_passcode_entry(self):
        """Calls the LED board power up method."""
        self.led_board.power_up()

    def get_next_signal(self):
        """Gets the next signal from keypad and returns this to the FSM. In case of a login attempt the method returns
        an override signal to determine whether the login was successful."""
        if self.verify_attempt:
            self.verify_attempt = False
            return self.verify_result
        else:
            return self.keypad.get_next()

    def verify_login(self, signal):
        """Checks if login is successful by comparing what is currently in the password accumulator and password.
        Calls LED board methods to signal result."""
        print(self.pw_accumulator)
        print(self.pw)
        self.verify_attempt = True
        if self.pw_accumulator == self.pw:
            self.reset_password_accumulator(None)
            self.verify_result = "Y"
            self.login_success(signal)
        else:
            self.verify_result = "N"
            self.login_fail(signal)


    # -----LedBoard Methods-----
    def select_led(self, led_id):
        """Selects a LED that is going to be lit up."""
        self.led_select = led_id

    def verify_led_select(self, signal):
        """Dummy method to confirm LED select."""
        pass

    def append_next_time_digit(self, signal):
        """Appends the user-specified time digits to the total time the LED is going to be lit."""
        self.led_time += signal

    def light_selected_led(self, signal):
        """Instructs the LED board to light the LED selected for the amount of time specified by previous methods."""
        self.led_board.light_led(self.led_select-1, self.led_time)
        self.refresh_agent(signal)

    def flash_leds(self, seconds):
        """Instructs the LED board to flash all lights indicating failure"""
        self.led_board.flash_all_leds(seconds)

    def twinkle_leds(self, seconds):
        """"Instructs the LED board to flash all lights indicating success"""
        self.led_board.twinkle_all_leds(seconds)

    def login_success(self, signal):
        """Calls twinkle_leds to indicate success"""
        self.twinkle_leds(2)

    def login_fail(self, signal):
        """Calls flash_leds to indicate failure"""
        self.flash_leds(2)

    def password_changed(self, signal):
        """Calls twinkle_leds to indicate success"""
        self.twinkle_leds(2)

    def password_did_not_change(self, signal):
        """Calls flash_leds to indicate failure"""
        self.flash_leds(2)

    def exit_action(self):
        """Calls the LED board power_down method."""
        self.led_board.power_down()

    # -----Password Methods-----
    def reset_password_accumulator(self, signal): # resets input accumulaor
        self.pw_accumulator = ""

    def append_next_password_digit(self, signal):
        """Appends the user-specified password digits to the password accumulator."""
        self.pw_accumulator += signal
        print(self.pw_accumulator)

    def verify_new_password(self, signal):
        """Verifies the new password by comparing 1st cache of password and second confirmation stored in password
        accumulator."""
        print(self.pw_accumulator)
        print(self.pw_1st_cache)
        if self.pw_accumulator == self.pw_1st_cache:
            self.pw = self.pw_1st_cache
            self.refresh_agent(signal)
            self.password_changed(signal)
        else:
            self.password_did_not_change(signal)

    def cache_1st_password(self, signal):
        """Caches the first password change attempt."""
        self.pw_1st_cache = self.pw_accumulator
        self.reset_password_accumulator(signal)

    #---Agent update-methods---

    def reset_agent(self, signal):
        """Resets the agent by resetting the password accumulator"""
        self.reset_password_accumulator(signal)

    def refresh_agent(self, signal):
        """Refreshes the agent by resetting the password accumulator, password 1st cache and les_select."""
        self.led_select = None
        self.reset_password_accumulator(signal)
        self.pw_1st_cache = None

    def fully_activate_agent(self, signal):
        """Dummy method that is called when FSM enters s3"""
        pass

    def shutdown_attempt(self, signal):
        """Caches the first shutdown attempt."""
        self.shutdown_1st = True

    def full_shutdown(self, signal):
        """Confirmation of shutdown and calls indirectly LED board power_down method"""
        if self.shutdown_1st:
            self.shutdown_1st = False
            self.exit_action()


