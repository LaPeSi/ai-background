import requests
import time
import os

tmp_file_path = os.path.split(os.path.abspath(__file__))[0] + "/ai_background_tmp.jpg"

tmp_file_path_last = os.path.split(os.path.abspath(__file__))[0] + "/ai_background_tmp_last.jpg"


def get_image():
    # save last image
    os.system("cp " + tmp_file_path + " " + tmp_file_path_last)
    time.sleep(1)

    img = requests.request("GET", url="http://lape.si:8080/apps/ai-background/combined").content
    
    with open(tmp_file_path, "wb") as f:
        f.write(img)
        f.flush()


def set_image():
    # set as background
    os.system("gsettings set org.gnome.desktop.background picture-uri-dark file://" + tmp_file_path)
    time.sleep(2)
    os.system("cp " + tmp_file_path + " ~/.config/background")


def run(time_between_images=60):
    while True:
        get_image()
        time.sleep(3)  # short delay to ensure image is written to the disk properly
        set_image()
        time.sleep(time_between_images)


if __name__ == "__main__":
    time.sleep(20)
    run()