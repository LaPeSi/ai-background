# ai-background
 Desktop background image that is ai generated and updates automatically every few minutes.
 The image is taken from http://lape.si:8080/apps/ai-background/image.

## Windows 11 Installation
1. Clone the repository
2. Press Windows Key + R
3. Type in "shell:startup"
4. Create a shortcut to the "HideUpdateAiBackground.vbs" file in the startup folder (it will start update-ai-background.bat headless on startup)
5. Restart your computer

## Windows 11 Modify Installation
1. Open the "update-ai-background.bat" file in a text editor
2. To change the update interval, change the number in the "timeout" command
3. To change the download location, change the "curl" command to point to a different URL AND change the "reg add" command to point to the new location
4. Save the file
5. Restart your computer

## Windows 11 Remove Installation
1. Press Windows Key + R
2. Delete the "HideUpdateAiBackground.vbs" file from the startup folder
3. Delete the cloned repository
4. Restart your computer

## Linux Gnome Installation

1. Place the linux-gnome folder in any directory X
2. Change the line: `ExecStart=/usr/bin/python3 [Y]`
and replace [Y] with the absolute path of the main.py file.
3. place the ai_background.service file in `/etc/systemd/system` 
(might be diffrerent in some distributions)
4. use the command `sudo systemctl enable ai_background` to make the application autostart after boot.


## Linux Gnome Troubleshooting
 - If the background is not changing properly, try to set the tmp image in the X folder as a background manually.