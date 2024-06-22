# 1
print('1)')
pixels = 128 * 128
print(pixels)
print(f'{pixels // 1024}kb')
print()

print('2)')
pixels = 1024 * 1024
size = 512 * 1024 * 8
size_per_pixel = size // pixels
print(f'size per pizel: {size_per_pixel} bit')
print(f'colors: {2 ** size_per_pixel}')
print()

print('3)')
pixels = 600 * 450
size = 90 * 1024 * 8
bits_per_pixel = size // pixels
print(f'{bits_per_pixel} bits per pixel')
print(f'colors: {2 ** bits_per_pixel}')
print()

print('4)')
speed = 1024_000
t = 5
size = t * speed / 1024
print(size, end='\n\n')

print('5)')
pixels = 486 * 720
size = 80 * 1024 * 8 # bits
size2 = int(size // 0.85)
size_per_pixel = size2 // pixels
print(f'size per pixel: {size_per_pixel} bits')
print(f'colors: {2 ** size_per_pixel}')
print()

print('6)')
t = 15 # s

print()