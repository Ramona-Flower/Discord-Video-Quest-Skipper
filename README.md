# Discord-Video-Quest

This script allows you to make video quest on Discord almost instant by speeding up the playback rate by over 16x faster.  this script ensures your Discord video quests are completed almost immediately!
## ⭐ Feel free to star this repository ⭐

Get the code [by clicking here !](https://github.com/Ramona-Flower/Discord-Video-Quest-Skipper/blob/main/scripts.js) or by checking the readme ! 

Another script [click here !](https://github.com/Ramona-Flower/Discord-Video-Quest-Skipper/blob/main/scripts2.js)

# Features

- Increase playback rate to 16x the normal speed.
- Make Discord video quests nearly instant by reducing the time spent on video content.
- Easy to implement—just a simple line of JavaScript!

# Installation
- Step 1: Open Developer Tools in Discord
  - Open Discord in your browser (Chrome, Firefox, etc.) or in Vencord/BTT doing either f12 on webbrowser or CTRL+SHIFT+I (<- works everywhere).
Press F12 or right-click on the page and select Inspect to open the Developer Tools. Start the video quest.

- Step 2: Run the Script
-- Go to the Console tab in Developer Tools.
-- Paste the following code into the console:

(Write `allow pasting` if it does not let you

```js
document.querySelectorAll("video").forEach(v => v.playbackRate = 16);
```

  - Press Enter.
    
This will automatically adjust all video elements to play at 16x speed.

- Step 3: Enjoy!
   - After running the script, all videos on Discord will play at a faster rate. Feel free to replay the script if you want to adjust or reset the speed.

# How It Works
`document.querySelectorAll("video")`: Selects all the video elements on the page.
`.forEach(v => v.playbackRate = 16)`: Loops through each video element and sets the playbackRate property to 16.

# Note: 
I do not know if this kind of script is forbidden or not use it as your own risk.

# Why Use It?
Instant video quests: Skip through videos nearly instantly to get rewards faster.
Save time: Go through content without having to sit through 1 minute of video.

# Contributing
Feel free to contribute improvements or fixes! You can fork the repository and create a pull request. If you have any issues, open an issue in the repository, and I will try to resolve it as soon as possible.

License
This project is open-source and available under the MIT License.

