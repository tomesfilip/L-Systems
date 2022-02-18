import turtle


class LSystemDrawer:
    drawer = None

    def __init__(self, speed_val: int = 10, size: int = 10, start_x: int = -100, start_y: int = -100):
        self.size = size
        turtle.setworldcoordinates(-1, -1, 2000, 2000)
        self.drawer = turtle.Turtle()
        self.drawer.speed(speed_val)

    def draw_sierpinski_triangle(self, sentences: list):
        sierpinski_triangle_alphabet = ["F", "G", "+", "-"]
        pass

    def draw_dragon_curve(self, sentences: list):
        dragon_curve_alphabet = ["F", "G", "+", "-"]
        angle = 90

        for i, sentence in enumerate(sentences):
            for command in sentence:
                if command not in dragon_curve_alphabet:
                    print(f"Unknown character: {command} cannot be processed - skipping..")
                    continue
                match command:
                    case "F" | "G":
                        self.drawer.forward(self.size),
                    case "+":
                        self.drawer.left(angle)
                    case "-":
                        self.drawer.right(angle)
            if i < 5:
                self._move_by(moving_val=200)
            elif i >= 5:
                self.clear_board()
                self.drawer.penup()
                self.drawer.goto(self.drawer.getscreen().window_width() / 2, self.drawer.getscreen().window_height() / 2)
                self.drawer.pendown()
        turtle.done()

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
                        # TODO: get the last coordinates and position
                        pass

            if i < 5:
                self._move_by(moving_val=200)
            elif i >= 5:
                self.clear_board()
                self.drawer.penup()
                self.drawer.goto(self.drawer.getscreen().window_width() / 2, self.drawer.getscreen().window_height() / 2)
                self.drawer.pendown()
        turtle.done()

    def clear_board(self):
        self.drawer.clear()

    def _move_by(self, moving_val):
        self.drawer.penup()
        self.drawer.setx(self.drawer.xcor() + moving_val)
        self.drawer.sety(self.drawer.ycor() + moving_val)
        self.drawer.pendown()
