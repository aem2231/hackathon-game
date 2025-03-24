import arcade

# Window Margins #
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Platformer"

# Game opening #
def main():
    """Main function"""
    window = GameView()
    window.setup()
    arcade.run()

class GameView(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class to set up the window
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

        self.background_color = arcade.csscolor.LIGHT_CYAN

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass

    def on_draw(self):
        """Render the screen."""

        # The clear method should always be called at the start of on_draw.
        # It clears the whole screen to whatever the background color is
        # set to. This ensures that you have a clean slate for drawing each
        # frame of the game.
        self.clear()

        # Code to draw other things will go here

if __name__ == "__main__":
    main()