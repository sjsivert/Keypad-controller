from FSM import *


def signal_is_digit(signal): return 48 <= ord(signal) <= 57


def signal_is_any(signal): return True


def signal_is_asterisk(signal): return ord(signal) == 42


def main():
    fsm = FSM()
    rule1 = Rule("s0", "s1", signal_is_any, "KPC.reset_password_accumulator")
    fsm.add_rule(rule1)
    rule2 = Rule("s1", "s1", signal_is_digit, "KPC.append_next_password_digit")
    fsm.add_rule(rule2)
    rule3 = Rule("s1", "s2", signal_is_asterisk, "KPC.verify_password")
    fsm.add_rule(rule3)
    rule4 = Rule("s1", "s0", signal_is_any, "KPC.reset_agent")

    fsm.main_loop()

if __name__ == '__main__':
    main()
