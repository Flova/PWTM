import math
import container

def draw_Window(id,x,y,heigth,width):
    windows(id).x = x
    windows(id).y = y
    windows(id).height = height
    windows(id).width = width

def place_Windows(container_uebergabe, lokation_x, lokation_y):
    if container_uebergabe.leav == True:
        draw_Window(container_uebergabe.leav_id,lokation_x,lokation_y,container_uebergabe.height,container_uebergabe.width)
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


def main():
    place_Windows(root_container,0,0)

if __name__ == '__main__':
    root_container = container(screen.width, screen.width height, 0, [], 1, 0, 0)
    main()
