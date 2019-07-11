import pew
import random
import time

HAND_PIXELS = [
    # 0, 1, 2
    [(0,0), (1,1), (2,2), (3,3)],
    [(2,0), (2,1), (3,2), (3,3)],
    [(5,0), (5,1), (4,2), (4,3)],
    # 3, 4, 5
    [(7,0), (6,1), (5,2), (4,3)],
    [(7,2), (6,2), (5,3), (4,3)],
    [(7,5), (6,5), (5,4), (4,4)],
    # 6, 7, 8
    [(7,7), (6,6), (5,5), (4,4)],
    [(5,7), (5,6), (4,5), (4,4)],
    [(2,7), (2,6), (3,5), (3,4)],
    # 9, 10, 11
    [(0,7), (1,6), (2,5), (3,4)],
    [(0,5), (1,5), (2,4), (3,4)],
    [(0,2), (1,2), (2,3), (3,3)],
]


def enable_hand(screen, hand_id, color=1):
    for p in HAND_PIXELS[hand_id]:
        screen.pixel(p[0], p[1], color)

def disable_hand(screen, hand_id):
    enable_hand(screen, hand_id, 0)
    

def loop():
    screen = pew.Pix()

    # Run until user input
    while not pew.keys():
        current_time = time.localtime()
        h = current_time[3] % 12
        m = current_time[4] // 5
        s = current_time[5] // 5

        # Paint pixels
        enable_hand(screen, h, 1)
        enable_hand(screen, m, 2)
        enable_hand(screen, s, 3)

        # Update display
        pew.show(screen)
        # Wait until next iteration
        pew.tick(1/2)

        # Clear pixels
        disable_hand(screen, h)
        disable_hand(screen, m)
        disable_hand(screen, s)
        

pew.init()
loop()
