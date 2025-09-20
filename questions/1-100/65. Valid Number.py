


class Solution:
    def isNumber(self, s: str) -> bool:
        # {state: {char_type: state}}
        transitions = {
            'Start': {'digit': 'Integer', 'sign': 'Sign', 'dot': 'Dot'},
            'Sign': {'digit': 'Integer', 'dot': 'Dot'},
            'Integer': {'digit': 'Integer', 'dot': 'Fraction', 'e': 'Exponent'},
            'Dot': {'digit': 'Fraction'},
            'Fraction': {'digit': 'Fraction', 'e': 'Exponent'},
            'Exponent': {'digit': 'Exp_number', 'sign': 'Exp_sign'},
            'Exp_sign': {'digit': 'Exp_number'},
            'Exp_number': {'digit': 'Exp_number'}
        }

        valid_end_states = {'Integer', 'Fraction', 'Exp_number'}

        def get_char_type(char):
            if char.isdigit():
                return 'digit'
            if char in '+-':
                return 'sign'
            if char in 'eE':
                return 'e'
            if char == '.':
                return 'dot'
            return None

        current_state = 'Start'

        for char in s:
            char_type = get_char_type(char)
            if not char_type or char_type not in transitions[current_state]:
                return False
            current_state = transitions[current_state][char_type]

        return current_state in valid_end_states