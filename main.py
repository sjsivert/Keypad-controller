from FSM import *
from KPC import *


def signal_is_digit(signal): return 48 <= ord(signal) <= 57


def signal_is_any(signal): return True


class ProxyKeypad:

    def get_next(self):
        return input("input: ")


class ProxyLedBoard:

    def turn_on_led(self, led_number):
        print("Turning on led", led_number)

    def turn_off_leds(self):
        print("Turning off leds")

    def light_led(self, led_number, seconds):
        print("Turns on", led_number, "for", seconds, "seconds")

    def flash_all_leds(self, seconds):
        print("Flashing all leds for", seconds, "seconds")

    def twinkle_all_leds(self, seconds):
        print("Twinkle all leds for", seconds, "seconds")

    def random_blink(self, seconds):
        """ Lights up random leds in sequence for the specified number of seconds """
        print("Lights up random leds for", seconds, "seconds")

    def power_up(self):
        print("Power up led-board")

    def power_down(self):
        print("Power down led-board")



def main():

    kpc = KPC(ProxyKeypad(),ProxyLedBoard())
    fsm = FSM(kpc)
    rule_1 = Rule("s0", "s1", signal_is_any, KPC.reset_password_accumulator)
    fsm.add_rule(rule_1)
    rule_2 = Rule("s1", "s1", signal_is_digit, KPC.append_next_password_digit)
    fsm.add_rule(rule_2)
    rule_3 = Rule("s1", "s2", "*", KPC.verify_login)
    fsm.add_rule(rule_3)
    rule_4 = Rule("s1", "s0", signal_is_any, KPC.reset_agent)
    fsm.add_rule(rule_4)
    rule_5 = Rule("s2", "s3", True, KPC.fully_activate_agent)
    fsm.add_rule(rule_5)
    rule_6 = Rule("s2", "s0", signal_is_any, KPC.reset_agent)
    fsm.main_loop()


if __name__ == '__main__':
    main()
