from FSM import *
from KPC import *


def signal_is_digit(signal): return 48 <= ord(signal) <= 57


def signal_is_any(signal): return True


def main():
    kpc = KPC()
    fsm = FSM()
    rule_1 = Rule("s0", "s1", signal_is_any, "KPC.reset_password_accumulator")
    fsm.add_rule(rule_1)
    rule_2 = Rule("s1", "s1", signal_is_digit, "KPC.append_next_password_digit")
    fsm.add_rule(rule_2)
    rule_3 = Rule("s1", "s2", "*", "KPC.verify_password")
    fsm.add_rule(rule_3)
    rule_4 = Rule("s1", "s0", signal_is_any, "KPC.reset_agent")
    fsm.add_rule(rule_4)
    rule_5 = Rule("s2", "s3", "Y", "KPC.fully_activate_agent")
    fsm.add_rule(rule_5)
    rule_6 = Rule("s2", "s0", signal_is_any, "KPC.reset_agent")
    fsm.main_loop()


if __name__ == '__main__':
    main()
