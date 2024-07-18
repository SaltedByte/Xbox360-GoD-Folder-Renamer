import os

#Game Folder Directory
games_dir = "D:\\backups\\xb360\\games"

#Game Mapping File
mapping_file = "games_mapping.txt"

# Read the mapping file into a dictionary
mapping = {}
with open(mapping_file, 'r') as f:
    for line in f:
        original, new_name = line.strip().split('=')
        mapping[original] = new_name

# Rename the folders
for original in mapping:
    original_path = os.path.join(games_dir, original)
    new_path = os.path.join(games_dir, mapping[original])
    if os.path.exists(original_path):
        os.rename(original_path, new_path)
        print(f"Renamed {original} to {mapping[original]}")

#completed
print("Renaming completed.")
