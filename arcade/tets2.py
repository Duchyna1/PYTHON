import arcade

class ball(arcade.Sprite):
    def setup(self):
        self.

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Set the background color
        arcade.set_background_color(arcade.color.ASH_GREY)

        self.x, self.y = 0, 0

    def update(self, delta_time: float):
        pass

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        arcade.draw_circle_filled(self.x, self.y, 15, arcade.color.AUBURN)
        for x in range(10):
            arcade.draw_circle_filled(randint(0, 640), randint(0, 480), 20,
                                      arcade.color.LIME)

    def on_mouse_drag(self, x: float, y: float, dx: float, dy: float, buttons: int, modifiers: int):
        self.x = x
        self.y = y


def main():
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()


main()
