import arcade
import random

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

        self.score = 0
        self.health = 100

        self.collectibles = arcade.SpriteList()
        for _ in range(5):
            collectible = arcade.SpriteSolidColor(20, 40, arcade.color.YELLOW)
            collectible.center_x = random.randint(0, width)
            collectible.center_y = random.randint(0, height)
            self.collectibles.append(collectible)

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.enemy.draw()
        self.collectibles.draw()
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE)
        arcade.draw_text(f"Health: {self.health}", 10, 30, arcade.color.WHITE)

    def update(self, delta_time):
        if arcade.check_for_collision(self.player, self.enemy):
            self.health -= 10
            if self.health <= 0:
                self.game_over()

        for collectible in self.collectibles:
            if arcade.check_for_collision(self.player, collectible):
                self.score += 10
                collectible.remove_from_sprite_lists()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player.center_x -= 10
        elif key == arcade.key.RIGHT:
            self.player.center_x += 10
        elif key == arcade.key.UP:
            self.player.center_y += 10
        elif key == arcade.key.DOWN:
            self.player.center_y -= 10

    def game_over(self):
        # Add game over logic here
        pass

def main():
    game = Game(800, 600)
    arcade.run()

if __name__ == "__main__":
    main()
