def on_gesture_shake():
    global Stappen
    Stappen += 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

Stappen = 0
led.stop_animation()

def on_forever():
    basic.show_number(Stappen)
basic.forever(on_forever)
