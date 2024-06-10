import os
import pygame


class IMAGE_TOOL:
    @staticmethod
    def img_crop_paste_scale(sheet, x, y, width, height, colorkey, scale):
        img = pygame.Surface((width, height))
        img.blit(sheet, (0, 0), (x, y, width, height))
        img.set_colorkey(colorkey)
        img = pygame.transform.scale(img, (int(width * scale), int(height * scale)))
        return img

    @staticmethod
    def img_scale(sheet, target_w, target_h, scale):
        src_w, src_h = sheet.get_size()
        scale_w = target_w / src_w
        scale_h = target_h / src_h
        img = pygame.transform.scale(sheet, (int(target_w*scale), int(target_h*scale)))
        return img, (scale_w*scale, scale_h*scale)

    @staticmethod
    def load_img(img_dir, accept=[".jpg", ".png", ".bmp", ".gif"]):
        result = dict()
        names = os.listdir(img_dir)
        for name in names:
            basename, ext = os.path.splitext(name)
            if ext not in accept:
                continue
            img_path = os.path.join(img_dir, name)
            img = pygame.image.load(img_path)
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
            result[name] = img
        return result
