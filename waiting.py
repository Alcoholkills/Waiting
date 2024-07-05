from pynput.keyboard import Key, Controller
import pyautogui
import sounddevice as sd
import numpy as np
import time
import random
import datetime
import sys
import math

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
    
    def __get_current_time_to_HHMMSS__(self) -> int:
        """Gets the current time of the day and returns it as an `int` in the form `HHMMSS`"""
        now = datetime.datetime.now()
        return int(now.strftime("%H%M%S"))
    
    def __get_teams_status__(self):
        """Returns the name of the teams status based on reading"""
        color_vector = self.__pixel_color_red_at_location__(self.SMALL_SCREEN_TEAMS_NOTIFICATION_STATUS, self.TEAMS_NOTIFICATION_STATUS_SIZE)
        avg_color = self.__find_average_color__(color_vector)
        min_distance = 500
        min_color = ""
        for k, v in self.DICT_TEAMS_STATUS.items():
            d = self.__distance_between_colors__(avg_color, v)
            if d < min_distance:
                min_distance = d
                min_color = k
        return min_color
    
    def __open_teams__(self):
        """Opens Teams manually"""
        pyautogui.moveTo(*self.TEAMS_LOCATION, duration=1.5)
        pyautogui.click()

    def __pixel_color_red_at_location__(self, pos: tuple[int, int], size: tuple[int, int]) -> list[tuple[int, int, int]]:
        """"Reads all pixel at given location and returns the rgb values as a list of tuples"""
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

    def __find_average_color__(self, color_vector: list[tuple[int, int, int]]):
        """Reads a list of colors (rgb tuple) and returns the average color"""
        sum_r = sum_g = sum_b = 0
        size = len(color_vector)
        for color in color_vector:
            sum_r += color[0]
            sum_g += color[1]
            sum_b += color[2]
        return (sum_r // size, sum_g // size, sum_b // size)
    
    def __distance_between_colors__(self, p1, p2):
        """Distance in R3"""
        x1, y1, z1 = p1
        x2, y2, z2 = p2
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

    def __play_sound__(self, duration = 2, frequency = 440.0, volume = 1):
        """Plays a sound for the given `duration` in secods, for the given `frequency` in Hertz, for a given `volume` (|R+)"""
        samplerate = 44100
        t = np.linspace(0.0, duration, int(duration * samplerate), endpoint=False)
        samples = volume * np.sin(2 * np.pi * frequency * t).astype(np.float32)
        sd.play(samples, samplerate)
        sd.wait()

    def SoD(self):
        """Start of Day"""
        now = self.__get_current_time_to_HHMMSS__()
        if now > self.START_WORKING_TIME:
            self.__open_teams__()
            return
        self.keyboard.tap(Key.f2)
        time.sleep(20)
        self.SoD()
    
    def DtD(self):
        """During the Day"""
        now = self.__get_current_time_to_HHMMSS__()
        if now < self.STOP_WORKING_TIME:
            return
        self.keyboard.tap(Key.f2)
        status = self.__get_teams_status__()
        if status.lower() == "none":
            self.__play_sound__(2, 200, 5)
        elif status.lower() == "yellow":
            self.__play_sound__(1,600, 10)
            self.__play_sound__(2,1,0)
            self.__play_sound__(1,600, 10)
            self.__play_sound__(2,1,0)
            self.__play_sound__(1,600, 10)
        elif status.lower() == "red":
            self.__play_sound__(5, 440, 5)
            self.__play_sound__(2, 1, 0)
        elif status.lower() == "green":
            time.sleep(20)
        self.DtD()
    
    def start(self):
        """Starts waiting"""
        self.SoD()
        self.DtD()



if __name__ == "__main__":
    ...

