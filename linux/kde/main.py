import requests
import time
import os
import dbus

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


def kde_set_image():
    # set as background

    jscript = """
    var allDesktops = desktops();
    print (allDesktops);
    for (i=0;i<allDesktops.length;i++) {
        d = allDesktops[i];
        d.wallpaperPlugin = "%s";
        d.currentConfigGroup = Array("Wallpaper", "%s", "General");
        d.writeConfig("Image", "file://%s")
    }
    """
    bus = dbus.SessionBus()
    plasma = dbus.Interface(bus.get_object(
        'org.kde.plasmashell', '/PlasmaShell'), dbus_interface='org.kde.PlasmaShell')
    plasma.evaluateScript(jscript % ('org.kde.image', 'org.kde.image', tmp_file_path))


def run(time_between_images=60):
    while True:
        get_image()
        time.sleep(3)  # short delay to ensure image is written to the disk properly
        kde_set_image()
        time.sleep(time_between_images)


if __name__ == "__main__":
    time.sleep(20)
    run()