
# Installation

1. Place the linux-gnome folder in any directory 

2. Change the line: `ExecStart=/usr/bin/python3 [X]` in the ai_background.service file
by replacing [X] with the absolute path of the main.py file.

3. Change the line: `User=[Y]` in the ai_background.service file
by replacing [Y] with your username.

4. Place the ai_background.service file in `/etc/systemd/system` 
(might be differrent in some distributions)

5. Use the command `sudo systemctl enable ai_background` to make the application autostart after boot.


# Troubleshooting
 - If the background is not changing properly, try to set the tmp image in the X folder as a background manually.
