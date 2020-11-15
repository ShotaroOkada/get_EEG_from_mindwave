import thinkgear
from setting import MINDWAVE_PORT
import csv
from datetime import datetime, time

PORT = MINDWAVE_PORT

with open('data/new.csv', 'w') as csvfile:
    w = csv.writer(csvfile, lineterminator='\n')

    for packets in thinkgear.ThinkGearProtocol(PORT).get_packets():
        for p in packets:
            if isinstance(p, thinkgear.ThinkGearRawWaveData):
                print p
                now = datetime.now().time()
                w.writerow([now.isoformat(), p])
            else:
                continue
