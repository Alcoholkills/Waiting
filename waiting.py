from pynput.keyboard import Key, Controller
import pyautogui
import sounddevice as sd
import numpy as np
import time
import random
import datetime
import sys
import math

keyboard = Controller()
START_WORKING_TIME = 80000 - random.randint(0, 300)
STOP_WORKING_TIME = 170000 + random.randint(0, 300)
TEAMS_LOCATION = (372, 1156)
SMALL_SCREEN_TEAMS_NOTIFICATION_STATUS = (383, 1140)
TEAMS_NOTIFICATION_STATUS_SIZE = (22, 22)
TEAMS_STATUS_GREEN = (26, 122, 26)
TEAMS_STATUS_RED = (162, 49, 55)
TEAMS_STATUS_YELLOW = (171, 124, 17)
TEAMS_STATUS_NONE = (44, 46, 73)
DICT_TEAMS_STATUS = {
    "Green": TEAMS_STATUS_GREEN,
    "Red": TEAMS_STATUS_RED,
    "Yellow": TEAMS_STATUS_YELLOW,
    "None": TEAMS_STATUS_NONE
}

class WAITING():
    def __init__(self) -> None:
        self.keyboard = Controller()
        self.START_WORKING_TIME = 80000 - random.randint(0, 300)
        self.STOP_WORKING_TIME = 170000 + random.randint(0, 300)
        self.TEAMS_LOCATION = (372, 1156)
        self.SMALL_SCREEN_TEAMS_NOTIFICATION_STATUS = (383, 1140)
        self.TEAMS_NOTIFICATION_STATUS_SIZE = (22, 22)
        self.TEAMS_STATUS_GREEN = (26, 122, 26)
        self.TEAMS_STATUS_RED = (162, 49, 55)
        self.TEAMS_STATUS_YELLOW = (171, 124, 17)
        self.TEAMS_STATUS_NONE = (44, 46, 73)
        self.DICT_TEAMS_STATUS = {
            "Green": self.TEAMS_STATUS_GREEN,
            "Red": self.TEAMS_STATUS_RED,
            "Yellow": self.TEAMS_STATUS_YELLOW,
            "None": self.TEAMS_STATUS_NONE
        }
    
    def SoD(self):
        now = self.get_current_time_to_HHMMSS()
        if now > self.START_WORKING_TIME:
            self.open_teams()
            return
        self.keyboard.tap(Key.f2)
        time.sleep(20)
        self.SoD()
    
    def DtD(self):
        now = get_current_time_to_HHMMSS()
        if now < self.STOP_WORKING_TIME:
            return
        keyboard.tap(Key.f2)
        status = get_teams_status()
        if status.lower() == "none":
            play_sound(2, 200, 5)
        elif status.lower() == "yellow":
            play_sound(1,600, 10)
            play_sound(2,1,0)
            play_sound(1,600, 10)
            play_sound(2,1,0)
            play_sound(1,600, 10)
        elif status.lower() == "red":
            play_sound(5, 440, 5)
            play_sound(2, 1, 0)
        elif status.lower() == "green":
            time.sleep(20)
        wait_DtD()


def Waiting() -> None:
    wait_SoD()
    wait_DtD()


def wait() -> None:
    try:
        while True:
            keyboard.tap(Key.f2)
            time.sleep(20)
    except KeyboardInterrupt:
        exit()

def wait_EoD():
    keyboard = Controller()
    now: int = get_current_time_to_HHMMSS()
    while now < STOP_WORKING_TIME:
        now: int = get_current_time_to_HHMMSS()
        keyboard.tap(Key.f2)
        time.sleep(20)

