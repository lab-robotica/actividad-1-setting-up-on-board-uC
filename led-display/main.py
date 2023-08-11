from gpiozero import LED
import time


if __name__ == "__main__":
    mi_led = LED(17)

    times = 3

    for i in range(3):
        print(f"Blinking {i + 1} time(s)")
        mi_led.on()
        time.sleep(0.3)
        mi_led.off()
        time.sleep(0.3)
