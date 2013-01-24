# -*- encoding: utf-8 -*-
import smbus

GO_TO_RGB = 0x6e
FADE_TO_RGB = 0x63
FADE_TO_HSB = 0x68
FADE_TO_RANDOM_RGB = 0x43
FADE_TO_RANDOM_HSB = 0x48
PLAY_LIGHT_SCRIPT = 0x70
STOP_SCRIPT = 0x6f
SET_FADE_SPEED = 0x66
SET_TIME_ADJUST = 0x74
GET_CURRENT_RGB = 0x67
WRITE_SCRIPT_LINE = 0x57
READ_SCRIPT_LINE = 0x52
SET_SCRIPT_LENGTH_AND_REPEATS = 0x4c
SET_BLINKM_ADDRESS = 0x41
GET_BLINKM_ADDRESS = 0x61
GET_BLINKM_FIRMWARE_VERSION = 0x5a
SET_STARTUP_PARAMETERS = 0x42


class Scripts:
    """Default BlinkM Scripts Reference."""
    STARTUP = 0
    RGB = 1
    WHITE_FLASH = 2
    RED_FLASH = 3
    GREEN_FLASH = 4
    BLUE_FLASH = 5
    CYAN_FLASH = 6
    MAGENTA_FLASH = 7
    YELLOW_FLASH = 8
    BLACK = 9
    HUE_CYCLE = 10
    MOOD_LIGHT = 11
    VIRTUAL_CANDLE = 12
    WATER_REFLECTIONS = 13
    OLD_NEON = 14
    THE_SEASONS = 15
    THUNDERSTORM = 16
    STOP_LIGHT = 17
    MORSE_CODE = 18


class I2C:
    """I2C Connection Manager

    :param bus: I2C Bus
    :param addr: I2C address  

    """
    def __init__(self, bus=1, addr=0x09):
        self.bus = smbus.SMBus(bus)
        self.addr = addr

    def _write_bytes(self, *bytes):
        """Write bytes at I2C address."""
        for byte in bytes:
            self.bus.write_byte(self.addr, byte)

    def _read_bytes(self, nb_bytes=1):
        """Read bytes at I2C address

        :param nb_bytes: Number of bytes to read

        """
        for i in range(nb_bytes):
            yield self.bus.read_byte(self.addr)


class BlinkM(I2C):
    """Drop dead simple BlinkM control.

    :param bus: I2C Bus
    :param addr: I2C address

    """
    def reset(self):
        """Stop script and fade to black."""
        self.stop_script()
        self.fade_to()

    def stop_script(self):
        """Stop playing script."""
        self._write_bytes(STOP_SCRIPT)

    def go_to(self, r=0, g=0, b=0):
        """Go to RGB Color Now."""
        self._write_bytes(GO_TO_RGB, r, g, b)

    def go_to_hex(self, hex_color):
        """Go to Hexadecimal Color Now."""
        r, g, b = tuple(ord(c) for c in hex_color.decode('hex'))
        self.go_to(r, g ,b)

    def fade_to(self, r=0, g=0, b=0):
        """Fade to RGB Color."""
        self._write_bytes(FADE_TO_RGB, r, g, b)

    def fade_to_hex(self, hex_color):
        """Fade to Hexadecimal Color."""
        r, g ,b = tuple(ord(c) for c in hex_color.decode('hex'))
        self.fade_to(r, g, b)

    def fade_to_hsb(self, h=0, s=0, b=0):
        """Fade to HSB Color.

        :param h: Hue (0-360°)
        :param s: Saturation (0-100%)
        :param b: Brightness (0-100%)

        """
        h = h * 255 / 360
        s = s * 255 / 100
        b = b * 255 / 100
        self._write_bytes(FADE_TO_HSB, h, s, b)

    def fade_to_percent(self, percent=0):
        """Fade to color from Blue (Cold) to Red (Hot).

        Takes an input from 0-100 and convert it to HSB from 180/100/100 to 0/100/100.

        """
        h = 180 - 180 * percent / 100
        self.fade_to_hsb(h, 100, 100)

    def fade_to_random_rgb(self, r=0, g=0, b=0):
        """Fade to Random RGB Color."""
        self._write_bytes(FADE_TO_RANDOM_RGB, r, g, b)

    def play_script(self, script_number, repeat=0, start_line=0):
        """Play Light Script."""
        self._write_bytes(PLAY_LIGHT_SCRIPT, script_number, repeat, start_line)

    def set_fade_speed(self, fade_speed):
        """Set Fade Speed.

        :param fade_speed: fade speed from 1-255.

        """
        self._write_bytes(SET_FADE_SPEED, fade_speed)

    def set_time_adjust(self, adjust):
        """Set Time Adjust.

        Adjusts the playback speed of a light script.

        :param adjust: Relative adjustement between -128 and 127.

        """

    def get_rgb_color(self):
        """Get Current RGB Color.

        Returns current red, green and blue channels."""
        self._write_bytes(GET_CURRENT_RGB)
        r, g, b = self._read_bytes(3)
        return r, g ,b

