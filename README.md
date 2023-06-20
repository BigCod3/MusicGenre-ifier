# MusicGenre-ifier
Small program I made with the help of chatGPT to create genre specific playlists(m3u files) from local files to use when DJing. Pretty slow and not perfect but gets the job done.

I would ensure the software you plan to use the playlists in can support m3u files, if not, you can modify the file extension within the code itself here: 

![image](https://github.com/BigCod3/MusicGenre-ifier/assets/101913888/9329fe31-8e7d-4e98-8eec-72f5b12be0fe)



# To run
Could probably work as standalone programs if you have python installed but I find its best to run within VSCode.
Make sure you change the folder_path to match your music folder in each file. **Make sure to change backslashes to forward slashes as seen in this picture:**

![image](https://github.com/BigCod3/MusicGenre-ifier/assets/101913888/fe04f6db-ef5e-4412-b135-460ab8fdcc67)


Next you'll want to run the program using VSCode's interactive window:

![image](https://github.com/BigCod3/MusicGenre-ifier/assets/101913888/b90b3cfd-18fa-4d95-8a19-89582a8f5687)

# Next step
Patience. This process takes a while for a couple reasons,
- We have to wait for results to generate before we click on something
- We also have to wait for the page to load **after** clicking something
- Waiting for bot check page to pass, I'd say about 90% of the time during my use, this automatically went away. In rare cases you may have to click on the "Am I a human" box to ensure the program continues running.
- This took roughly 3-4 hours to go through ~750 songs. Part of this time was troubleshooting the program itself though, so time will vary.
- When this is finished, you'll get an output of each genre and how many songs are in each one. Use this to determine the minimum number of songs you'd like to keep in your playlists in the next step.

You can pretty much run this in the background while working on something else, however if the bot_check page asks for human input and you don't enter within 2 minutes the program will exit.
The progress should be saved in this event under the file 'music_dict.json'. Then when the program runs again, it will check this file to resume progress.

# PlaylistCleaner
This is a seperate program that will **remove** any playlists that have **less than** 10 songs by default. 
I have tested this on my own system a couple times but **PLEASE** backup your files first. Better safe than sorry when dealing with deletion of files as files deleted in this way cannot be recovered.
- Change the folder_path as we did earlier, you can also modify the min_songs if 10 doesn't work for you. 
- Run in interactive window just like the previous program
  - Then, verify that no playlist you want to keep is on the list of removal
  - Enter 'y' on the next two prompts to remove the selected playlists

# Finally
Once the both programs are run successfully you should have your playlist files!
Depending on your DJ Software the playlists may appear in different ways. I use Traktor Pro 3 and this is how I see my playlists: 
![image](https://github.com/BigCod3/MusicGenre-ifier/assets/101913888/e3458b73-9b57-404e-98a2-e453ee3ea862)


# Known issues/Possible improvements
- Speed: Threading could probably vastly increase the speed that this runs at but the main issue I faced was:
  - Iterating through the song list, we'd want to avoid using the same song twice. This is probably easily solvable and I may dive into this in the future. But for one use-case, no threading is fine.
- Clicking on wrong song/Song not in list: 
  - This is a tricky issue as in my case, a lot of my music isn't actually on Spotify. For example I have a lot of remixes to popular songs, and sometimes when the song name is searched, the original appears first and we will get genre info for that song. 
     - One example of this was an EDM remix of Thunderstruck by AC/DC, the results I got from Chosic are only for the original song. 
  - In some cases, the song will not be on spotify at all, and we will get genre info from whatever the first result is.
  - Parts of the filename containing extra text can cause these issues sometimes. For example if audio is downloaded from YouTube and the title contains stuff like "[MUSIC VIDEO]" or "[OFFICIAL AUDIO]". 
- Could add more specific error handling for more clear descriptions of what's wrong when an error occurs.
- Using Spotify API
  - This is a big potential improvement as Chosic is basically doing this part for us.
  - Requires a rewrite to a lot of the code as this code is mainly focused on Selenium and grabbing info from the website. 

# End/Thanks
Thanks for checking out my project! This was my first attempt at uploading a project to Github, any feedback is appreciated. 

Also thank you to these resources, without them my DJing hobby would be much harder to persue.
- [Chosic](https://www.chosic.com) - Without this site and its tools I would still be fumbling with Spotify API calls to make this work. They have plenty of tools aside from just a genre finder, check them out!
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Fantastic cmdline tool for downloading audio from YouTube
- [spotdl](https://github.com/spotDL/spotify-downloader) - Another awesome cmdline tool for downloading spotify links. Analyzes info from Spotify link and gets audio from YouTube.
- [Undetected Chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) - Mentioned earlier but an awesome project that aims to avoid bot detection when using selenium. 
- [Selenium Documentation](https://www.selenium.dev/documentation/webdriver/) - Super useful tool for automating anything with a browser.
