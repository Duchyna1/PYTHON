import pygame


class Tank(pygame.sprite.Sprite):
    def __init__(self, pScreen, pX, pY, pRotation, pColor, pBullet):
        self.screen = pScreen
        self.x, self.y = pX, pY
        self.color = pColor
        self.bullet = pBullet
        self.rotation = pRotation

        self.WIDTH, self.HEIGHT = 25, 25

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([self.WIDTH, self.HEIGHT])
        self.image.fill(self.color)

        self.rect = self.image.get_rect()

    def update(self, *args):
        pos = pygame.mouse.get_pos()
        self.rect.center = pos

    def rotate(self, pRotation):
        center = self._Rect.center
        rotate = pygame.transform.rotate
        self.image = rotate(self.rotation, pRotation)
        self.rotation += pRotation
        self.rect = self.image.get_rect(center=center)

    def shoot(self):
        self.bullet.shoot()


    def destroy(self):
        super().kill()
