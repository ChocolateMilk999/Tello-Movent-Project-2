from djitellopy import Tello
from time import sleep

tello = Tello()


tello.connect()
tello.take_off()


sleep(2)
tello.move_up(106)


sleep(2)
tello.move_forward(304)

sleep(2)
tello.move_left(304)

sleep(2)
tello.move_backwards(304)

sleep(2)
tello.move_right(304)


sleep(2)
tello.flip_back()


sleep(2)
tello.land()
