# Lexer.py
import ply.lex as lex
import sys


class Lexer:
    literals = ".:[ ]={}^_~*></#"
    t_ignore = " \n\t"
    tokens = ("INT", )

    def t_INT(self, t):
        r"[0-9]+"
        t.value = int(t.value)
        return t

    def t_COMMENT(self, t):
        r".*\#.*"
        pass

    def t_error(self, t):
        print(f"Parser error. Unexpected char: {t.value[0]}", file=sys.stderr)
        exit(1)

    def __init__(self):
       self.lexer = None

    def Build(self, input, **kwargs):
       self.lexer = lex.lex(module=self, **kwargs)
       self.lexer.input(input)



