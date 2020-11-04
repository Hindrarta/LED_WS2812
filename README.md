# LED_WS2812

Setup
-----

Connect DI Pin of WS281x to SPI - MOSI pin of your jetson. In this case I use Pin No 19

Activate SPI pin of your jetson, for more information follow this link
https://docs.nvidia.com/jetson/l4t/index.html#page/Tegra%20Linux%20Driver%20Package%20Development%20Guide/hw_setup_jetson_io.html

Install neopixel-spi package

```bash
pip3 install adafruit-circuitpython-neopixel-spi
```

for more information about this package follow this link
https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel_SPI