import pygame
from config.config import CONFIG as cfg


class Info:
    def __init__(self) -> None:
        self.labels = []
        self.create_labels()

    def create_labels(self):
        self.labels.append(
            [
                self._create_single_label(
                    "press enter to continue...", (255, 255, 255), 30
                ),
                (10, cfg.screen_height - 40),
            ]
        )

    def _create_single_label(self, txt, color, size):
        font = pygame.font.SysFont(cfg.font_name, size)
        image_txt = font.render(txt, 1, color)
        return image_txt

    def draw(self, surface):
        for label in self.labels:
            surface.blit(label[0], label[1])
