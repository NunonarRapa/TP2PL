# main.py
from Parser import Parser
import Change

with open("test0.pst", mode="r") as fh:
    contents = fh.read()

parser = Parser()
parser.Parse(contents)
Change.midi.update_time(0)
Change.midi.end_of_track()