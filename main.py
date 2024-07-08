from controllers.game_controller import GameController

def main():
    game_controller = GameController()
    try:
        game_controller.start_game()
    except KeyboardInterrupt:
        game_controller.stop_game()

if __name__ == "__main__":
    main()
