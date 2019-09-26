import sys


class dfa:
    ''' 
    This class will check strings against a defined DFA and return a nice representation of the DFA
    '''

    def __init__(self, states, alphabet, transitions, start_state, accepting_states):
        self.states = states 
        self.alphabet = alphabet
        self.transitions = transitions if self._recursively_check_validity(self.states, transitions) else None
        self.start_state = start_state if self._check_validity(self.states, start_state) else None
        self.accepting_states = accepting_states if self._recursively_check_validity(self.states, accepting_states) else None


    def _check_validity(self, states, test_state):
        return test_state in states


    def _recursively_check_validity(self, states, values):
        if type(values) != list:
            sys.exit('Transistions not specified correctly. Provide transitions as a list.')
        if values == []:
            return True
        if type(values[0]) == tuple:
            test_transition = values[0]
            _start = test_transition[0]
            _end = test_transition[2]
            return (_start in states) and (_end in states) and self._recursively_check_validity(states, values[1:])
        else:
            return (values[0] in states) and self._recursively_check_validity(states, values[1:])


    def __repr__(self):
        output_str = ''
        for variable in [self.states, self.alphabet, self.transitions, self.start_state, self.accepting_states]:
            output_str += str(f'{variable}\n') if variable != None else sys.exit(f'{variable} is Nonetype. Check given value.')
        return output_str


    def accepts(self, lang_string):

        def _recursively_check_string(self, lang_string, curr_state):

            if len(lang_string) == 0:
                return True if curr_state in self.accepting_states else False
 
            next_state = None
            next_char = lang_string[0]
            for transition in self.transitions:
                _start = transition[0]
                _char = transition[1]
                _end = transition[2]
                if curr_state == _start and next_char == _char:
                    next_state = _end
                    break

            return _recursively_check_string(self, lang_string[1:], next_state) if next_state else False
                

        if type(lang_string) != str:
            sys.exit('Given string is not of valid type. Please Enter a str.')
        return _recursively_check_string(self, lang_string, self.start_state)
        

def _test():
    DFA = dfa(['1', '2', '3'], ['a','b'], [('1', 'a', '2'), ('2', 'b', '3'), ('3', 'a', '1')], '1', ['3'])
    print(repr(DFA))
    print('Test String: ab')
    print(DFA.accepts('ab'))

    DFA = dfa(['1', '2', '3'], ['a','b'], [('1', 'a', '2'), ('2', 'b', '3'), ('3', 'a', '1')], '1', ['3'])
    print(repr(DFA))
    print('Test String: ba')
    print(DFA.accepts('ba'))

    DFA = dfa(['1', '2', '3'], ['a','b'], [('1', 'a', '2'), ('2', 'b', '3'), ('3', 'a', '1')], '1', ['3'])
    print(repr(DFA))
    print('Test String: a')
    print(DFA.accepts('a'))


if __name__ == '__main__':
    _test()