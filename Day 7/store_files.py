import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
files_dir = os.path.join(BASE_DIR, "images")

if not os.path.exists(files_dir):
    os.makedirs(files_dir)

my_images = range(12)

for i in my_images:
    fname = f"{i}.txt"
    file_path = os.path.join(files_dir, fname)
    if os.path.exists(file_path):
        print(f"skipped {fname}")
    else:
        with open(file_path, "w") as f:
            f.write(f"Hello world for {i}")

