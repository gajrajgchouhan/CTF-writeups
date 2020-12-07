with open('file') as h:
    data = h.read().strip()

data = list(data)

median = lambda x : len(x)//2 + (0 if len(x)%2==1 else -1)

# dummy data

dummy = list(range(len(data)))

def encode(data):
    encrypted = []

    while data:
        index = median(data)
        encrypted.append(data[index])
        del data[index]

    return encrypted

encrypted_dummy = encode(dummy)

d = dict(zip(encrypted_dummy, data))
original = [None]*len(data)

for k, v in d.items():
    original[k] = v

print("".join(original))
# b00t2root{@The_Director_is_the_bot}