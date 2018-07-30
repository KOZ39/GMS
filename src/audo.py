import pathlib
import time

DIR = 'AUDO'

begin = time.time()

with open('data.win', mode='rb') as f:
    d = f.read()

idx = d.find(b'AUDO')
cnt = 0

pathlib.Path(f'{DIR}').mkdir(parents=True, exist_ok=True)

while idx != len(d):
    if d[idx:idx+7] == b'WAVEfmt':
        p = idx - 8
        idx += 7
        cnt += 1

        while idx != len(d):
            if d[idx:idx+7] == b'WAVEfmt':
                idx -= 8
                break

            idx += 1

        with open(f'{DIR}/{str(cnt).zfill(4)}.wav', mode='wb') as f:
            f.write(d[p:idx])
    else:
        idx += 1

end = time.time()

print(f"Time: {end - begin:.3f}s")
