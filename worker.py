import math
import container
import win32gui, win32con, time
from win32api import GetSystemMetrics

system_height = GetSystemMetrics(1)
system_width = GetSystemMetrics(0)
outline_x = 0
outline_y = 0

def draw_Window(hwnd,x,y,heigth,width):
    win32gui.MoveWindow(hwnd, x, y, width + 2*outline_x, heigth + 2 * outline_y, True)

def place_Windows(container_uebergabe, lokation_x, lokation_y):
    print(container_uebergabe.hwnd)
    if container_uebergabe.leav == True:
        draw_Window(container_uebergabe.hwnd,lokation_x,lokation_y,container_uebergabe.height,container_uebergabe.width)
    else:
        if container_uebergabe.splid_mode == 0:
            pixel_horrizontal_counter = lokation_x
            for i in container_uebergabe.childs:
                place_Windows(i,pixel_horrizontal_counter,lokation_y)
                pixel_horrizontal_counter += i.width
        else:
            pixel_vertical_counter = lokation_y
            for i in container_uebergabe.childs:
                place_Windows(i,location_x,pixel_vertical_counter)
                pixel_vertical_counter += i.height

def enumHandler1(hwnd, list1):
    list1.append(int(hwnd))

def main():
    windowlist = []
    win32gui.EnumWindows(enumHandler1, windowlist)
    counter = 0
    for a in windowlist:
        if win32gui.IsWindowVisible(a) and (a != 0) and str(win32gui.GetWindowText(a)) != "":
            try:
                win32gui.ShowWindow(a, win32con.SW_NORMAL)
                if counter < 3:
                    root_container.hwnd = int(a)
                    print(win32gui.GetWindowText(a) + "  " + str(counter) + "  " + str(a))
                counter += 1
            except Exception as e:
                print("Error Type 1\n" + str(e))

    root_container.leav = True
    place_Windows(root_container,0,0)

if __name__ == '__main__':
    root_container = container.container(system_width,system_height, 0, [], 1, 0, 0, False,0)
    main()
