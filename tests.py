from elias_omega_codding import encode, decode
import random

# array = [5, 5]#random.randint(1, 10) for _ in range(5)]
# print(array)
#
# encoded = encode(array)
# print(encoded)
#
# decoded = decode(encoded)
# print(decoded)

for i in range(100):
    print(i, 'is started')
    array = [random.randint(1, 10) for _ in range(5)]
    print(array)
    encoded = encode(array)
    decoded = decode(encoded)
    print(decoded)
    print(encoded)
    assert array == decoded
    print(i, 'is completed')
