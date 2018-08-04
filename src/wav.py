import pathlib
import time

DIR = 'wav'

begin = 0
end = 0
cnt = 0

with open('data.win', 'rb') as f:
    d = f.read()

pathlib.Path(f'{DIR}').mkdir(parents=True, exist_ok=True)

while True:
    begin = d.find(b'WAVEfmt', end)

    if begin == -1:
        break

    end = d.find(b'WAVEfmt', begin + 1)

    cnt += 1
    
    v1 = begin - 8
    v2 = None if end == -1 else end - 8

    with open(f'{DIR}/{str(cnt).zfill(4)}.wav', 'wb') as f:
        f.write(d[v1:v2])
