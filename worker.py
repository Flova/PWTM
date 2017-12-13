import math
import container
import win32gui, win32con, time
from win32api import GetSystemMetrics

windowlist = []
system_height = GetSystemMetrics(1)
system_width = GetSystemMetrics(0)
outline_x = 0
outline_y = 0

def draw_Window(hwnd,x,y,heigth,width):
    win32gui.MoveWindow(hwnd, int(x), int(y),int(width + 2*outline_x), int(heigth + 2 * outline_y), True)

def place_Windows(container_uebergabe, lokation_x, lokation_y):
    try:
        title = str(win32gui.GetWindowText(container_uebergabe.hwnd))
    except:
        title = "Invalid"
    print("\nPrint Recursive Draw of Container\nContainer id: " + str(container_uebergabe.hwnd) + "\n Window Title: " + title + "\nIs Leav: " + str(container_uebergabe.leav) + "\nPosition: " + str(lokation_x) + " | " + str(lokation_y) + "\nSize:" + str(container_uebergabe.width) + " | " + str(container_uebergabe.height) + "\n\n--------------------------------------------------------------\n")
    if container_uebergabe.leav == True:
        draw_Window(container_uebergabe.hwnd,lokation_x,lokation_y,container_uebergabe.height,container_uebergabe.width)
    else:
        if container_uebergabe.splid_mode == 0:
            pixel_horrizontal_counter = lokation_x
            for i in container_uebergabe.childs:
                i.set_Percentage()
                place_Windows(i,pixel_horrizontal_counter,lokation_y)
                pixel_horrizontal_counter += i.width
        else:
            pixel_vertical_counter = lokation_y
            for i in container_uebergabe.childs:
                i.set_Percentage()
                place_Windows(i,lokation_x,pixel_vertical_counter)
                pixel_vertical_counter += i.height

def check_Window(hwnd):
     if(win32gui.IsWindowVisible(hwnd) and (hwnd != 0) and str(win32gui.GetWindowText(hwnd)) != "Windows PowerShell" and str(win32gui.GetWindowText(hwnd)) != ""):
         return True
     return False

def enumHandler1(hwnd, list1):
    if check_Window(hwnd):
        list1.append(int(hwnd))

def add_all_windows():
    win32gui.EnumWindows(enumHandler1, windowlist)

def debug_init():
    root_container.leav = False
    root_container.add_container(container.container(0,0,0,[],0.5, 0,1, True, 0))
    root_container.add_container(container.container(0,0,0,[],0.5, 1,2, False, 0))
    root_container.childs[1].add_container(container.container(0,0,0,[],0.5, 0,3, True, 0))
    root_container.childs[1].add_container(container.container(0,0,0,[],0.5, 0,4, True, 0))
    print(windowlist)
    root_container.childs[0].hwnd = int(windowlist[0])
    print(win32gui.GetWindowText(windowlist[0]) + "  " + str(windowlist[0]) + "\n")
    index = 0
    test1 = windowlist
    test1.pop(0)
    for hwnd in test1:
        try:
            win32gui.ShowWindow(hwnd, win32con.SW_NORMAL)
            root_container.childs[1].childs[index].hwnd = int(hwnd)
            print(win32gui.GetWindowText(hwnd) + "  "  + str(hwnd) + "\n")
        except Exception as e:
            print("Error Type 1\n" + str(hwnd))
        index += 1


def main():
    add_all_windows()
    debug_init()
    place_Windows(root_container,0,0)

if __name__ == '__main__':
    root_container = container.container(system_width,system_height, 0, [], 1, 0, 0, False,0)
    main()
