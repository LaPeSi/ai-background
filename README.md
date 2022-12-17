# ai-background
 Desktop background image that is ai generated and updates automatically every few minutes.
 The image is taken from http://lape.si:8080/apps/ai-background/image.

#Windows 11 Installation
1. Clone the repository
2. Press Windows Key + R
3. Type in "shell:startup"
4. Create a shortcut to the "HideUpdateAiBackground.vbs" file in the startup folder (it will start update-ai-background.bat headless on startup)
5. Restart your computer

#Modify Windows 11 Installation
1. Open the "update-ai-background.bat" file in a text editor
2. To change the update interval, change the number in the "timeout" command
3. To change the download location, change the "curl" command to point to a different URL AND change the "reg add" command to point to the new location
4. Save the file
5. Restart your computer