def on_gesture_shake():
    basic.show_number(randint(0, 10))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
