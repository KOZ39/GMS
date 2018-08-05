from pathlib import Path

DIR = 'wav'

begin = 0
end = 0
cnt = 0

wavNames = []

with open('data.win', 'rb') as f:
    d = f.read()

Path(DIR).mkdir(parents=True, exist_ok=True)

while True:
    end = d.find(b'.wav', end + 1)
    
    if end == -1:
        end = 0
        break

    begin = d.rfind(b'\x00', 0, end)

    v1 = begin + 1
    v2 = end + 4

    wavNames.append(d[v1:v2])

while True:
    begin = d.find(b'WAVEfmt', end)

    if begin == -1:
        break

    end = d.find(b'WAVEfmt', begin + 1)

    cnt += 1
    
    v1 = begin - 8
    v2 = None if end == -1 else end - 8

    if wavNames:
        with open(f'{DIR}/{wavNames[cnt].decode("utf-8")}', 'wb') as f:
            f.write(d[v1:v2])
    else:
        with open(f'{DIR}/{str(cnt).zfill(4)}.wav', 'wb') as f:
            f.write(d[v1:v2])
