class ProxyKeypad:

    def get_next(self):
        return input("input: ")


class ProxyLedBoard:

    def turn_on_led(self, led_number):
        print("Turning on led", led_number)

    def turn_off_leds(self):
        print("Turning off leds")

    def light_led(self, led_number, seconds):
        print("Turns on led", led_number, "for", seconds, "seconds")

    def flash_all_leds(self, seconds):
        print("Flashing all leds for", seconds, "seconds")

    def twinkle_all_leds(self, seconds):
        print("Twinkle all leds for", seconds, "seconds")

    def random_blink(self, seconds):
        print("Lights up random leds for", seconds, "seconds")

    def power_up(self):
        print("Power up led-board")

    def power_down(self):
        print("Power down led-board")
