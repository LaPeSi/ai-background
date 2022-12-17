import requests
import time
import os

tmp_file_path = os.path.split(os.path.abspath(__file__))[0] + "/ai_background_tmp.jpg"


def get_image():
    img = requests.request("GET", url="http://lape.si:8080/apps/ai-background/image").content
    with open(tmp_file_path, "wb") as f:
        f.write(img)
        f.flush()


def set_image():
    # set as background
    os.system("gsettings set org.gnome.desktop.background picture-uri-dark file://" + tmp_file_path)


def run(time_between_images=60):
    while True:
        get_image()
        time.sleep(3)  # short delay to ensure image is written to the disk properly
        set_image()
        time.sleep(time_between_images)


if __name__ == "__main__":
    time.sleep(20)
    run()
