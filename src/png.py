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

            while True:
                start = data.find(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR', stop)

                if start == -1:
                    break

                stop = data.find(b'IEND\xaeB`\x82', start + 1)

                cnt += 1

                with open(f'{dir}/{str(cnt).zfill(4)}.png', 'wb') as f:
                    f.write(data[start:stop])
