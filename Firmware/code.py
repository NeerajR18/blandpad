print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientationfrom
from kmk.modules.macros import Macros, Press, Release, Tap

keyboard = KMKKeyboard()
macros=Macros()
keyboard.modules.append(macros)

keyboard.col_pins = (board.D0, board.D1, board.D2)
keyboard.row_pins = (board.D6, board.D7, board.D8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

CALC = KC.MACRO(Press(KC.LGUI), Tap(KC.R), Release(KC.LGUI), KC.MACRO_SLEEP_MS(200), KC.MACRO_STRING("calc\n")
VSCODE = KC.MACRO(Press(KC.LGUI), Tap(KC.R), Release(KC.LGUI), KC.MACRO_SLEEP_MS(200), KC.MACRO_STRING("code\n"))
SPOTIFY = KC.MACRO(Press(KC.LGUI), Tap(KC.R), Release(KC.LGUI), KC.MACRO_SLEEP_MS(200), KC.MACRO_STRING("spotify:\n"))                
keyboard.keymap = [
    [KC.LCTL(KC.C), KC.LCTL(KC.V),KC.PSCR,
     KC.MPRV,KC.MPLY,KC.MNXT,
     CALC,VSCODE, SPOTIFY,]
]

if __name__ == '__main__':
    keyboard.go()