import pygame.midi as pm
import time

pm.init()
player = pm.Output(0)
player.set_instrument(0, 1)

note_to_num = {
    'C': 0,
    'C#': 1,
    'D': 2,
    'D#': 3,
    'E': 4,
    'F': 5,
    'F#': 6,
    'G': 7,
    'G#': 8,
    'A': 9,
    'A#': 10,
    'B': 11,
}


def play_notes(note, cf):
    player.note_on(note, 127)
    player.note_on(cf, 127)
    time.sleep(1.23)
    player.note_off(note, 127)
    player.note_off(cf, 127)


def play_sequence(seq, cf):
    for s, c in zip(seq, cf):
        if len(s) > 2:
            snote = note_to_num[s[0:2]] + (int(s[2:3]) + 1) * 12
        else:
            snote = note_to_num[s[0:1]] + (int(s[1:2]) + 1) * 12

        if len(c) > 2:
            cnote = note_to_num[c[0:2]] + (int(c[2:3]) + 1) * 12
        else:
            cnote = note_to_num[c[0:1]] + (int(c[1:2]) + 1) * 12

        play_notes(snote, cnote)


# test_sequence = ['D3', 'D3', 'E3', 'F3', 'E3', 'D3', 'C3', 'B2', 'A2', 'C#3', 'D3']
# test_cf = ['D4', 'F4', 'E4', 'D4', 'G4', 'F4', 'A4', 'G4', 'F4', 'E4', 'D4']
#
# ali_a = ['F4', 'F4', 'C#4', 'C4', 'C4', 'G#3', 'C4', 'C4', 'G#3', 'F3', 'F3']
#
# play_sequence(test_sequence, test_cf)

del player
pm.quit()
