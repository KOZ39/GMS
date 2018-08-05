from pathlib import Path

DIR = 'png'

begin = 0
end = 0
cnt = 0

with open('data.win', 'rb') as f:
    d = f.read()

Path(DIR).mkdir(parents=True, exist_ok=True)

while True:
    begin = d.find(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR', end + 1)

    if begin == -1:
        break

    end = d.find(b'IEND\xaeB`\x82', begin + 1)

    cnt += 1

    with open(f'{DIR}/{str(cnt).zfill(4)}.png', 'wb') as f:
        f.write(d[begin:end])
