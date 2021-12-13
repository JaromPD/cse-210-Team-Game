from zombie_run.script.HandlePlayerMonstersCollison import HandlePlayerMonstersCollision
from genie.director import Director
from genie.cast.cast import Cast
from genie.script.script import Script
from genie.services import *

from genie.cast.animatedActor import AnimatedActor
from genie.cast.actor import Actor
from genie.script.action import Action

from zombie_run.script.HandleOffscreenAction import HandleOffscreenAction
from zombie_run.script.HandleStartGameAction import HandleStartGameAction

from zombie_run.cast.hearts import Heart
from zombie_run.cast.background import Background
from zombie_run.cast.playerScore import PlayerScore
from zombie_run.cast.ship import Ship
from zombie_run.cast.floor import Floor
from zombie_run.script.PlayBackgroundMusicAction import PlayBackgroundMusicAction
from zombie_run.script.DrawScoreAction import DrawScoreAction
from zombie_run.script.HandlePlayerHittingFloorAction import HandlePlayerHittingFloorAction
from zombie_run.cast.startGameButton import StartGameButton
from zombie_run.script.HandleQuitAction import HandleQuitAction
from zombie_run.script.HandlePlayerMovementAction import HandlePlayerMovementAction
from zombie_run.script.MoveActorsAction import MoveActorsAction
from zombie_run.script.HandlePointAccumulation import HandlePointAccumulation
from zombie_run.script.SpawnMonstersAction import SpawnMonstersAction
from zombie_run.script.DrawActorsAction import DrawActorsAction
from zombie_run.script.UpdateScreenAction import UpdateScreenAction


W_SIZE = (1000, 500)
START_POSITION = 200, 250
SHIP_WIDTH = 40
SHIP_LENGTH = 55
SCREEN_TITLE = "Zombie Run"
FPS = 120
INITIAL_NUM_LIVES = 3

def get_services():
    """
        Ask the user whether they want to use pygame or raylib services
    """
    # Initialize all services:
    service_code = 2
    
    return {
        "keyboard" : PygameKeyboardService() if service_code == 1 else RaylibKeyboardService(),
        "physics" : PygamePhysicsService() if service_code == 1 else RaylibPhysicsService(),
        "screen" : PygameScreenService(W_SIZE, SCREEN_TITLE, FPS) if service_code == 1 \
                    else RaylibScreenService(W_SIZE, SCREEN_TITLE, FPS),
        "audio" : PygameAudioService() if service_code == 1 else RaylibAudioService(),
        "mouse" : PygameMouseService() if service_code == 1 else RaylibMouseService()
    }

def main():
    """
        Create director, cast, script, then run the game loop
    """
    # Get all the services needed services 
    services = get_services()

    keyboard_service = services["keyboard"]
    physics_service = services["physics"]
    screen_service = services["screen"]
    audio_service = services["audio"]
    mouse_service = services["mouse"]
    
    # Create a director
    director = Director()

    # Create all the actors, including the player
    cast = Cast()

    # Create the player
    player_walk = []
    for i in range(11):
        if i < 10:
            player_walk.append(f"zombie_run/assets/zombie/walk/__Zombie01_Walk_00{i}.png")
        else:
            player_walk.append(f"zombie_run/assets/zombie/walk/__Zombie01_Walk_0{i}.png")

    player = AnimatedActor(player_walk,
                            width =70, 
                            height=85,
                            animation_fps=11,
                            game_fps=60,
                            event_triggered=False,
                            x=200, y=400, 
                            rotation=0, 
                            rotation_vel=0, flipped = False
                            )

    # Start game button
    start_button = StartGameButton(path="zombie_run/assets/others/start_button2.png",
                                    width = 305,
                                    height = 113,
                                    x = W_SIZE[0]/2,
                                    y = W_SIZE[1]/2)

    # Create a floor
    floor = Floor(path=" ",
                                    width = 1000,
                                    height = int(W_SIZE[0] / 5.7),
                                    x = W_SIZE[0]/2,
                                    y = W_SIZE[1]-int(W_SIZE[0] / 5.7)/2) 
    
    # Create the score
    score = PlayerScore(path="", score=0 )

    background_image = Background("zombie_run/assets/3_game_background.png", 
                                    width=W_SIZE[0],
                                    height=W_SIZE[1],
                                    x = W_SIZE[0]/2,
                                    y = W_SIZE[1]/2)

    # Give actor(s) to the cast
    cast.add_actor("background_image", background_image)
    cast.add_actor("player", player)
    cast.add_actor("score", score)
    cast.add_actor("start_button", start_button)
    cast.add_actor("floor", floor)
        # Create the hearts
    heart_x = 700
    for _ in range(INITIAL_NUM_LIVES):
        heart = Heart(path="zombie_run/assets/tombstone.png", 
                        width = 100,
                        height = 100,
                        x = heart_x,
                        y = 50,
                        rotation=0)
        heart_x += 75
        cast.add_actor("hearts", heart)

    # Create all the actions
    script = Script()

    # Create input actions
    script.add_action("input", HandleQuitAction(1, keyboard_service))

    # Add actions that must be added to the script when the game starts
    startgame_actions = {"input" : [], "update" : [], "output": []}
    startgame_actions["input"].append(HandlePlayerMovementAction(2, keyboard_service))
    startgame_actions["update"].append(SpawnMonstersAction(1, W_SIZE))
    startgame_actions["update"].append(HandlePointAccumulation(1, W_SIZE))
    script.add_action("input", HandleStartGameAction(2, mouse_service, physics_service, startgame_actions, audio_service))

    # Create update actions
    script.add_action("update", HandlePlayerHittingFloorAction(1, W_SIZE))
    script.add_action("update", MoveActorsAction(1, physics_service))
    script.add_action("update", HandleOffscreenAction(2, W_SIZE))
    script.add_action("update", HandlePlayerMonstersCollision(1, physics_service, audio_service))
    #script.add_action("update", HandlePointAccumulation(1,W_SIZE))

    # Create output actions
    script.add_action("output", PlayBackgroundMusicAction(1, "zombie_run/assets/sound/background_music.mp3", audio_service))
    script.add_action("output", DrawActorsAction(1, screen_service))
    script.add_action("output", DrawScoreAction(1, screen_service))
    script.add_action("output", UpdateScreenAction(2, screen_service))


    # Give the cast and script to the dirrector by calling direct_scene.
    # direct_scene then runs the main game loop:
    director.direct_scene(cast, script)

if __name__ == "__main__":
    main()