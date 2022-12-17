
# Installation

1. Place the linux-gnome folder in any directory X
2. Change the line: `ExecStart=/usr/bin/python3 [Y]`
and replace [Y] with the absolute path of the main.py file.
3. place the ai_background.service file in `/etc/systemd/system` 
(might be diffrerent in some distributions)
4. use the command `sudo systemctl enable ai_background` to make the application autostart after boot.


# Troubleshooting
 - If the background is not changing properly, try to set the tmp image in the X folder as a background manually.