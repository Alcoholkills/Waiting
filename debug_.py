import pyautogui
import sys
import time
from pynput import mouse


def DEBUG_rgb_colored_block(r, g, b):
    return f"\033[38;2;{r};{g};{b}m██\033[0m"

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

def find_teams_logo():
    # print(pyautogui.size())
    # pyautogui.screenshot('Full_screen_shot.png')
    teams_logo_pos = pyautogui.locateOnScreen(r'C:\Users\prambert\Document\Programming\Python\Waiting\Teams_logo.png', confidence=0.8)
    print(teams_logo_pos)
    pyautogui.moveTo(teams_logo_pos)
    # for x in range(teams_logo_pos.left, teams_logo_pos.left + teams_logo_pos.width):
    #     for y in range(teams_logo_pos.top, teams_logo_pos.top + teams_logo_pos.height):
    #         pyautogui.pixel(x, y)
    # DEBUG_print_pixel_red_at_location((teams_logo_pos.left, teams_logo_pos.top), (teams_logo_pos.width, teams_logo_pos.height))
    DEBUG_print_pixel_red_at_location((teams_logo_pos.left + teams_logo_pos.width // 2, teams_logo_pos.top), (teams_logo_pos.width // 2, teams_logo_pos.height // 2))

def click_to_pos():
    def on_click(x, y, button, pressed):
        if button == mouse.Button.right and pressed:
            print(f"Mouse right-click at: ({x}, {y})")
        if button == mouse.Button.middle and pressed:
            exit()

    # Set up the mouse listener
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

def auto_click_machine():
    time.sleep(5)
    for i in range(274):
        # Selection de toutes les missions
        pyautogui.click(39, 320)
        # clique droit sur une mission
        time.sleep(0.2)
        pyautogui.rightClick(310, 498)
        # Bloquer mission
        time.sleep(0.2)
        pyautogui.click(429, 266)
        # valider
        time.sleep(0.5)
        pyautogui.click(1038, 195)
        # Attente recharchement
        time.sleep(2)

# Mouse right-click at: (39, 320)
# Mouse right-click at: (310, 498)
# Mouse right-click at: (429, 266)
# Mouse right-click at: (1038, 195)

if __name__ == "__main__":
    # mouse_position = (449, 1020)
    # mouse_position = (299, 1040)
    # mouse_position = (300, 1401)
    auto_click_machine()
    # (449, 1020)
    # (22, 22)
    # DEBUG_print_pixel_red_at_location(mouse_position, (13, 13))
    # find_teams_logo()