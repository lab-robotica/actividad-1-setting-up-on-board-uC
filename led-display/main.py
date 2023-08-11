from gpiozero import LED
import time


if __name__ == "__main__":
    mi_led = LED(17)
    try: 
        print("Turning on led")
        mi_led.on()
        input("Click enter to turn it off")
    except KeyboardInterrupt: 
        pass

    print("Turning off led")
    mi_led.off()
