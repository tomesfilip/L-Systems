import random
import string
import turtle
import time
from operator import itemgetter
from queue import LifoQueue


class LSystemDrawer:
    drawer = None

    def __init__(self, speed_val: int = 10, size: int = 10, pen_width: int = 2, sleep_time: int = 1):
        self.size = size
        self.sleep_time = sleep_time
        self.drawer = turtle.Turtle()
        self.drawer.speed(speed_val)
        self.drawer.pensize(pen_width)
        self.drawer.hideturtle()
        self.conditions = {
            "A-U": string.ascii_uppercase.rsplit("V")[0],
            "a-u": string.ascii_lowercase.rsplit("v")[0],
            "digits": string.digits,
            "V-Z": string.ascii_uppercase.rsplit("U")[1],
            "v-z": string.ascii_lowercase.rsplit("u")[1],
        }

    def clear_board(self):
        self.drawer.clear()

    def draw_object(self, sentences: list, angle: int, object_name: str):
        drawing_states = LifoQueue()
        print(f"---{object_name}---")
        for i, sentence in enumerate(sentences):
            self._write_text(f"#{i} {object_name}")
            self._restart_drawer(color_set=self._get_random_color())
            print(f"Iteration #{i} / Sentence: {sentence}")
            for command in sentence:
                if command in self.conditions.get("A-U") or command in self.conditions.get("digits"):
                    self.drawer.pendown()
                    self.drawer.forward(self.size)
                elif command in self.conditions.get("a-u"):
                    self.drawer.penup()
                    self.drawer.forward(self.size)
                elif command in self.conditions.get("V-Z") or command in self.conditions.get("v-z"):
                    continue
                elif command == "+":
                    self.drawer.left(angle)
                elif command == "-":
                    self.drawer.right(angle)
                elif command == "|":
                    self.drawer.setheading(180)
                elif command == "[":
                    drawing_states.put({"pos": self.drawer.pos(), "angle": self.drawer.heading()})
                elif command == "]":
                    curr_pos, curr_angle = itemgetter("pos", "angle")(drawing_states.get())
                    self.drawer.setposition(curr_pos)
                    self.drawer.setheading(curr_angle)
                else:
                    continue

            time.sleep(self.sleep_time)
            self._restart_drawer(clear=True)

    def _restart_drawer(self, clear: bool = False, color_set: str = "#000000"):
        if clear:
            self.clear_board()
        self.drawer.penup()
        self.drawer.setposition(
            self.drawer.getscreen().window_width() * 0.01,
            self.drawer.getscreen().window_height() * 0.01
        )
        self.drawer.pencolor(color_set)
        self.drawer.setheading(0)
        self.drawer.pendown()

    def _get_screen_width(self):
        return self.drawer.getscreen().window_width()

    def _get_screen_height(self):
        return self.drawer.getscreen().window_height()

    def _write_text(self, text: str):
        self.drawer.penup()
        self.drawer.setposition(
            self.drawer.getscreen().window_width() / -2 + 100,
            self.drawer.getscreen().window_height() / 2 - 100
        )
        self.drawer.pendown()
        self.drawer.write(text, font=("Verdana", 16, "bold"))

    @staticmethod
    def _get_random_color():
        return "#" + "".join([random.choice("0123456789ABCDEF") for char in range(6)])
