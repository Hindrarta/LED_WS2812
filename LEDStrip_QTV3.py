# import time
import board
import neopixel_spi as neopixel

class LEDStrip():
	def __init__(
		self, numPixel=None, pixelOrder=None, 
		notifPixel=None, flashPixelR=None, flashPixelL=None
		):
		if numPixel == None:
			self.numPixel = 8
		else:
			self.numPixel = numPixel

		if(pixelOrder == 'GRB'):
			self.pixelOrder = neopixel.RGB
		else:
			self.pixelOrder = neopixel.GRB

		
		try:
			self.spi = board.SPI()	# SPI MOSI - PIN 19
		except Exception as e:
			print("Exception occured : ",e)

		self.notifPixel = notifPixel
		self.flashPixelR = flashPixelR
		self.flashPixelL = flashPixelL
		self.lenNotifPixel = len(range(numPixel)[self.notifPixel])
		self.lenFlashPixelR = len(range(numPixel)[self.flashPixelR])
		self.lenFlashPixelL = len(range(numPixel)[self.flashPixelL])

		try:
			self.pixels = neopixel.NeoPixel_SPI(
				self.spi, self.numPixel, pixel_order = self.pixelOrder, auto_write=False
			)
		except Exception as e:
			print("Exception occured : ",e)


	def checkRGB(self, val):
		if val < 0:
			return 0
		elif val > 255:
			return 255
		else:
			return val

	def fromRGB(self, Red, Grn, Blu):
		return Red, Grn, Blu

	def setColor(self, color, brightness = 1.0):
		if(type(color) == tuple) :
			rgb = color
		elif(type(color) == str):
			if(color == 'red'):
				rgb = self.fromRGB(255,0,0)
			elif(color == 'green'):
				rgb = self.fromRGB(0,255,0)
			elif(color == 'blue'):
				rgb = self.fromRGB(0,0,255)
			elif(color == 'orange'):
				rgb = self.fromRGB(255,128,0)
			elif(color == 'yellow'):
				rgb = self.fromRGB(255,255,0)
			elif(color == 'cyan'):
				rgb = self.fromRGB(0,255,255)
			elif(color == 'magenta'):
				rgb = self.fromRGB(255,0,255)
			elif(color == 'white'):
				rgb = self.fromRGB(255,255,255)
			elif(color == 'black'):
				rgb = self.fromRGB(0,0,0)
			else:
				rgb = self.fromRGB(0,0,0)
				print('Color not defined, use fromRGB instead')
				return
		else:
			rgb = self.fromRGB(0,0,0)
			print('color argument with undefined data type, use str or int')
			return

		R = int(rgb[0] * brightness)
		G = int(rgb[1] * brightness)
		B = int(rgb[2] * brightness)
		
		col = (((R << 8) + G) << 8) + B
		
		return col

	def setOnNotifLED(self, color, brightness = 1.0):
		
		col = self.setColor(color, brightness=brightness)

		self.pixels[self.notifPixel] = [col] * self.lenNotifPixel
		self.pixels.show()

	def setOffNotifLED(self):
		col = self.setColor('black', brightness=1.0)

		self.pixels[self.notifPixel] = [col] * self.lenNotifPixel
		self.pixels.show()

	def setOnFlashLED(self, brightness = 1.0):
		col = self.setColor('white', brightness=brightness)

		self.pixels[self.flashPixelR] = [col] * self.lenFlashPixelR
		self.pixels[self.flashPixelL] = [col] * self.lenFlashPixelL
		self.pixels.show()

	def setOffFlashLED(self):
		col = self.setColor('black', brightness=1.0)

		self.pixels[self.flashPixelR] = [col] * self.lenFlashPixelR
		self.pixels[self.flashPixelL] = [col] * self.lenFlashPixelL
		self.pixels.show()

