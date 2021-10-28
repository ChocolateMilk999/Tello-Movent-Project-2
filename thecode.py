from djitellopy import Tello

tello = Tello()

tello.connect()
tello.take_off()

tello.move_up(106)

tello.move_forward(304)
tello.move_left(304)
tello.move_backwards(304)
tello.move_right(304)

tello.flip_back()

tello.land()
