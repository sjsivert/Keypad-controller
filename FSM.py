from KPC import KPC
from inspect import isfunction

class Rule:

    def __init__(self, state1, state2, trigger_signal, action):
        self.state1 = state1
        self.state2 = state2
        self.trigger_signal = trigger_signal
        self.action = action

    def matching(self, FSM):
        if isfunction(self.state1) and isfunction(self.trigger_signal):
            return self.state1(FSM.current_state) and self.trigger_signal(FSM.signal)
        elif isfunction(self.trigger_signal):
            return self.state1 == FSM.current_state and self.trigger_signal(FSM.signal)
        elif isfunction(self.state1):
            return self.state1(FSM.current_state) and self.trigger_signal == FSM.signal
        else:
            return self.state1 == FSM.current_state and self.trigger_signal == FSM.signal


class FSM:

    def __init__(self):
        self.rules = []
        self.signal = None
        self.current_state = "s0"
        #self.KPC = KPC()

    def add_rule(self, rule):
        self.rules.append(rule)

    def get_next_signal(self):
        self.signal = input("input: ")

    def run_rules(self):
        for rule in self.rules:
            if rule.matching(self):
                self.fire_rule(rule)
                break

    def fire_rule(self, rule):
        self.current_state = rule.state2
        print(rule.action)

    def main_loop(self):
        while True:
            self.get_next_signal()
            self.run_rules()

