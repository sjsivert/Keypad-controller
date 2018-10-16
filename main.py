from FSM import *
from KPC import *
from proxy import *


def signal_is_digit(signal): return 48 <= ord(signal) <= 57


def signal_is_1_6_digit(signal): return 49 <= ord(signal) <= 54


def signal_is_any(signal): return True


def main():

    kpc = KPC(ProxyKeypad(), ProxyLedBoard())
    kpc.init_passcode_entry()

    fsm = FSM(kpc)

    rule_1 = Rule("s0", "s1", signal_is_any, KPC.reset_password_accumulator)
    fsm.add_rule(rule_1)
    rule_2 = Rule("s1", "s1", signal_is_digit, KPC.append_next_password_digit)
    fsm.add_rule(rule_2)
    rule_3 = Rule("s1", "s2", "*", KPC.verify_login)
    fsm.add_rule(rule_3)
    rule_4 = Rule("s1", "s0", signal_is_any, KPC.reset_agent)
    fsm.add_rule(rule_4)
    rule_5 = Rule("s2", "s3", "Y", KPC.fully_activate_agent)
    fsm.add_rule(rule_5)
    rule_6 = Rule("s2", "s0", signal_is_any, KPC.reset_agent)
    fsm.add_rule(rule_6)
    rule_7 = Rule("s3", "s6", signal_is_1_6_digit, KPC.select_led)
    fsm.add_rule(rule_7)
    rule_8 = Rule("s6", "s7", "*", KPC.verify_led_select)
    fsm.add_rule(rule_8)
    rule_9 = Rule("s6", "s3", signal_is_any, KPC.reset_agent)
    fsm.add_rule(rule_9)
    rule_10 = Rule("s7", "s7", signal_is_digit, KPC.append_next_time_digit)
    fsm.add_rule(rule_10)
    rule_11 = Rule("s7", "s3", "*", KPC.light_selected_led)
    fsm.add_rule(rule_11)
    rule_12 = Rule("s7", "s3", signal_is_any, KPC.refresh_agent)
    fsm.add_rule(rule_12)
    rule_13 = Rule("s3", "s4", "*", KPC.reset_password_accumulator)
    fsm.add_rule(rule_13)
    rule_14 = Rule("s4", "s4", signal_is_digit, KPC.append_next_password_digit)
    fsm.add_rule(rule_14)
    rule_15 = Rule("s4", "s5", "*", KPC.cache_1st_password)
    fsm.add_rule(rule_15)
    rule_16 = Rule("s4", "s3", signal_is_any, KPC.refresh_agent)
    fsm.add_rule(rule_16)
    rule_17 = Rule("s5", "s5", signal_is_digit, KPC.append_next_password_digit)
    fsm.add_rule(rule_17)
    rule_18 = Rule("s5", "s3", "*", KPC.verify_new_password)
    fsm.add_rule(rule_18)
    rule_19 = Rule("s5", "s3", signal_is_any, KPC.refresh_agent)
    fsm.add_rule(rule_19)
    rule_20 = Rule("s3", "s8", "#", KPC.shutdown_attempt)
    fsm.add_rule(rule_20)
    rule_21 = Rule("s8", "s0", "#", KPC.exit_action)
    fsm.add_rule(rule_21)
    rule_22 = Rule("s8", "s3", signal_is_any, KPC.refresh_agent)
    fsm.add_rule(rule_22)

    fsm.main_loop()


if __name__ == '__main__':
    main()
