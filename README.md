# ai-background
 Desktop background image that is ai generated and updates automatically every few minutes.
 The image is taken from http://lape.si:8080/apps/ai-background/image.

 ### Optional:
 Change the type of image or amount of images (combined -> 6 images) by changing the url to the following:

 **Wikipedia Articles**: http://lape.si:8080/apps/ai-background/wikipedia/image (currently not updating)

 **Landscapes**: http://lape.si:8080/apps/ai-background/landscape/image

 **Combined**: http://lape.si:8080/apps/ai-background/combined

 **Combined Landscapes**: http://lape.si:8080/apps/ai-background/landscape/combined

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

## Windows 11 Uninstall
1. Press Windows Key + R
2. Delete the "HideUpdateAiBackground.vbs" file from the startup folder
3. Delete the cloned repository
4. Restart your computer

## Linux Installation
1. Place the linux folder anywhere in your system
2. Choose the right subfolder according to your desktop environment and copy the path to main.py
2. Change the line: `ExecStart=/usr/bin/python3 [X]` in the ai_background.service file
by replacing [X] with the absolute path of your main.py file.
3. Change the line: `User=[Y]` in the ai_background.service file
by replacing [Y] with your username.
4. Place the ai_background.service file in `/etc/systemd/system` 
(might be differrent in some distributions)
5. Use the command `sudo systemctl enable ai_background` to make the application autostart after boot.


## Linux Gnome Troubleshooting
 - If the background is not changing properly, try to set the tmp image in the X folder as a background manually.
