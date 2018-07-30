import pathlib
import time

DIR = 'TXTR'

begin = time.time()

with open('data.win', mode='rb') as f:
    d = f.read()

idx = 0 #d.find(b'TXTR')
cnt = -1

pathlib.Path(f'{DIR}').mkdir(parents=True, exist_ok=True)

while d[idx:idx+4] != b'AUDO':
    if d[idx:idx+16] == b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR': # PNG Header
        p = idx
        idx += 16
        cnt += 1

        while d[idx:idx+8] != b'IEND\xaeB`\x82': # PNG Footer
            idx += 1
        idx += 8

        with open(f'{DIR}/{str(cnt).zfill(4)}.png', mode='wb') as f:
            f.write(d[p:idx])
    else:
        idx += 1

end = time.time()

print(f"Time: {end - begin:.3f}s")
