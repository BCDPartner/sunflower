import pygame
from config.config import CONFIG as cfg
from source.component.boy import Boy
from source.component.info import Info


class Game:
    def __init__(self) -> None:
        screen_w = cfg.screen_width
        screen_h = cfg.screen_height

        # 初始化
        pygame.init()
        pygame.display.set_mode((screen_w, screen_h))
        pygame.display.set_caption(cfg.window_name)
        self.screen = pygame.display.get_surface()
        # 加载背景图
        self.bgimg = pygame.image.load(cfg.bgimg_path)
        self.clock = pygame.time.Clock()
        # 创建人物精灵
        self.boy = Boy()
        self.group = pygame.sprite.Group()
        self.group.add(self.boy)
        # 文字信息
        self.info = Info()
        
    def run(self):
        # 开始游戏
        while True:
            # 鼠标事件监控
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # 退出游戏
                    pygame.display.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()#键盘所有按键的状态
                    self.boy.update(keys)

                # 背景
                self.screen.blit(self.bgimg, (0, 0))
                pygame.display.update()
                self.clock.tick(cfg.frame)
            # self.group.draw(self.screen)
            self.info.draw(self.screen)
            pygame.display.update()
            self.clock.tick(cfg.frame)
