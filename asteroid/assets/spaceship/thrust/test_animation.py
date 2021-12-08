import pygame
from genie_plugins.services.PygameKeyboardService import PygameKeyboardService

FPS = 60
W_SIZE = (900, 500)
W_CENTER = (450, 250)

WIN = pygame.display.set_mode(W_SIZE)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0, 0)
VEL = 5
ANIMATION_SPEED = 0.2
SPARK_SIZE = (15, 20)
CIRCLE_COOR = {"x": 300, "y":300}

class AnimationSprite:
    def __init__(self, images, position):
        
        self.x = position[0]
        self.y = position[1]

        self._images = images
        self._current_index = 0
        self._is_being_drawn = True
        self._is_animating = True
    
    def get_current_image(self):
        print(int(self._current_index))
        image = self._images[int(self._current_index)]
        if (self._is_animating):
            self._current_index = (self._current_index + ANIMATION_SPEED) % 3
        return image
    
    def set_animating(self, animating):
        self._is_animating = animating
    
    def get_animating(self):
        return self._is_animating
    
    def set_being_drawn(self, is_drawn):
        self._is_being_drawn = is_drawn

    def is_being_drawn(self):
        return self._is_being_drawn

    def reset_animation(self):
        self._current_index = 0
    
    def get_position(self):
        return (self.x, self.y)

def draw_frame(*animation_sprites):
    WIN.fill(BLACK)

    pygame.draw.circle(WIN, WHITE, (CIRCLE_COOR["x"], CIRCLE_COOR["y"]), 10, 5)
    for sprite in animation_sprites:
        if (sprite.is_being_drawn()):
            WIN.blit(sprite.get_current_image(), sprite.get_position())

    pygame.display.update()

def main():
    running = True
    clock = pygame.time.Clock()
    
    btm_imgs = []
    btm_imgs.append(pygame.transform.scale(pygame.image.load('thrust_1.png'), SPARK_SIZE))
    btm_imgs.append(pygame.transform.scale(pygame.image.load('thrust_2.png'), SPARK_SIZE))
    btm_imgs.append(pygame.transform.scale(pygame.image.load('thrust_3.png'), SPARK_SIZE))
    
    lft_imgs = []
    lft_imgs.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('thrust_1.png'), SPARK_SIZE), 270))
    lft_imgs.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('thrust_2.png'), SPARK_SIZE), 270))
    lft_imgs.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('thrust_3.png'), SPARK_SIZE), 270))

    rgt_imgs = []
    rgt_imgs.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('thrust_1.png'), SPARK_SIZE), 90))
    rgt_imgs.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('thrust_2.png'), SPARK_SIZE), 90))
    rgt_imgs.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('thrust_3.png'), SPARK_SIZE), 90))
    
    bs_pos = (CIRCLE_COOR["x"] - 8, CIRCLE_COOR["y"] + 12)
    lft_pos = (bs_pos[0] - 25, bs_pos[1] - 20)
    rgt_pos = (bs_pos[0] + 20, bs_pos[1] - 20)

    bottom_spark = AnimationSprite(btm_imgs, bs_pos)
    left_spark = AnimationSprite(lft_imgs, lft_pos)
    right_spark = AnimationSprite(rgt_imgs, rgt_pos)

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys_state = pygame.key.get_pressed()

        if (keys_state[pygame.K_UP]):
            bottom_spark.set_being_drawn(True)
            CIRCLE_COOR["y"] -= VEL
            bottom_spark.y -= VEL
            left_spark.y -= VEL
            right_spark.y -= VEL
        else:
            bottom_spark.set_being_drawn(False)
        
        if (keys_state[pygame.K_LEFT]):
            right_spark.set_being_drawn(True)
            CIRCLE_COOR["x"] -= VEL
            bottom_spark.x -= VEL
            left_spark.x -= VEL
            right_spark.x -= VEL
        else:
            right_spark.set_being_drawn(False)
        
        if (keys_state[pygame.K_RIGHT]):
            left_spark.set_being_drawn(True)
            CIRCLE_COOR["x"] += VEL
            bottom_spark.x += VEL
            left_spark.x += VEL
            right_spark.x += VEL
        else:
            left_spark.set_being_drawn(False)
        
        if (keys_state[pygame.K_DOWN]):
            CIRCLE_COOR["y"] += VEL
            bottom_spark.y += VEL
            left_spark.y += VEL
            right_spark.y += VEL


        draw_frame(bottom_spark, left_spark, right_spark)

    pygame.quit()

if __name__ == "__main__":
    main()