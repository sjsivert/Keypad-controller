import keypad
import led_board
import FSM

class KPC:
    def __init__(self, keypad, fsm, led_board):
        self._keypad = keypad
        self._fsm = fsm
        self._led_board = led_board

        # skriver assert for å fortelle pycharm typen til objektet
        # slik at vi får autocomplete :))
        assert isinstance(self._fsm, FSM.FSM)
        assert isinstance(self._led_board, led_board.LedBoard)
        assert isinstance(self._keypad, keypad.Keyboard)
        self._standard_passord = [1,2,3] # standard passord ved restart
        self._password = self._standard_passord # passord i bruk
        self._password_accumulator = []

    def init_passcode_entry(self): # Calls LED Boards power up method
        self._led_board.power_up()

    def get_next_signal(self): # return override-signal or get next keypress from keypad
        self._keypad.get_next()

    def verify_login(self): # check user-entered password with correct password (in a file)
        '''
        n = lengden til satt passord.
        m = lengden på totalt antall signal sendt til password_accumulator
        sjekker om de n siste tallene i password_accumulator er lik passowrd

        return True or False
        '''
        n = len(self._password)
        m = len(self._password_accumulator)
        if n < m and self._password_accumulator[m-n:] == self._password:
            self.reset_password_accumulator()
            return True

        return False

    def validate_passcode_change(self): # check that newly-entered password is legal
        # går ut ifar at password_accumulator var tom, når passowrdet ble skrevet
        self._password = self._password_accumulator


    # -----LedBoard Methods-----
    def light_one_led(self, led_id): # Call LED boards light_led method
        assert isinstance(self._led_board, led_board.LedBoard)
        self._led_board.light_led(led_id)

    def flash_leds(self, seconds): # call LED boards flash_all_leds method
        self._led_board.flash_all_leds(seconds)

    def twinkle_leds(self, seconds): # call LED boards twinkle all leds
        self._led_board.twinkle_all_leds(seconds)

    def exit_action(self): # Call LED boards power down method
       self._led_board.power_down()

    # -----FSM Methods-----
    def reset_password_accumulator(self): # resets input accumulaor
        self._password_accumulator = []

    def append_next_password_digit(self, signal): # appends signal to password acuumulator
        assert isinstance(signal, str)
        self._password_accumulator.append(signal)

    def verify_password(self):
        self.verify_login()
    def reset_agent(self):
        self.reset_password_accumulator()
        self._password = self._standard_passord

    def fully_activate_agent(self):
        assert NotImplementedError
        # svare på om passwordet stemmer eller ikke


