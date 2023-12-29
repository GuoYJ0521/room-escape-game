import pygame
import os

from wall import *

living_room_1_image = pygame.transform.scale(pygame.image.load(f"image/living_room/Wall/living_room_1.png"), (GAME_WIDTH, GAME_HEIGHT))
living_room_2_image = pygame.transform.scale(pygame.image.load(f"image/living_room/Wall/living_room_2.png"), (GAME_WIDTH, GAME_HEIGHT))
living_room_3_image = pygame.transform.scale(pygame.image.load(f"image/living_room/Wall/living_room_3.png"), (GAME_WIDTH, GAME_HEIGHT))
living_room_4_image = pygame.transform.scale(pygame.image.load(f"image/living_room/Wall/living_room_4.png"), (GAME_WIDTH, GAME_HEIGHT))
bedroom_1_image = pygame.transform.scale(pygame.image.load(f"image/black.png"), (GAME_WIDTH, GAME_HEIGHT))
bedroom_2_image = pygame.transform.scale(pygame.image.load(f"image/black.png"), (GAME_WIDTH, GAME_HEIGHT))
bedroom_3_image = pygame.transform.scale(pygame.image.load(f"image/black.png"), (GAME_WIDTH, GAME_HEIGHT))
bedroom_4_image = pygame.transform.scale(pygame.image.load(f"image/black.png"), (GAME_WIDTH, GAME_HEIGHT))
study_1_image = pygame.transform.scale(pygame.image.load(f"image/study/Wall/study_1.png"), (GAME_WIDTH, GAME_HEIGHT))
study_2_image = pygame.transform.scale(pygame.image.load(f"image/study/Wall/study_2.png"), (GAME_WIDTH, GAME_HEIGHT))
study_3_image = pygame.transform.scale(pygame.image.load(f"image/study/Wall/study_3.png"), (GAME_WIDTH, GAME_HEIGHT))

# 章節1的所有房間/牆面
#yj
class LivingRoom:
    def __init__(self):
        # data
        # 房間背景
        self.bg_image = [living_room_1_image, living_room_2_image, living_room_3_image,living_room_4_image]

        # 房間牆面數
        self.wall_size = 4

        # 切換畫面鍵
        self.right_button = RightButton(WIN_WIDTH - 50,WIN_HEIGHT/2)
        self.left_button = LeftButton(20,WIN_HEIGHT/2)

        # 此房間在不同牆面有的物品/座標 (包括移動鍵)
        # 牆面1有這些東西
        self.__object_1 = [self.right_button,self.left_button,
                           DoorToExit(GAME_X, GAME_Y),LivingRoomWindow(GAME_X, GAME_Y)]
        # 牆面2有這些東西
        self.__object_2 = [self.right_button,self.left_button,
                           DoorToBedRoom(GAME_X, GAME_Y),Clock(GAME_X, GAME_Y),BookShelf(GAME_X, GAME_Y)]
        # 牆面3有這些東西
        self.__object_3 = [self.right_button,self.left_button,DoorToKitchen(GAME_X, GAME_Y),
                           Tv(GAME_X, GAME_Y,True),TvShelf(GAME_X, GAME_Y), Painting(GAME_X, GAME_Y),Globe(GAME_X, GAME_Y),GlobeTable(GAME_X, GAME_Y)]
        self.__object_4 = [self.right_button, self.left_button,Desk(GAME_X, GAME_Y),Calendar(GAME_X, GAME_Y),TrashCan(GAME_X, GAME_Y)]

        # 當前牆面/建立此房間的牆面
        # 不同房間的牆面數會不一樣 要注意
        self.wall = {'1': Wall(self.bg_image,self.__object_1),
                     '2': Wall(self.bg_image,self.__object_2),
                     '3': Wall(self.bg_image,self.__object_3),
                     '4': Wall(self.bg_image,self.__object_4)}

class Study:
    def __init__(self):
        # data
        # 房間背景
        self.bg_image = [study_1_image, study_2_image, study_3_image]

        # 房間牆面數
        self.wall_size = 3

        # 切換畫面鍵
        self.right_button = RightButton(WIN_WIDTH - 50, WIN_HEIGHT / 2)
        self.left_button = LeftButton(20, WIN_HEIGHT / 2)

        # 此房間在不同牆面有的物品/座標
        # 牆面1有這些東西
        self.__object_1 = [self.right_button,self.left_button,Desk(GAME_X, GAME_Y),Book(GAME_X, GAME_Y), Painting(GAME_X, GAME_Y)]
        # 牆面2有這些東西
        self.__object_2 = [self.right_button,self.left_button,BookShelf(GAME_X, GAME_Y),Globe(GAME_X, GAME_Y),GlobeTable(GAME_X, GAME_Y),Window(GAME_X, GAME_Y)]
        # 牆面3有這些東西
        self.__object_3 = [self.right_button,self.left_button,DoorToLivingRoom(GAME_X, GAME_Y, 0),DroppedPainting(GAME_X, GAME_Y)]
        # 當前牆面/建立此房間的牆面
        # 不同房間的牆面數會不一樣 要注意
        self.wall = {'1': Wall(self.bg_image, self.__object_1),
                     '2': Wall(self.bg_image, self.__object_2),
                     '3': Wall(self.bg_image, self.__object_3)}

class Kitchen:
    def __init__(self):
        # data
        # 房間背景
        self.bg_image = [living_room_1_image, living_room_2_image, living_room_3_image]

        # 房間牆面數
        self.wall_size = 3

        # 切換畫面鍵
        self.right_button = RightButton(WIN_WIDTH - 50, WIN_HEIGHT / 2)
        self.left_button = LeftButton(20, WIN_HEIGHT / 2)

        # 此房間在不同牆面有的物品/座標
        # 牆面1有這些東西
        self.__object_1 = [self.right_button,self.left_button]
        # 牆面2有這些東西
        self.__object_2 = [self.right_button,self.left_button]
        # 牆面3有這些東西
        self.__object_3 = [self.right_button,self.left_button]

        # 當前牆面/建立此房間的牆面
        # 不同房間的牆面數會不一樣 要注意
        self.wall = {'1': Wall(self.bg_image, self.__object_1),
                     '2': Wall(self.bg_image, self.__object_2),
                     '3': Wall(self.bg_image, self.__object_3)}

class Bedroom:
    def __init__(self):
        # data
        # 房間背景
        self.bg_image = [bedroom_1_image, bedroom_2_image, bedroom_3_image, bedroom_4_image]

        # 房間牆面數
        self.wall_size = 4

        # 切換畫面鍵
        self.right_button = RightButton(WIN_WIDTH - 50, WIN_HEIGHT / 2)
        self.left_button = LeftButton(20, WIN_HEIGHT / 2)

        # 此房間在不同牆面有的物品/座標
        # 牆面1有這些東西
        self.__object_1 = [self.right_button,self.left_button]
        # 牆面2有這些東西
        self.__object_2 = [self.right_button,self.left_button]
        # 牆面3有這些東西
        self.__object_3 = [self.right_button,self.left_button,DoorToLivingRoom(GAME_X, GAME_Y, 0)]
        # 牆面4有這些東西
        self.__object_4 = [self.right_button,self.left_button]

        # 當前牆面/建立此房間的牆面
        # 不同房間的牆面數會不一樣 要注意
        self.wall = {'1': Wall(self.bg_image, self.__object_1),
                     '2': Wall(self.bg_image, self.__object_2),
                     '3': Wall(self.bg_image, self.__object_3),
                     '4': Wall(self.bg_image, self.__object_4)}