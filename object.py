import os
import pygame
from user_request import *
from setting import *

# TODO : 將所有物件的圖片匯入 並調整至合適大小
# 同個物件 不同狀況(像是開啟/關閉)可以用相同名字，後面用tv-1 tv-2 做區分
# tv_image = [pygame.transform.scale(pygame.image.load(f"image/Object/Tv/tv-{i}.png"), (int(201), int(211))) for i in range(1)]
tv_image = [pygame.transform.scale(pygame.image.load(f"image/living_room/Tv/tv-{i}.png"), (GAME_WIDTH, GAME_HEIGHT)) for i in range(1)]
newspaper_image = [pygame.transform.scale(pygame.image.load(f"image/Object/Newspaper/newspaper-{i}.png"), (int(466//3), int(260//3))) for i in range(1)]

clock_image = pygame.transform.scale(pygame.image.load(f"image/living_room/Clock/clock.png"), (GAME_WIDTH, GAME_HEIGHT))
clock_open_image = pygame.transform.scale(pygame.image.load(f"image/living_room/Clock/clock_open.png"), (GAME_WIDTH, GAME_HEIGHT))
hr_image = [pygame.transform.scale(pygame.image.load(f"image/living_room/Clock/hr/hr-{i}.png"), (int(1920//2), int(1080//2))) for i in range(0,12)]
mins_image = [pygame.transform.scale(pygame.image.load(f"image/living_room/Clock/mins/mins-{i}.png"), (int(1920//2), int(1080//2))) for i in range(0,60,5)]

right_image = pygame.transform.scale(pygame.image.load(f"image/Icon/right.png"), (int(30), int(30)))
left_image = pygame.transform.scale(pygame.image.load(f"image/Icon/left.png"), (int(30), int(30)))
menu_image = pygame.transform.scale(pygame.image.load(f"image/Icon/menu.png"), (int(30), int(30)))
exit_image = pygame.transform.scale(pygame.image.load(f"image/Icon/left.png"), (int(30), int(30)))

door_image = pygame.transform.scale(pygame.image.load(f"image/Object/door.png"), (int(200), int(400)))
#yj
door_image_1  = pygame.transform.scale(pygame.image.load(f"image/living_room/Door/door_1.png"), (GAME_WIDTH, GAME_HEIGHT))
door_image_2  = pygame.transform.scale(pygame.image.load(f"image/living_room/Door/door_2.png"), (GAME_WIDTH, GAME_HEIGHT))
door_image_3  = pygame.transform.scale(pygame.image.load(f"image/living_room/Door/door_3.png"), (GAME_WIDTH, GAME_HEIGHT))
door_image_4  = pygame.transform.scale(pygame.image.load(f"image/living_room/Door/door_4.png"), (GAME_WIDTH, GAME_HEIGHT))
door_image_2_reverse  = pygame.transform.scale(pygame.image.load(f"image/study/door_2.png"), (GAME_WIDTH, GAME_HEIGHT))

desk_image = pygame.transform.scale(pygame.image.load(f"image/study/desk.png"), (GAME_WIDTH, GAME_HEIGHT))
book_image = pygame.transform.scale(pygame.image.load(f"image/study/book2.png"), (GAME_WIDTH, GAME_HEIGHT))
book_shelf_image = pygame.transform.scale(pygame.image.load(f"image/study/book_shelf.png"), (GAME_WIDTH, GAME_HEIGHT))
globe_image = pygame.transform.scale(pygame.image.load(f"image/study/Globe/globe.png"), (GAME_WIDTH, GAME_HEIGHT))
globe_table_image = pygame.transform.scale(pygame.image.load(f"image/study/Globe/globe_table.png"), (GAME_WIDTH, GAME_HEIGHT))
window_image = pygame.transform.scale(pygame.image.load(f"image/study/window.png"), (GAME_WIDTH, GAME_HEIGHT))
chest_image = pygame.transform.scale(pygame.image.load(f"image/study/chest.png"), (GAME_WIDTH, GAME_HEIGHT))
dropped_painting_image = pygame.transform.scale(pygame.image.load(f"image/study/dropped_painting.png"), (GAME_WIDTH, GAME_HEIGHT))
wife_1_image = pygame.transform.scale(pygame.image.load(f"image/Object/Wife/wife.png"), (GAME_WIDTH, GAME_HEIGHT))


handle_icon = pygame.transform.scale(pygame.image.load(f"image/Object/Wife/wife.png"), (GAME_WIDTH, GAME_HEIGHT))
password_hint_1_icon = pygame.transform.scale(pygame.image.load(f"image/Object/Wife/wife.png"), (GAME_WIDTH, GAME_HEIGHT))

# 待繪製物件
none_image = pygame.transform.scale(BACKGROUND_IMAGE, (100, 100))
none_icon = pygame.transform.scale(pygame.image.load(f"image/icon.png"), (45, 45))

# 選單按鈕
class MenuButton:
    def __init__(self, x, y):
        self.image = menu_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y):
            # 測試用
            print('menu btn been press')
            # TODO : 叫出暫停選單
            pass

class RightButton:
    def __init__(self, x, y):
        self.image = right_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y):
            return 'right'
        else:
            return 0

class LeftButton:
    def __init__(self, x, y):
        self.image = left_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y):
            return 'left'
        else:
            return 0

class ExitButton:
    def __init__(self, x, y):
        self.image = exit_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y):
            return 'stop_investigation'
        else:
            return 0

#yj
class DoorToBedRoom:
    def __init__(self, x, y):
        self.image = door_image_3
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'bedroom'
        else:
            return 0

#把所有doors存成class attribute，用room id來決定要用哪一個圖片
class DoorToLivingRoom:
    doors = [door_image_2_reverse, door_image]
    def __init__(self, x, y, room):
        self.image = self.doors[room]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'living_room'
        else:
            return 0
        
#yj living room通往外面的門
class DoorToExit:
    def __init__(self, x, y):
        self.image = door_image_1
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'exit' #亂打的
        else:
            return 0

#yj 往study的門
class DoorToStudy:
    def __init__(self, x, y):
        self.image = door_image_2
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'study'
        else:
            return 0
        
#yj 往kitchen的門
class DoorToKitchen:
    def __init__(self, x, y):
        self.image = door_image_4
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'kitchen'
        else:
            return 0

# 可互動物件大概會是這個架構

# TV 會用到的原件 ===========================================
class TvButton:
    def __init__(self, x, y, num):
        self.image = pygame.transform.scale(pygame.image.load(f"image/living_room/Tv/btn.png"), (50, 50))
        self.number = num
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x: int, y: int):
        # TODO : 再看看要回傳甚麼 以及怎麼監測
        if self.rect.collidepoint(x, y):
            # 測試
            print(self.number)

            return self.number
        else:
            return 0

# 可互動物件本身 ===========================================
class Tv:
    def __init__(self, x, y):
        self.image = tv_image[0]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

        # 下方要有儲存解謎進度的data
        # TODO : 點擊放大後的圖片
        self.focus = pygame.transform.scale(pygame.image.load(f"image/living_room/Tv/tv-investigation.png"), (GAME_WIDTH, GAME_HEIGHT))
        # TODO : 此圖片中可互動的物件
        self.object = [ExitButton(500,550),
                       TvButton(600,200,1),TvButton(700,200,2),TvButton(800,200,3),
                       TvButton(600,300,4),TvButton(700,300,5),TvButton(800,300,6),
                       TvButton(600,400,7),TvButton(700,400,8),TvButton(800,400,9)]

    def clicked(self, x: int, y: int):
        # TODO : 連接到 user_request 若是可互動物件被點到 轉換場景 若是不可互動則說話或是
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'investigation'

    # TODO : 用於改變在解謎中改動到的資料
    def puzzle(self):
        pass


# Clock 會用到的原件 ===========================================

# yj clock時針
class Hr:
    def __init__(self, x, y):
        self.index = 0
        self.image = hr_image[0]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.ans = 1 # 1點
        self.lock = False

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            # 檢查是否已解完
            if self.lock:
                return 'lock'
            if self.index == 11:
                self.index = 0
            else:
                self.index += 1
            self.image = hr_image[self.index]
            self.rect = self.image.get_rect()
            self.rect.center = (self.x, self.y)
            self.mask = pygame.mask.from_surface(self.image)
            return 'move'


# yj clock秒針
class Mins:
    def __init__(self, x, y):
        self.index = 0
        self.image = mins_image[0]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.ans = 9 #45分
        self.lock = False

    def clicked(self, x: int, y: int):

        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            # 檢查是否已解完
            if self.lock:
                return 'lock'
            if self.index == 11:
                self.index = 0
            else:
                self.index += 1
            self.image = mins_image[self.index]
            self.rect = self.image.get_rect()
            self.rect.center = (self.x, self.y)
            self.mask = pygame.mask.from_surface(self.image)
            return 'move'

# 可互動物件本身 ===========================================
#yj
class Clock:
    def __init__(self,x,y):
        self.image = clock_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.focus = pygame.transform.scale(pygame.image.load(f"image/living_room/Clock/clock-investigation.png"), (GAME_WIDTH, GAME_HEIGHT))
        # TODO : 此圖片中可互動的物件
        self.object = [ExitButton(500,550),
                       Mins(483,400),Hr(483,400)]
        self.hr_right = False
        self.min_right = False
        self.is_open = False
    
    def clicked(self, x: int, y: int):
        # TODO : 連接到 user_request 若是可互動物件被點到 轉換場景 若是不可互動則說話或是
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'investigation'
    def open(self):
        self.is_open = True
        self.image = clock_open_image
        self.object[1].lock = True
        self.object[2].lock = True
        self.focus = pygame.transform.scale(pygame.image.load(f"image/living_room/Clock/clock_open-investigation.png"), (GAME_WIDTH, GAME_HEIGHT))
        self.object = [ExitButton(500,550),Handle(300,200),Password_Hint_1(500,200)]



# NewPaper 會用到的原件 ===========================================


# 可互動物件本身 ===========================================
class NewPaper:
    def __init__(self, x, y):
        self.image = tv_image[0]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        # 下方要有儲存解謎進度的data
        # TODO : 點擊放大後的圖片
        self.focus = pygame.transform.scale(pygame.image.load(f"image/living_room/Tv/tv-investigation.png"), (GAME_WIDTH, GAME_HEIGHT))
        # TODO : 此圖片中可互動的物件
        self.object = [ExitButton(500,550)]

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y):
            return 'investigation'

    # TODO : 用於改變在解謎中改動到的資料
    def puzzle(self):
        pass

# Desk 會用到的原件 ===========================================
class Letter:
    def __init__(self, x, y, num):
        self.image = None
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x: int, y: int):
        # TODO : 再看看要回傳甚麼 以及怎麼監測
        if self.rect.collidepoint(x, y):
            # 測試
            print(self.number)

            return self.number
        else:
            return 0

# 可互動物件本身 ===========================================
class Desk:
    def __init__(self, x, y):
        self.image = desk_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

        # 下方要有儲存解謎進度的data
        # TODO : 點擊放大後的圖片
        self.focus = pygame.transform.scale(pygame.image.load(f"image/living_room/Tv/tv-investigation.png"), (GAME_WIDTH, GAME_HEIGHT))
        # TODO : 此圖片中可互動的物件
        self.object = [ExitButton(500,550)]

    def clicked(self, x: int, y: int):
        # TODO : 連接到 user_request 若是可互動物件被點到 轉換場景 若是不可互動則說話或是
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'investigation'

    # TODO : 用於改變在解謎中改動到的資料
    def puzzle(self):
        pass



# 我打算把他與書桌合併(圖片上) 就不必宣告這個class by hank
#不確定是不是可互動物件
class Book:
    def __init__(self, x, y):
        self.image = book_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
    
    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'none'

#可互動物件，investigation尚未完成
class BookShelf:
    def __init__(self, x, y):
        self.image = book_shelf_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'none'

#可互動物件，investigation尚未完成
class Globe:
    def __init__(self, x, y):
        self.image = globe_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'none'

#可互動物件，investigation尚未完成        
class DroppedPainting:
    def __init__(self, x, y):
        self.image = dropped_painting_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'none'


# 非可互動物件
class Window:
    def __init__(self, x, y):
        self.image = window_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x - self.rect.x, y - self.rect.y)) != 0:
            return 'none'


# 非可互動物件
class GlobeTable:
    def __init__(self, x, y):
        self.image = globe_table_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x - self.rect.x, y - self.rect.y)) != 0:
            return 'none'


# 非可互動物件
class Chest:
    def __init__(self, x, y):
        self.image = chest_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x - self.rect.x, y - self.rect.y)) != 0:
            return 'none'

# 對話物件 ===========================================
class Wife_Ch1:
    def __init__(self, x, y):
        self.image = wife_1_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        # 對話內容
        self.text = ["要是能回到過去該有多好⋯","你找到遺產了嗎?"]
        self.text_index = 0
        self.text_size = 2


    def clicked(self, x: int, y: int):
        # TODO : 連接到 user_request 若是可互動物件被點到 轉換場景 若是不可互動則說話或是
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            return 'speak'


# 物品欄物件(可放入物品欄的東西)
class Handle:
    def __init__(self, x, y):
        self.image = none_image
        # 放入物品欄後顯示的圖示
        self.icon = none_icon
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        # 物件狀況
        # 被檢起
        self.in_bag = False
    # TODO : 一些交互用函式
    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            # 被撿起放入物品欄
            return 'take'

class Password_Hint_1:
    def __init__(self, x, y):
        self.image = none_image
        self.icon = none_icon
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        # 物件狀況
        # 被檢起
        self.in_bag = False
    # TODO : 一些交互用函式

    def clicked(self, x: int, y: int):
        if self.rect.collidepoint(x, y) and self.mask.get_at((x -  self.rect.x, y -  self.rect.y)) != 0:
            # 被撿起放入物品欄
            return 'take'