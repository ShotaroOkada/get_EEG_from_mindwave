import thinkgear
from setting import MINDWAVE_PORT
import csv
from datetime import datetime, time

PORT = MINDWAVE_PORT

with open('data/2120050/6-4.csv', 'w') as csvfile:
    w = csv.writer(csvfile, lineterminator='\n')

    for packets in thinkgear.ThinkGearProtocol("/dev/tty.MindWaveMobile-SerialPo").get_packets():
        for p in packets:
            if isinstance(p, thinkgear.ThinkGearRawWaveData):
                print p
                now = datetime.now().time()
                w.writerow([now.isoformat(), p])
            else:
                continue
