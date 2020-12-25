# Input
door_public = 13316116
key_public = 13651422

# Test
# door_public = 17807724
# key_public = 5764801

def transform(value, subject):
    value *= subject
    value %= 20201227
    return value

value = 1
loops = 0
while value != door_public:
    loops += 1
    value = transform(value, 7)
value2 = 1
loops2 = 0
while value2 != key_public:
    loops2 += 1
    value2 = transform(value2, 7)

print(f'DoorPublic: {value2} after {loops2} loops, KeyPublic: {value} after {loops} loops.')

value = 1
for _ in range(loops):
    value = transform(value, key_public)

print(value)