from PIL import ImageGrab
import win32gui

toplist, winlist = [], []
def enum_cb(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
win32gui.EnumWindows(enum_cb, toplist)
firefox = [(hwnd, title) for hwnd, title in winlist if 'among us' in title.lower()]
# just grab the hwnd for first window matching firefox
firefox = firefox[0]
hwnd = firefox[0]

win32gui.SetForegroundWindow(hwnd)
bbox = win32gui.GetWindowRect(hwnd)
img = ImageGrab.grab(bbox)
(width, heigh) = img.size

ratio_speed = 5

while True:
    green_found = 0
    blue_found = 0
    for x in range(int(width/ratio_speed)):
        for y in range(int(heigh/ratio_speed)):
            pixels = img.getpixel((x*ratio_speed, y*ratio_speed))
            if (10 < pixels[0] < 20 and 60 < pixels[1] < 140 and 25 < pixels[2] < 50):
                green_found+=1
            if (10 < pixels[0] < 20 and 30 < pixels[1] < 60 and 180 < pixels[2] < 220):
                blue_found+=1
    print("\n" * 5)
    #DEBUG
    print(f"\nDEBUG:")
    if True:
        print(f"Green: {green_found}")
        print(f"Blue: {blue_found}")

    print(f"\nFound:")

    if 5 < green_found < 100: print(f"Green")
    if 5 < blue_found  < 100:  print(f"Blue")
    img = ImageGrab.grab(bbox)