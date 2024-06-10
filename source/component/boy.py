import os
import pygame
from config.config import CONFIG as cfg
from source.component.utils import IMAGE_TOOL


class Boy(pygame.sprite.Sprite):
    def __init__(self, *groups) -> None:
        super(Boy, self).__init__(*groups)
        self.boys = []
        self.load_boys()
        self.boy_ind = 0
        self.image = self.boys[self.boy_ind]
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 300
        self.state_num = len(self.boys)
        self.face_right = True

    def load_boys(self):
        boys = IMAGE_TOOL.load_img(cfg.boy)
        length = len(boys)
        for i in range(length):
            boy, _ = IMAGE_TOOL.img_scale(
                boys["%d.png" % (i + 1)], cfg.boy_size[0], cfg.boy_size[1], 1
            )
            self.boys.append(boy)

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            #更新人物运动状态
            self.update_motion()
            #更新朝向
            if self.face_right:
                self.image = pygame.transform.flip(self.image, True, False)#水平翻转
                self.face_right = False
            #按左键，向左移动10像素
            self.rect.x -= cfg.boy_step

        elif keys[pygame.K_RIGHT]:
            #更新人物运动状态
            self.update_motion()
            #更新朝向
            if not self.face_right:
                self.image = pygame.transform.flip(self.image, True, False)#水平翻转
                self.face_right = True
            #按右键，向右移动10像素
            self.rect.x += cfg.boy_step

    def update_motion(self):
        #更新人物运动状态
        self.boy_ind += 1
        self.boy_ind = self.boy_ind % self.state_num
        self.image = self.boys[self.boy_ind]
        self.face_right = True 
