from gpiozero import LED
from gpiozero import MotionSensor

red_led = LED(15)
pir = MotionSensor(14)
red_led.off()
while True:
    pir.wait_for_motion()
    print("Motion Detected")
    red_led.on()
    pir.wait_for_no_motion()
    red_led.off()
    print("Motion Stopped")