class Automata:
    def __init__(self, states:list, initial, final, transitions) -> None:
        self.states = states
        self.initial = initial
        self.final = final
        self.transitions = transitions
        return
    
    def accepts(self, cadena:str):
        current_state = self.initial
        for element in cadena:
            current_state = self.__get_next_state(current_state, element)
        return True if current_state == self.final else False

    def __get_next_state(self, current_state, element):
        return self.transitions[current_state][element]
    def match_token(self, texto:str) -> int:
        current_state = self.initial
        for element in texto:
            current_state = self.__get_next_state(current_state, element)
            if current_state == self.final:
                return texto.find(element)
        return -1
    
def compile(regex:str)->Automata:
    states = []
    transitions = []
    for i, character in range(regex.__len__()), regex:
        if character == '|':
            pass #Ejecuta el OR
        transitions.append((character, i))
    automata = Automata(states, 1, states.__len__(), transitions)
    return(automata)
