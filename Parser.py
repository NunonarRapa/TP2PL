# Parser.py
import sys
import random
import ply.yacc as yacc
from Lexer import Lexer
from Change import Change

note = [60, 16]


class Parser:
    tokens = Lexer.tokens

    def __init__(self):
        self.parser = None
        self.lexer = None
        self.vars = {}

    def Parse(self, input, **kwargs):
        self.lexer = Lexer()
        self.lexer.Build(input, **kwargs)
        self.parser = yacc.yacc(module=self, **kwargs)
        program = self.parser.parse(lexer=self.lexer.lexer)
        Change.exec(program, self)

    def p_error(self, t):
        print("Please write some 'code' with the following:"
              "\nPlay note: '.'"
              "\nPause: '*'"
              "\nUp half tone: '^'"
              "\nDown half tone: '_'"
              "\nDouble note duration: '>'"
              "\nHalf note duration: '>'"
              "\nAttach note to the next one: '~'"
              "\nMake a chord: ':'")
        exit(1)

    def p_program0(self, p):
        """  program  :  change  """
        p[0] = [p[1]]

    def p_program2(self, p):
        """  program  :  program change  """
        lst = p[1]
        lst.append(p[2])
        p[0] = lst

    def p_change0(self, p):
        """  change  :  '.'
                     |  '.' '~'
                     |  '~' change  """
        if len(p) == 2:
            p[0] = Change(".", 1)
        elif p[2] == ".":
            p[0] = Change("~", {"num": 1})
        else:
            p[0] = Change("~", {"num": 2})

    def p_change1(self, p):
        """  change  :  '^'
                     |  '^' '{' INT '}'  """
        if len(p) == 2:
            p[0] = Change("^", {"var": 1})
        else:
            p[0] = Change("^", {"var": int(p[3])})

    def p_change2(self, p):
        """  change  :  '_'
                     |  '_' '{' INT '}'  """
        if len(p) == 2:
            p[0] = Change("_", {"var": 1})
        else:
            p[0] = Change("_", {"var": int(p[3])})

    def p_change3(self, p):
        """  change  :  ':'  """
        p[0] = Change(":", 1)

    def p_change4(self, p):
        """  change  :  '>'  """
        p[0] = Change(">", {"var": 1})

    def p_change5(self, p):
        """  change  :  '<' """
        p[0] = Change("<", {"var": 1})

    def p_change_7(self, p):
        """  change  :  '*'  """
        p[0] = Change("*", 1)