import arcade

class Game(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.BLACK)

        self.player = arcade.SpriteCircle(20, arcade.color.BLUE)
        self.player.center_x = width // 2
        self.player.center_y = height // 2

        self.enemy = arcade.SpriteSolidColor(20,20, arcade.color.RED)
        self.enemy.center_x = width // 4
        self.enemy.center_y = height // 4

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.enemy.draw()

    def update(self, delta_time):
        pass

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player.center_x -= 10
        elif key == arcade.key.RIGHT:
            self.player.center_x += 10
        elif key == arcade.key.UP:
            self.player.center_y += 10
        elif key == arcade.key.DOWN:
            self.player.center_y -= 10

def main():
    game = Game(800, 600)
    arcade.run()

if __name__ == "__main__":
    main()
