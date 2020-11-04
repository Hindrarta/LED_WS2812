import time
from LEDStrip_QTV3 import *

NUM_PIXEL = 16
PIXEL_ORDER = 'RGB'
DELAY = 0.1

NOTIF_PIXEL = slice(0,8)
FLASH_PIXEL_R = slice(8,12,2)
FLASH_PIXEL_L = slice(12,16,2)

LED = LEDStrip(NUM_PIXEL, PIXEL_ORDER, NOTIF_PIXEL, FLASH_PIXEL_R, FLASH_PIXEL_L)

CUSTOM_COLOR = (
	LED.setColor('red'),
	LED.setColor('orange'),
	LED.setColor('yellow'),
	LED.setColor('green'),
	LED.setColor('cyan'),
	LED.setColor('blue'),
	LED.setColor('magenta')
)

def main():
	LED.setOnNotifLED('yellow', brightness = 0.5)
	LED.setOffFlashLED()
	time.sleep(DELAY)

	LED.setOffNotifLED()
	LED.setOnFlashLED(brightness = 0.5)
	time.sleep(DELAY)

def custom():
	a = int(NUM_PIXEL / 2)
	for j in range(len(CUSTOM_COLOR)):
		if j+1 == len(CUSTOM_COLOR):
			r = 0
		else:
			r = j+1
			
		for i in range(a):
			LED.pixels[i] = CUSTOM_COLOR[j]
			LED.pixels[i+a] = CUSTOM_COLOR[r]
			LED.pixels.show()
			time.sleep(DELAY)


if __name__ == "__main__":
	while True:
		try:
			custom()
		except KeyboardInterrupt as k:
			break
