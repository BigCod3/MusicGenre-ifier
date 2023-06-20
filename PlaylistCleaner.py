import os

# Set the path to your music folder
music_folder = "<CHANGE ME>"

# Set the minimum number of songs for a playlist to be kept
min_songs = 10  # Change this to your preference

# List to store the names of playlists to be deleted
to_delete = []

# Iterate through the files in the music folder
for filename in os.listdir(music_folder):
    # Check if the file is an M3U playlist
    if filename.endswith(".m3u"):
        # Create the full file path
        file_path = os.path.join(music_folder, filename)

        try:
            # Open the playlist file
            with open(file_path, 'r', encoding='utf-8') as f:
                # Count the number of songs in the playlist
                num_songs = len(f.readlines())
        except Exception as e:
            print(f"Could not open file {filename}. Error: {e}")
            continue

        # If the playlist has fewer songs than the minimum, add it to the deletion list
        if num_songs < min_songs:
            to_delete.append(file_path)

# Print the names of the playlists to be deleted
print("The following playlists will be deleted:")
for playlist in to_delete:
    print(playlist)

# Ask for user confirmation before deletion
confirm = input("Do you want to proceed with the deletion? (y/n): ")
if confirm.lower() == 'y':
    reconfirm = input("Are you sure? This operation cannot be undone. (y/n): ")
    if reconfirm.lower() == 'y':
        # Delete the playlists
        for playlist in to_delete:
            try:
                os.remove(playlist)
            except Exception as e:
                print(f"Could not delete file {playlist}. Error: {e}")
        print("Playlists deleted.")
    else:
        print("Deletion cancelled.")
else:
    print("Deletion cancelled.")
