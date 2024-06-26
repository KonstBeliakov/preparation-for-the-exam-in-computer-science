pixels = 2048 * 1792
colors = 65536  # 2 ** 16
n = 512

bytes_per_img = pixels * 2

print(bytes_per_img * n // (1024 ** 2))