def wait_DtD():
    now = get_current_time_to_HHMMSS()
    if now < STOP_WORKING_TIME:
        return
    keyboard.tap(Key.f2)
    status = get_teams_status()
    if status.lower() == "none":
        play_sound(2, 200, 5)
    elif status.lower() == "yellow":
        play_sound(1,600, 10)
        play_sound(2,1,0)
        play_sound(1,600, 10)
        play_sound(2,1,0)
        play_sound(1,600, 10)
    elif status.lower() == "red":
        play_sound(5, 440, 5)
        play_sound(2, 1, 0)
    elif status.lower() == "green":
        time.sleep(20)
    wait_DtD()

def wait_SoD():
    now = get_current_time_to_HHMMSS()
    if now > START_WORKING_TIME:
        open_teams()
        return
    keyboard.tap(Key.f2)
    time.sleep(20)
    wait_SoD()

def open_teams():
    pyautogui.moveTo(*TEAMS_LOCATION, duration=1.5)
    pyautogui.click()

def get_current_time_to_HHMMSS() -> int:
    now = datetime.datetime.now()
    return int(now.strftime("%H%M%S"))

def DEBUG_print_mouse_position_continuously():
    try:
        while True:
            print(pyautogui.position())
    except KeyboardInterrupt:
        ...

def rgb_colored_block(r: int, g:int, b: int) -> str:
    return f"\033[38;2;{r};{g};{b}m█\033[0m"

def DEBUG_print_pixel_red_at_location(pos: tuple[int, int], size: tuple[int, int]):
    for y in range(pos[1], pos[1] + size[1]):
        for x in range(pos[0], pos[0] + size[0]):
            try:
                rgb_value = pyautogui.pixel(x, y)
                print(rgb_colored_block(*rgb_value), end="", flush=False)
            except OSError:
                continue
            except KeyboardInterrupt:
                sys.exit()
        print()

def pixel_color_red_at_location(pos: tuple[int, int], size: tuple[int, int]) -> list[tuple[int, int, int]]:
    pixel_color_vector = list()
    for y in range(pos[1], pos[1] + size[1]):
        for x in range(pos[0], pos[0] + size[0]):
            try:
                pixel_color_vector.append(pyautogui.pixel(x, y))
            except OSError:
                continue
            except KeyboardInterrupt:
                sys.exit()
    return pixel_color_vector

def find_average_color(color_vector: list[tuple[int, int, int]]):
    sum_r = sum_g = sum_b = 0
    size = len(color_vector)
    for color in color_vector:
        sum_r += color[0]
        sum_g += color[1]
        sum_b += color[2]
    return (sum_r // size, sum_g // size, sum_b // size)

def distance_between_colors(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def get_teams_status():
    color_vector = pixel_color_red_at_location(SMALL_SCREEN_TEAMS_NOTIFICATION_STATUS, TEAMS_NOTIFICATION_STATUS_SIZE)
    avg_color = find_average_color(color_vector)
    min_distance = 500
    min_color = ""
    for k, v in DICT_TEAMS_STATUS.items():
        d = distance_between_colors(avg_color, v)
        if d < min_distance:
            min_distance = d
            min_color = k
    return min_color

def play_sound(duration = 2, frequency = 440.0, volume = 1):
    samplerate = 44100  # Hz

    # Generate a sine wave
    t = np.linspace(0.0, duration, int(duration * samplerate), endpoint=False)
    samples = volume * np.sin(2 * np.pi * frequency * t).astype(np.float32)

    # Play the sound
    sd.play(samples, samplerate)
    sd.wait()

if __name__ == "__main__":
    ...
    # wait()
    # print_mouse_position_continuously()
    # print_pixel_red_at_location(SMALL_SCREEN_TEAMS_NOTIFICATION_STATUS, TEAMS_NOTIFICATION_STATUS_SIZE)
    # color_vector = pixel_color_red_at_location(SMALL_SCREEN_TEAMS_NOTIFICATION_STATUS, TEAMS_NOTIFICATION_STATUS_SIZE)
    # avg_color = find_average_color(color_vector)
    # print(avg_color)
    # print(rgb_colored_block(*avg_color))
    # play_sound(2, 400, 5)
    open_teams()


