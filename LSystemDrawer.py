import turtle
from operator import itemgetter


class LSystemDrawer:
    drawer = None

    def __init__(self, speed_val: int = 10, size: int = 10, start_x: int = -100, start_y: int = -100):
        self.size = size
        turtle.setworldcoordinates(0, 0, 2000, 2000)
        self.drawer = turtle.Turtle()
        self.drawer.speed(speed_val)

    def draw_sierpinski_triangle(self, sentences: list):
        sierpinski_triangle_alphabet = ["-", "+", "F", "G"]
        angle = 120

        for i, sentence in enumerate(sentences):
            for command in sentence:
                if command not in sierpinski_triangle_alphabet:
                    print(f"Unknown character: {command} cannot be processed, skipping..")
                match command:
                    case "F" | "G":
                        self.drawer.forward(self.size),
                    case "+":
                        self.drawer.left(angle)
                    case "-":
                        self.drawer.right(angle)
            self._draw_next_iter(curr_iter=i)

    def draw_dragon_curve(self, sentences: list):
        dragon_curve_alphabet = ["F", "G", "+", "-"]
        angle = 90

        for i, sentence in enumerate(sentences):
            for command in sentence:
                if command not in dragon_curve_alphabet:
                    print(f"Unknown character: {command} cannot be processed, skipping..")
                    continue
                match command:
                    case "F" | "G":
                        self.drawer.forward(self.size),
                    case "+":
                        self.drawer.left(angle)
                    case "-":
                        self.drawer.right(angle)
            self._draw_next_iter(curr_iter=i)

    def draw_fractal_plant(self, sentences: list):
        fractal_plant_alphabet = ["X", "F", "+", "-", "[", "]"]
        angle = 25
        drawing_states = []

        for i, sentence in enumerate(sentences):
            for command in sentence:
                if command not in fractal_plant_alphabet:
                    print(f"Unknown character: {command} cannot be processed - skipping..")
                    continue
                match command:
                    case "F":
                        self.drawer.forward(self.size),
                    case "+":
                        self.drawer.left(angle)
                    case "-":
                        self.drawer.right(angle)
                    case "X":
                        continue
                    case "[":
                        drawing_states.insert(0, {"pos": self.drawer.pos(), "angle": self.drawer.heading()})
                    case "]":
                        curr_pos, curr_angle = itemgetter("pos", "angle")(drawing_states.pop())
                        self.drawer.setheading(curr_angle)
                        self.drawer.penup()
                        self.drawer.goto(curr_pos)
                        self.drawer.pendown()

            self._draw_next_iter(curr_iter=i)

    def clear_board(self):
        self.drawer.clear()

    # def _draw_object(self, alphabet: list, sentences: list, angle=25, use_drawing_state_stack: bool=False):
    #     for i, sentence in enumerate(sentences):
    #         for command in sentence:
    #             if command not in alphabet:
    #                 print(f"Unknown character: {command} cannot be processed - skipping..")
    #                 continue
    #             match command:
    #                 case "F":
    #                     self.drawer.forward(self.size),
    #                 case "+":
    #                     self.drawer.left(angle)
    #                 case "-":
    #                     self.drawer.right(angle)
    #                 case "X":
    #                     continue
    #                 case "[":
    #                     drawing_states.insert(0, {"pos": self.drawer.pos(), "angle": self.drawer.heading()})
    #                 case "]":
    #                     print(drawing_states.pop())
    #                     # TODO: get the last coordinates and position
    #                     pass
    #
    #         self._draw_next_iter(curr_iter=i)
    #     turtle.done()

    def _move_by(self, moving_val=200):
        self.drawer.penup()
        self.drawer.setx(self.drawer.xcor() + moving_val)
        self.drawer.sety(self.drawer.ycor() + moving_val)
        self.drawer.pendown()

    def _draw_next_iter(self, curr_iter):
        if curr_iter < 3:
            self._move_by(moving_val=self.drawer.getscreen().window_width() / 2)
        elif curr_iter >= 3:
            self.clear_board()
            self.drawer.penup()
            self.drawer.goto(self.drawer.getscreen().window_width() / 2, self.drawer.getscreen().window_height())
            self.drawer.pendown()
