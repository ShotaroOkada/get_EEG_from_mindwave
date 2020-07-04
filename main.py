import thinkgear
from setting import MINDWAVE_PORT

PORT = MINDWAVE_PORT
for packets in thinkgear.ThinkGearProtocol(PORT).get_packets():
    for p in packets:
        if isinstance(p, thinkgear.ThinkGearRawWaveData):
            continue
        print p
