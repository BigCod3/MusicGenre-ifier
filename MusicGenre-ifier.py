import os
import time
import json
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



# Set the path to your folder
folder_path = "<CHANGE ME>"

# Website I used to gather genres
website_url = 'https://www.chosic.com/music-genre-finder/'


# Configure the webdriver with the specified path
driver = uc.Chrome()
actions = ActionChains(driver)
# Used when waiting for bot_check and waiting for song results after a search
# Currently set for 2 minutes (120 seconds), this could be whatever you want. 
wait = WebDriverWait(driver, 120)
music_list = []
music_dict = {}
genre_dict = {}
c=1

# Check to see if we have previous progress from a crash
try:
    with open('music_dict.json', 'r') as f:
        music_dict = json.load(f)
except:
    print('No previous music data found.')

# Iterate through the files in the folder
try:
    for filename in os.listdir(folder_path):
        # Create the full file path
        file_path = os.path.join(folder_path, filename)

        # Extract the file name without the extension

        file_name = os.path.splitext(filename)[0]
        if file_name not in music_dict:
            music_list.append(file_name)
    for file_name in music_list:
        # Open the website in the browser
        driver.get(website_url)
        # Cloudflare bot detection may appear at times, this waits until it goes away.
        bot_check = wait.until(EC.title_contains("Music Genre Finder"))
        try:
            # Find the text box element on the website
            text_box = driver.find_element(By.ID, 'search-word')  # Replace 'textbox-id' with the actual ID of the text box element
            # Enter the file name into the text box
            text_box.send_keys(file_name)
            time.sleep(4)
            first_song_check = wait.until(EC.text_to_be_present_in_element_attribute((By.XPATH, '//*[@id="hh1"]'),"data-id", "1"))
            first_song = driver.find_element(By.XPATH, '//*[@id="hh1"]')
            first_song.click()
            time.sleep(3)
            tags = driver.find_elements(By.XPATH, '//*[@id="spotify-tags"]/div/div[2]/a')
            genres = [genre.text for genre in tags]
            music_dict[file_name] = genres
            print(f"Finished song #{c} - {file_name}")
            c+=1

        except:
            print(f"Failed on song: {file_name}")
            c+=1

    # Iterate over the music_dict
    for song, genres in music_dict.items():
        # For each song, iterate over its genres
        for genre in genres:
            # If the genre is already a key in the genre_dict, append the song to its list
            if genre in genre_dict:
                genre_dict[genre].append(song)
            # If the genre is not a key in the genre_dict, initialize a new list for it with the current song
            else:
                genre_dict[genre] = [song]

            # Write the song to the corresponding genre's M3U file
            with open(f"{folder_path}/{genre}.m3u", "a") as f:
                f.write(song + ".mp3" + "\n")  # Replace 'song' with the full path to the song file if necessary

    # Convert the genre_dict to a list of tuples (genre, number of songs)
    genre_list = [(genre, len(songs)) for genre, songs in genre_dict.items()]

    # Sort the list in descending order based on the number of songs
    genre_list.sort(key=lambda x: x[1], reverse=True)

    # Print the sorted list
    for genre, count in genre_list:
        print(f"{genre}: {count} songs")
except Exception as e:
    print("An error occurred. Saving progress...")
    with open('music_dict.json', 'w') as f:
        json.dump(music_dict, f)
    print(f"Error: {e}")
finally:
    # Close the browser
    driver.quit()
