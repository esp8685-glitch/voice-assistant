from machine import I2S
from machine import Pin

mic = I2S(
    0,
    sck=Pin(4),
    ws=Pin(5),
    sd=Pin(6),
    mode=I2S.RX,
    bits=16,
    format=I2S.MONO,
    rate=16000,
    ibuf=40000
)

def record(seconds=3):

    size = 32000 * seconds

    buf = bytearray(size)

    mic.readinto(buf)

    return buf