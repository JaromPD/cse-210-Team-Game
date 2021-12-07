from pyray import *
from raylib.colors import *
import math

from genie.cast.actor import Actor
from genie.cast.animatedActor import AnimatedActor

circle_sectors_dict = {
    # tr    tl    bl    br       : (start_angle, end_angle)

    (False, False, False, False) : (0, 360),
    (False, False, False, True) : (0, 90),
    (False, False, True, False) : (0, -90),
    (False, False, True, True) : (-90, 90),
    (False, True, False, False) : (-90, -180),
    (False, True, False, True) : ((-90, -180), (0, 90)),
    (False, True, True, False) : (0, -180),
    (False, True, True, True) : (90, -180),
    
    (True, False, False, False) : (90, 180),
    (True, False, False, True) : (0, 180),
    (True, False, True, False) : ((90, 180), (0, -90)),
    (True, False, True, True) : (-90, 180),
    (True, True, False, False) : (90, 270),
    (True, True, False, True) : (0, 270),
    (True, True, True, False) : (90, 360),
    (True, True, True, True) : (0, 360)
}

class RaylibScreenService:
    """
        This class provides the tool you need to draw stuff
    """
    def __init__(self, window_size, title : str = "", fps : int = 60):
        # if not pyray.is_window_ready():
        #     print("window initialized!")
        init_window(window_size[0], window_size[1], title)
        self._textures_cache = {}
        self.set_fps(fps)
    
    def initialize(self):
        """
            Nothing here for now...
        """
        pass

    def _load_texture(self, actor : Actor):
        """
            Takes in an actor that has 2 traits: Body and Image
                and load the image of that Actor into the cache
        """
        image_path = actor.get_path()
        # print("2")
                
        image_f = load_image(image_path)
        image_flip_horizontal(image_f)

        texture = load_texture(image_path)
        texture_f = load_texture_from_image(image_f)
        if texture_f == None:
            print("texture_f is none for some reason")
        # put image in cache so we don't have to load again
        if (image_path not in self._textures_cache.keys()):
            self._textures_cache[image_path] = texture
            self._textures_cache[image_path + "_f"] = texture_f

        return texture_f if actor.flipped() else texture

    def load_textures(self, actors : list):
        """
            load all the images into a dictionary cache
        """
        for actor in actors:
            self._load_texture(actor)
    
    def set_fps(self, fps : int = 60):
        """
            Set the desired fps. The framework will try to reach it
            but there's no guarantee.
        """
        self._fps = fps
        set_target_fps(fps)

    def begin_drawing(self):
        """
            What to call before drawing anything in a frame
        """
        begin_drawing()

    def fill_screen(self, color = WHITE):
        """
            Fill the screen with a certain color
        """
        clear_background(color)

    def update_screen(self):
        """
            Actually putting whatever was drawn on to the screen
        """
        end_drawing()

    def close_window(self):
        """
            Close the window when the game is exited
        """
        close_window()

    def is_quit(self):
        """
            Check to see if the X mark on the top right is clicked
        """
        return window_should_close()

    # def get_text_image(self):
    #     font = pygame.font.SysFont(font, font_size)
    #     text_image = font.render(text, antialias, color)

    def draw_text(self, text : str, font : str = None, font_size : int = 24, 
                    color : tuple = (0, 0, 0), position : tuple = (0, 0),
                    antialias : bool = True, position_center : bool = False):
        """
            Draw the input text (str).
            Inputs:
                - text: The text you want to draw
                - font: The font you want to use (This does not work for now...)
                - font_size: default is 24
                - color: An RGB tuple. (0,0,0) is BLACK, and (255,255,255) is WHITE
                        You can also pass a 4 entries tuple. the 4th entry determines opacity
                - position: A tuple in the form of (x, y)
                - antialias: Boolean. Default is True (This does not work for now)
                - position_center: A boolean that tells whether the position given should be
                                    the center of the text image or the top-left corner.
                        + True: treats the position as the center of the text image
                        + False: treats the position as the top-left corner of the text image

        """
        # The font and antialias parameters are ignored for now
        if position_center:
            text_image = image_text(text, font_size, color)
            draw_text(text, int(position[0] - text_image.width/2), int(position[1] - text_image.height/2), font_size, color)
            # draw_rectangle_lines(int(position[0] - text_image.width/2), int(position[1] - text_image.height/2), text_image.width, text_image.height, color)
        else:
            draw_text(text, int(position[0]), int(position[1]), font_size, color)

    def draw_rectangle(self, center : tuple, width : int, height: int, color : tuple = (0, 0, 0), 
                        border_width : int = 0, roundness : float = 0):
        """
            Draw a rectangle.

            Input:
                - center: An (x, y) tuple indicating the center of the rectangle
                - width: the width of the rectangle
                - height: the height of the rectangle
                - color: An RGB tuple. (0,0,0) is BLACK, and (255,255,255) is WHITE
                        You can also pass a 4 entries tuple. the 4th entry determines opacity
                - border_width: how many pixels you want the border to be
                
                - border_radius, border_..._radius: use these parameters if you want your rectangle
                                     to have rounded corners.
                                        + values < 1 means squared corners
                                        + values >= 1 means rounded corners. Increase this
                                            to increase the roundness
        """
        topleft_x, topleft_y = center[0] - width/2, center[1] - height/2
    
        if border_width == 0:
            draw_rectangle_rounded(Rectangle(topleft_x, topleft_y, width, height), roundness, 60, color)
        elif border_width > 0:
            draw_rectangle_rounded_lines(Rectangle(topleft_x, topleft_y, width, height), roundness, 60, border_width, color)
    
    def draw_circle(self, center, radius, color : tuple = (0, 0, 0), width : int = 0,
                    draw_top_right : bool = False, draw_top_left : bool = False, draw_bottom_left : bool = False, 
                    draw_bottom_right : bool = False):
        """
            Draw a circle.

            Input:
                - center: A tuple represents center of the circle (x, y)
                - radius: Well...
                - color: RGB tuple (0,0,0) is BLACK, (255,255,255) is WHITE.
                        Can also use 4th entry to specify opacity
                - width: How bold you want the border of the circle to be
                        0: filled circle
                        >0: empty circle with visible boundry line of 1px

                - draw_top_..., draw_bottom_...: Boolean. Use these parameters if want to draw
                    only parts of the circle (top left, top right, bottom left, bottom right)
        """
        sectors_key = (draw_top_right, draw_top_left, draw_bottom_left, draw_bottom_right)
        angles_data = circle_sectors_dict[sectors_key]
        separated_quads = isinstance(angles_data[0], tuple)

        if width == 0:
            if separated_quads:
                draw_circle_sector(Vector2(center[0], center[1]), radius, angles_data[0][0], angles_data[0][1], 60, color)
                draw_circle_sector(Vector2(center[0], center[1]), radius, angles_data[1][0], angles_data[1][1], 60, color)
            else:
                draw_circle_sector(Vector2(center[0], center[1]), radius, angles_data[0], angles_data[1], 60, color)
        elif width > 0:
            if sectors_key == (True, True, True, True) or sectors_key == (False, False, False, False):
                equiv_rec = Rectangle(center[0] - radius, center[1] - radius, 2*radius, 2*radius)
                draw_rectangle_rounded_lines(equiv_rec, 1, 60, width, color)
            # For now, if only part of the circle is drawn, "width" will be ignored
            elif separated_quads:
                draw_circle_sector_lines(Vector2(center[0], center[1]), radius, angles_data[0][0], angles_data[0][1], 60, color)
                draw_circle_sector_lines(Vector2(center[0], center[1]), radius, angles_data[1][0], angles_data[1][1], 60, color)
            else:
                draw_circle_sector_lines(Vector2(center[0], center[1]), radius, angles_data[0], angles_data[1], 60, color)

    def draw_actor(self, actor: Actor):
        """
            draw_actor():
                - Create the texture from the image whose path is stored in the actor
                - Use the dimensions and position of the actor to draw the texture to the screen
        """
        center = actor.get_position()
        path = actor.get_path()
        try:
            # Load image from cache or from file
            if path in self._textures_cache.keys():
                texture = self._textures_cache[path + "_f"] if actor.flipped() else self._textures_cache[path]
            else:
                texture = self._load_texture(actor)

            # width and height of the image
            frame_width = actor.get_width()
            frame_height = actor.get_height()
            
            draw_texture_pro(texture,
                            Rectangle(0,0,texture.width,texture.height),
                            Rectangle(center[0], center[1], frame_width, frame_height),
                            Vector2(frame_width/2, frame_height/2),
                            actor.get_rotation(),
                            WHITE)
                            
            if isinstance(actor, AnimatedActor):
                actor.set_next_frame()
                
            # This line of code when un-commented shows the hit box of the actor
            # draw_rectangle_lines(int(actor.get_top_left()[0]), int(actor.get_top_left()[1]), int(actor.get_width()), int(actor.get_height()),BLACK)
        except:
            print("Something went wrong in RaylibScreenService.draw_actor()! Maybe path is not found!")
            print(path)

    def draw_actors(self, actors : list, lerp : float = 0):
        """
            Draw all the actors in the "actors" list in order:
                    First thing in the list gets drawn first.

            actors: actors that need to be drawn
            lerp: linear interpolation (don't worry about this)
        """
        for actor in actors:
            self.draw_actor(actor)
        
    def release(self):
        """
            This might be used in the future
        """
        pass