import os
import sys
from pathlib import Path

del sys.argv[0]

if len(sys.argv) > 0:
    for argv in sys.argv:
        if os.path.isfile(argv):
            with open(argv, 'rb') as f:
                data = f.read()

            dir = os.path.join(os.path.dirname(argv), os.path.basename(argv).split('.')[0])

            Path(dir).mkdir(parents=True, exist_ok=True)

            start = stop = cnt = 0

            wavNames = []

            while True:
                stop = data.find(b'.wav', stop + 1)
                
                if stop == -1:
                    stop = 0
                    break

                start = data.rfind(b'\x00', 0, stop)

                wavNames.append(data[start+1:stop+4])

            while stop != len(data):
                start = data.find(b'RIFF', stop)

                stop = data.find(b'RIFF', start + 1)

                if stop == -1:
                    stop = len(data)

                cnt += 1

                if wavNames:
                    with open(f'{dir}/{wavNames[cnt].decode()}', 'wb') as f:
                        f.write(data[start:stop])
                else:
                    with open(f'{dir}/{str(cnt).zfill(4)}.wav', 'wb') as f:
                        f.write(data[start:stop])
