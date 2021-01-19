# Change.py
from mxm.midifile import MidiOutFile

note = [60, 16]
outfile = open("filegenerated.mid", "wb")
midi = MidiOutFile(outfile)
midi.header(format=0, nTracks=1, division=32)
midi.start_of_track()
auxNote = note[0]


def def_auxNote(nota):
    auxNote = nota


def ret_auxNote():
    return auxNote


def do_playTone(change, parser):
    midi.update_time(0)
    midi.note_on(channel=0, note=note[0])
    midi.update_time(note[1])
    midi.note_off(channel=0, note=note[0])


def do_toneUp(change, parser):
    note[0] = int(note[0] + change.args['var'])


def do_toneDown(change, parser):
    note[0] = int(note[0] - change.args['var'])


def do_pause(change, parser):
    midi.update_time(0)
    midi.note_on(channel=0, note=0)
    midi.update_time(note[1])
    midi.note_off(channel=0, note=0)


def do_chord(change, parser):
    midi.note_on(channel=0, note=note[0])  # original
    midi.note_on(channel=0, note=note[0] + 4)  # original + 4
    midi.note_on(channel=0, note=note[0] + 7)  # original + 7
    midi.update_time(note[1])
    midi.note_off(channel=0, note=note[0])  # original
    midi.note_off(channel=0, note=note[0] + 4)  # original + 4
    midi.note_off(channel=0, note=note[0] + 7)  # original + 7
    midi.update_time(0)


def do_durationUp(change, parser):
    if note[1] == 64:
        print("Please don't try such a long duration")
        exit()
    note[1] = int(note[1] * 2)


def do_durationDown(change, parser):
    if note[1] == 1:
        print("Please don't try such a short duration")
        exit()
    note[1] = int(note[1] / 2)


def do_attachTone(change, parser):
    if change.args['num'] == 1:
        def_auxNote(note[0])
        midi.note_on(channel=0, note=ret_auxNote())
    else:
        midi.note_on(channel=0, note=note[0])
        midi.update_time(note[1])
        midi.note_off(channel=0, note=ret_auxNote())
        midi.note_off(channel=0, note=note[0])


class Change:
    # Dispatch Table!
    dispatch_table = {
        ".": do_playTone,
        "*": do_pause,
        "^": do_toneUp,
        "_": do_toneDown,
        ":": do_chord,
        ">": do_durationUp,
        "<": do_durationDown,
        "~": do_attachTone
    }

    def __init__(self, change, args):
        self.name = change
        self.args = args

    def __repr__(self):
        return f"Change({self.name}, {self.args})"

    def play(self, parser):
        self.dispatch_table[self.name](self, parser)

    @classmethod
    def exec(cls, program, parser):
        for change in program:
            change.play(parser)
