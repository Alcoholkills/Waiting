import pyautogui
import sys


def DEBUG_rgb_colored_block(r, g, b):
    return f"\033[38;2;{r};{g};{b}m█\033[0m"

def DEBUG_print_mouse_position_continuously():
    try:
        while True:
            print(pyautogui.position())
    except KeyboardInterrupt:
        ...

def DEBUG_print_pixel_red_at_location(pos: tuple[int, int], size: tuple[int, int]):
    for y in range(pos[1], pos[1] + size[1]):
        for x in range(pos[0], pos[0] + size[0]):
            try:
                rgb_value = pyautogui.pixel(x, y)
                print(DEBUG_rgb_colored_block(*rgb_value), end="", flush=False)
            except OSError:
                continue
            except KeyboardInterrupt:
                sys.exit()
        print()

if __name__ == "__main__":
    mouse_position = (449, 1020)
    # DEBUG_print_mouse_position_continuously()
    (449, 1020)
    (22, 22)
    DEBUG_print_pixel_red_at_location(mouse_position, (22, 22))