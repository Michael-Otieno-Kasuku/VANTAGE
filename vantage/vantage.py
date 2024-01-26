import math
import csv
from pygame import Color
import os
import pygame
import sys
from pygame.locals import *
from pygame.font import Font
import json
import datetime as dt
from enum import Enum
import random

class LevelGenerator:
    @staticmethod
    def ease_in(a , b, p):
        return a + (b - a) * (p**2)
    
    @staticmethod
    def ease_out(a , b ,p):
        return a +(b - a)*(1 - ((1 - p)**2))
    
    @staticmethod
    def ease_in_out(a , b, p):
        return a + (b - a) * ((-math.cos(p * math.pi) / 2) + 0.5)
    
    @staticmethod
    def add_corner(enter, hold, exit, curve, start_y=0, height=0):
        segments = []
        peak = height * 260
        total = float(enter + hold + exit)
        last_y = start_y
        next_y = start_y

        for n in range(enter):
            last_y=next_y
            next_y = LevelGenerator.ease_in_out(start_y, peak, n/total)

            segments.append([LevelGenerator.ease_in(0,curve,n/enter),last_y,next_y])

        for n in range(hold):
            last_y = next_y
            next_y = LevelGenerator.ease_in_out(start_y, peak,(n + enter) / total)

            segments.append([curve,last_y,next_y])

        for n in range(exit):
            last_y = next_y
            next_y = LevelGenerator.ease_in_out(start_y,peak,(n + enter + hold) / total)

            segments.append([LevelGenerator.ease_in_out(curve,0,n/exit),last_y,next_y])
        
        return segments
    
    @staticmethod
    def add_hill(enter,hold,exit,height,start_y):
        segments = []
        peak = height * 260
        total = float(enter+hold+exit)
        y = start_y
        last_y = 0

        for n in range(enter):
            last_y = y
            y = LevelGenerator.ease_in_out(start_y,peak,n/total)
            segments.append([0,last_y,y])
        
        for n in range(hold):
            last_y = y
            y = LevelGenerator.ease_in_out(start_y,peak,(n+enter)/total)
            segments.append([0,last_y,y])
        
        for n in range(exit):
            last_y = y
            y=LevelGenerator.ease_in_out(start_y,peak,(n+enter+hold)/total)
            segments.append([0,last_y,y])
        
        return segments
    

    @staticmethod
    def add_straight(length,y):
        segments = []

        for n in range(length):
            segments.append([0,y,y])
        
        return segments
    
    @staticmethod
    def last_y(segments):
        return segments[-1][-1]
    
    @staticmethod
    def write(path,segments):
        with open(path,"w") as csvfile:
            w = csv.writer(csvfile)
            for row in segments:
                w.writerow(row)

class Melbourne:
    @staticmethod
    def create():
        segments = []
        sprites = []
        name = "melbourne"

        segments += LevelGenerator.add_straight(100,0)
        segments += LevelGenerator.add_hill(50, 50, 50, 40, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_straight(500, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_hill(30, 30, 30, 20, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_straight(200, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_corner(30,45,40,6, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_straight(90, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_hill(30,30,30,0, LevelGenerator.last_y(segments))

        segments += LevelGenerator.add_straight(150, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_corner(30, 45,40,6, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_straight(200, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_hill(80,80,80, 40, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_hill(20,20,20, 35, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_straight(50, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_hill(20, 20,20, 20, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_corner(30,45,40,-6, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_corner(30,45,40,4, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_straight(50, LevelGenerator.last_y(segments))

        segments += LevelGenerator.add_hill(20, 20,20, 40, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_straight(50, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_corner(25,45,25,5, LevelGenerator.last_y(segments),30)
        segments += LevelGenerator.add_corner(25,45,25,-5, LevelGenerator.last_y(segments),20)
        segments += LevelGenerator.add_corner(25,45,25,5, LevelGenerator.last_y(segments),10)
        segments += LevelGenerator.add_corner(25,45,25,-5, LevelGenerator.last_y(segments),0)
        segments += LevelGenerator.add_straight(300, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_corner(120,120,120,-6, LevelGenerator.last_y(segments),-6)
        segments += LevelGenerator.add_straight(200, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_corner(120,200,120,6, LevelGenerator.last_y(segments),0)
        segments += LevelGenerator.add_straight(300, LevelGenerator.last_y(segments))

        LevelGenerator.write(f"{name}.csv", segments)

class GoldCoast:
    @staticmethod
    def create():
        segments = []
        sprites = []
        name = "goldcoast"

        segments += LevelGenerator.add_straight(100,0)
        segments += LevelGenerator.add_corner(30,85,40,5,0,20)
        segments += LevelGenerator.add_straight(100, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_corner(30,45,40,4, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_corner(30,45,40,-6, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_corner(30,45,40,6, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_corner(30,45,40,-4, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_hill(25,25,25,0, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_straight(150,0)

        segments += LevelGenerator.add_corner(30,85,20,5,0,20)
        segments += LevelGenerator.add_corner(20,85,40,5, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_corner(80,45,40,6, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_corner(70,45,100,-6, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_hill(25,25,25,25, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_straight(20, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_hill(25,25,25,0, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_corner(140,220,140,5, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_hill(25,25,25,15, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_straight(5, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_hill(25,25,25,5, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_straight(5, LevelGenerator.last_y(segments))

        segments += LevelGenerator.add_hill(25,25,25,20, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_straight(5, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_hill(25,25,25,0, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_straight(5, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_hill(25,25,25,25, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_straight(5, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_hill(25,25,25,0, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_straight(40,0)

        segments += LevelGenerator.add_corner(30,55,40,5,0,25)
        segments += LevelGenerator.add_straight(40, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_corner(30,55,40,5, LevelGenerator.last_y(segments),0)
        segments += LevelGenerator.add_straight(40, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_corner(20,20,20,3, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_corner(20,20,20,-3, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_corner(20,20,20,3, LevelGenerator.last_y(segments))

        segments += LevelGenerator.add_corner(20,20,20,-3, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_corner(20,20,20,3, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_corner(20,20,20,-3, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_corner(20,20,20,5, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_corner(20,20,20,-5, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_corner(20,20,20,5, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_corner(20,20,20,-5, LevelGenerator.last_y(segments))
        segments += LevelGenerator.add_straight(100, LevelGenerator.last_y(segments))

        LevelGenerator.write(f"{name}.csv", segments)

class GameSetting:
    FPS                     = 60
    TITLE_FPS               = 20
    COUNTDOWN_FPS           = 1
    PLAYER_SELECT_FPS       = 10
    CREDITS_FPS             = 10
    LEVEL_OVER_LAG          = 8 * FPS
    TITLE_SCREEN            = True
    COUNTDOWN               = True
    PLAYER_SELECT           = True
    FULL_SCREEN             = True
    FRAME_RATE              =  (1.0/FPS)
    DIMENSIONS              = (640,480)
    MUSIC_VOLUME            = 0.8
    SEGMENT_HEIGHT          = 260
    RUMBLE_LENGTH           = 3
    DRAW_DISTANCE           = 125
    ROAD_WIDTH              = 2100
    LANES                   = 4
    BOUNDS                  = 2.1
    TUNNEL_BOUNDS           = 0.85
    TUNNEL_HEIGHT           = 90
    TUNNEL_LIGHT_FREQ       = 15
    AUTO_DRIVE              = False
    PLAYER_ANIM_HOLD        = 8
    CHECKPOINT              = 240
    LAP_DIFFICULTY_FACTOR   = 2
    LAPS_PER_LEVEL           = 1
    MINIMUM_DIFFICULTY      = 3
    MINIMUM_ENGINE_DIST     = 4000
    CRASH_DIVISOR           = 2
    POINTS                  = 15
    CHANCE_OF_BONUSES       = 3
    POINT_GAIN_PROSTITUTE   = 500
    POINT_LOSS_SPRITE       = 0.03
    POINT_LOSS_COMP         = 0.02
    POINT_MILESTONE         = 20000
    MINIMUM_CORNER_SMOKE    = 3
    FIELD_OF_VIEW           = 100 #Degrees
    CAMERA_HEIGHT           = 1300
    CAMERA_DEPTH            = 1/math.tan((FIELD_OF_VIEW/2)*math.pi/180)
    BOTTOM_OFFSET           = 5
    SPEED_BOOST_DECREASE    = 0.004
    SPEED_BOOST_LENGTH      = 50
    HARD_TOP_SPEED          = [(SEGMENT_HEIGHT/(1.0/FPS))*1.5,(SEGMENT_HEIGHT/(1.0/FPS))*2.4]
    HARD_HANDLING           = [0.1,0.45]
    HARD_ACCELERATION       = [2.0,7.0]
    PLAYER_Z                = (CAMERA_HEIGHT*CAMERA_DEPTH)
    BONUS_AMOUNT            = 3
    FONTS                   = {
        "retro_computer": os.path.join("assets/fonts","PressStart2P.ttf"),
        "fipps"         : os.path.join("assets/fonts","Fipps-Regular.otf")
    }
    COLOURS                 = {
        "white": Color(255,255,255),
        "opaque_white": Color(255,255,255,80),
        "text": Color(172,199,252),
        "dark_text": Color(57,84,137),
        "selection": [Color(172,199,252),Color(100,149,252)],
        "sky": Color(10,10,10),
        "gutter": Color(100,100,100),
        "red": Color(204,0,0),
        "bonus_a": Color(255,78,0),
        "bonus_b": Color(255,178,0),
        "green": Color(0,204,0),
        "black": Color(0,0,0),
        "tunnel": Color(38,15,8)
    }
    LEVELS                  =[
        {
            "id": "melbourne",
            "name": "Melbourne",
            "song": "lazerhawk-overdrive.ogg",
            "laps": LAPS_PER_LEVEL,
            "colours": {
                "wall": Color(32,32,32),
                "light": {
                    "road": Color(34,54,56),
                    "grass": Color(0,30,70),
                    "footpath": Color(82,96,115),
                    "line": Color(185, 185, 185)
                },
                "dark":{
                    "road": Color(48,64,81),
                    "grass": Color(0,16,56),
                    "footpath": Color(68,84,101),
                    "line": Color(185,185,185)
                }
            },
            "backgrounds": [
                {
                    "id": "night_sky",
                    "speed": 2,
                    "convert": True,
                    "scale": False
                },
                {
                    "id": "city",
                    "speed": 1,
                    "convert": False,
                    "scale": True
                }
            ]
        },
        {
            "id": "goldcoast",
            "name": "Gold Coast",
            "song": "timecop1983-summerheat.ogg",
            "laps": LAPS_PER_LEVEL,
            "colours": {
                "wall": Color(92,92,92),
                "light": {
                    "road": Color(64,84,86),
                    "grass": Color(136,236,125),
                    "footpath": Color(112,126,145),
                    "line": Color(185,185,185)
                },
                "dark": {
                    "road": Color(78,94,111),
                    "grass": Color(116,216,105),
                    "footpath": Color(98,114,131),
                    "line": Color(185,185,185)
                }
            },
            "backgrounds": [
                {
                    "id": "sunny_sky",
                    "speed": 2,
                    "convert": True,
                    "scale": False
                },
                {
                    "id": "beach",
                    "speed": 1,
                    "convert": False,
                    "scale": True
                }
            ]
        },
        {
            "id": "nullarbor",
            "name": "Nullarbor Desert",
            "song": "alvernagunn-maddog.ogg",
            "laps": LAPS_PER_LEVEL,
            "colours": {
                "wall": Color(92,92,92),
                "light": {
                    "road": Color(64,84,86),
                    "grass": Color(136,236,125),
                    "footpath": Color(112,126,145),
                    "line": Color(185,185,185)
                },
                "dark": {
                    "road": Color(78,94,111),
                    "grass": Color(116,216,105),
                    "footpath": Color(98,114,131),
                    "line": Color(185,185,185)
                }
            },
            "backgrounds": [
                {
                    "id": "sunny_sky",
                    "speed": 2,
                    "convert": True,
                    "scale": False
                },
                {
                    "id": "beach",
                    "speed": 1,
                    "convert": False,
                    "scale": True
                }
            ]
        }
    ]
    PLAYERS = [
        {
            "name": "Smervin' Mervin",
            "age": 48,
            "top_speed": (SEGMENT_HEIGHT / (1.0 / FPS)) * 1.9,
            "offroad_top_speed_factor": 2.0,
            "acceleration_factor": 4.6,
            "deceleration": 2.3,
            "centrifugal_force": 0.261,
            "city": "Melbourne , VIC",
            "select_sfx": "swervin_mervin_select.ogg",
            "sprites": {
                "mugshot_small": {
                    "path": "swervin_mervin_small.png",
                    "width": 60,
                    "height": 60
                },
                "mugshot_large": {
                    "path": "swervin_mervin_large.png",
                    "width": 320,
                    "height": 400
                },
                "straight1": {
                    "path": "straight1.png",
                    "width": 80,
                    "height": 50
                },
                "straight2": {
                    "path": "straight2.png",
                    "width": 80,
                    "height": 50
                },
                "left1": {
                    "path": "left1.png",
                    "width": 80,
                    "height": 50
                },
                "left2": {
                    "path": "left2.png",
                    "width": 80,
                    "height": 50
                },
                "right1": {
                    "path": "right1.png",
                    "width": 80,
                    "height": 50
                },
                "right2": {
                    "path": "right2.png",
                    "width": 80,
                    "height": 50
                },
                "left_smoke1": {
                    "path": "left_smoke1.png",
                    "width": 100,
                    "height": 56
                },
                "left_smoke2": {
                    "path": "left_smoke2.png",
                    "width": 100,
                    "height": 56
                },
                "right_smoke1": {
                    "path": "right_smoke1.png",
                    "width": 100,
                    "height": 56
                },
                "right_smoke2": {
                    "path": "right_smoke2.png",
                    "width": 100,
                    "height": 56
                },
                "uphill_straight1": {
                    "path": "uphill_straight1.png",
                    "width": 80,
                    "height": 56
                },
                "uphill_straight2": {
                    "path": "uphill_straight2.png",
                    "width": 80,
                    "height": 56
                },
                "uphill_left1": {
                    "path": "uphill_left1.png",
                    "width": 80,
                    "height": 56
                },
                "uphill_left2": {
                    "path": "uphill_left2.png",
                    "width": 80,
                    "height": 56
                },
                "uphill_right1": {
                    "path": "uphill_right1.png",
                    "width": 80,
                    "height": 56
                },
                "uphill_right2": {
                    "path": "uphill_right2.png",
                    "width": 80,
                    "height": 56
                },
                "uphill_left_smoke1": {
                "path": "uphill_left_smoke1.png",
                "width": 100,
                "height": 56
                },
                "uphill_left_smoke2": {
                    "path": "uphill_left_smoke2.png",
                    "width": 100,
                    "height": 56
                },
                "uphill_right_smoke1": {
                    "path": "uphill_right_smoke1.png",
                    "width": 100,
                    "height": 56
                },
                "uphill_right_smoke2": {
                    "path": "uphill_right_smoke2.png",
                    "width": 100,
                    "height": 56
                },
                "downhill_straight1": {
                    "path": "downhill_straight1.png",
                    "width": 80,
                    "height": 56
                },
                "downhill_straight2": {
                    "path": "downhill_straight2.png",
                    "width": 80,
                    "height": 56
                },
                "downhill_left1": {
                    "path": "downhill_left1.png",
                    "width": 80,
                    "height": 56
                },
                "downhill_left2": {
                    "path": "downhill_left2.png",
                    "width": 80,
                    "height": 56
                },
                "downhill_right1": {
                    "path": "downhill_right1.png",
                    "width": 80,
                    "height": 56
                },
                "downhill_right2": {
                    "path": "downhill_right2.png",
                    "width": 80,
                    "height": 56
                },
                "downhill_left_smoke1": {
                    "path": "downhill_left_smoke1.png",
                    "width": 100,
                    "height": 56
                },
                "downhill_left_smoke2": {
                    "path": "downhill_left_smoke2.png",
                    "width": 100,
                    "height": 56
                },
                "downhill_right_smoke1": {
                    "path": "downhill_right_smoke1.png",
                    "width": 100,
                    "height": 56
                },
                "downhill_right_smoke2": {
                    "path": "downhill_right_smoke2.png",
                    "width": 100,
                    "height": 56
                }
            }
        },
        {
            "name": "Candy",
            "age": 21,
            "top_speed": (SEGMENT_HEIGHT / (1.0/FPS)) * 2.14,
            "offroad_top_speed_factor": 1.8,
            "acceleration_factor": 5.2,
            "deceleration": 2.5,
            "centrifugal_force": 0.366,
            "city": "Surfers Paradise, QLD",
            "select_sfx": "candy_select.ogg",
            "sprites": {
                "mugshot_small": {
                    "path": "candy_small.png",
                    "width": 60,
                    "height": 60
                },
                "mugshot_large": {
                    "path": "candy_large.png",
                    "width": 320,
                    "height": 400
                },
                "straight1": {
                    "path": "straight1.png",
                    "width": 80,
                    "height": 50
                },
                "straight2": {
                    "path": "straight2.png",
                    "width": 80,
                    "height": 50
                },
                "left1": {
                    "path": "left1.png",
                    "width": 80,
                    "height": 50
                },
                "left2": {
                    "path": "left2.png",
                    "width": 80,
                    "height": 50
                },
                "right1": {
                    "path": "right1.png",
                    "width": 80,
                    "height": 50
                },
                "right2": {
                    "path": "right2.png",
                    "width": 80,
                    "height": 50
                },
                "left_smoke1": {
                    "path": "left_smoke1.png",
                    "width": 100,
                    "height": 56
                },
                "left_smoke2": {
                    "path": "left_smoke2.png",
                    "width": 100,
                    "height": 56
                },
                "right_smoke1": {
                    "path": "right_smoke1.png",
                    "width": 100,
                    "height": 56
                },
                "right_smoke2": {
                    "path": "right_smoke2.png",
                    "width": 100,
                    "height": 56
                },
                "uphill_straight1": {
                    "path": "uphill_straight1.png",
                    "width": 80,
                    "height": 56
                },
                "uphill_straight2": {
                    "path": "uphill_straight2.png",
                    "width": 80,
                    "height": 56
                },
                "uphill_left1": {
                    "path": "uphill_left1.png",
                    "width": 80,
                    "height": 56
                },
                "uphill_left2": {
                    "path": "uphill_left2.png",
                    "width": 80,
                    "height": 56
                },
                "uphill_right1": {
                    "path": "uphill_right1.png",
                    "width": 80,
                    "height": 56
                },
                "uphill_right2": {
                    "path": "uphill_right2.png",
                    "width": 80,
                    "height": 56
                },
                "uphill_left_smoke1": {
                    "path": "uphill_left_smoke1.png",
                    "width": 100,
                    "height": 56
                },
                "uphill_left_smoke2": {
                    "path": "uphill_left_smoke2.png",
                    "width": 100,
                    "height": 56
                },
                "uphill_right_smoke1": {
                    "path": "uphill_right_smoke1.png",
                    "width": 100,
                    "height": 56
                },
                "uphill_right_smoke2": {
                    "path": "uphill_right_smoke2.png",
                    "width": 100,
                    "height": 56
                },
                "downhill_straight1": {
                    "path": "downhill_straight1.png",
                    "width": 80,
                    "height": 56
                },
                "downhill_straight2": {
                    "path": "downhill_straight2.png",
                    "width": 80,
                    "height": 56
                },
                "downhill_left1": {
                    "path": "downhill_left1.png",
                    "width": 80,
                    "height": 56
                },
                "downhill_left2": {
                    "path": "downhill_left2.png",
                    "width": 80,
                    "height": 56
                },
                "downhill_right1": {
                    "path": "downhill_right1.png",
                    "width": 80,
                    "height": 56
                },
                "downhill_right2": {
                    "path": "downhill_right2.png",
                    "width": 80,
                    "height": 56
                },
                "downhill_left_smoke1": {
                    "path": "downhill_left_smoke1.png",
                    "width": 100,
                    "height": 56
                },
                "downhill_left_smoke2": {
                    "path": "downhill_left_smoke2.png",
                    "width": 100,
                    "height": 56
                },
                "downhill_right_smoke1": {
                    "path": "downhill_right_smoke1.png",
                    "width": 100,
                    "height": 56
                },
                "downhill_right_smoke2": {
                    "path": "downhill_right_smoke2.png",
                    "width": 100,
                    "height": 56
                }
            }
        },
        {
            "name": "Burl",
            "age": 37,
            "top_speed": (SEGMENT_HEIGHT / (1.0/FPS)) * 1.83,
            "offroad_top_speed_factor": 1.75,
            "acceleration_factor": 3.8,
            "deceleration": 2.2,
            "centrifugal_force": 0.188,
            "city": "Nullarbor Roadhouse, SA",
            "select_sfx": "burl_select.ogg",
            "sprites": {
                "mugshot_small": {
                    "path": "burl_small.png",
                    "width": 60,
                    "height": 60
                },
                "mugshot_large": {
                    "path": "burl_large.png",
                    "width": 320,
                    "height": 400
                },
                "straight1": {
                    "path": "straight1.png",
                    "width": 80,
                    "height": 50
                },
                "straight2": {
                    "path": "straight2.png",
                    "width": 80,
                    "height": 50
                },
                "left1": {
                    "path": "left1.png",
                    "width": 80,
                    "height": 50
                },
                "left2": {
                    "path": "left2.png",
                    "width": 80,
                    "height": 50
                },
                "right1": {
                    "path": "right1.png",
                    "width": 80,
                    "height": 50
                },
                "right2": {
                    "path": "right2.png",
                    "width": 80,
                    "height": 50
                },
                "left_smoke1": {
                    "path": "left_smoke1.png",
                    "width": 100,
                    "height": 56
                },
                "left_smoke2": {
                    "path": "left_smoke2.png",
                    "width": 100,
                    "height": 56
                },
                "right_smoke1": {
                    "path": "right_smoke1.png",
                    "width": 100,
                    "height": 56
                },
                "right_smoke2": {
                    "path": "right_smoke2.png",
                    "width": 100,
                    "height": 56
                },
                "uphill_straight1": {
                    "path": "uphill_straight1.png",
                    "width": 80,
                    "height": 56
                },
                "uphill_straight2": {
                    "path": "uphill_straight2.png",
                    "width": 80,
                    "height": 56
                },
                "uphill_left1": {
                    "path": "uphill_left1.png",
                    "width": 80,
                    "height": 56
                },
                "uphill_left2": {
                    "path": "uphill_left2.png",
                    "width": 80,
                    "height": 56
                },
                "uphill_right1": {
                    "path": "uphill_right1.png",
                    "width": 80,
                    "height": 56
                },
                "uphill_right2": {
                    "path": "uphill_right2.png",
                    "width": 80,
                    "height": 56
                },
                "uphill_left_smoke1": {
                    "path": "uphill_left_smoke1.png",
                    "width": 100,
                    "height": 56
                },
                "uphill_left_smoke2": {
                    "path": "uphill_left_smoke2.png",
                    "width": 100,
                    "height": 56
                },
                "uphill_right_smoke1": {
                    "path": "uphill_right_smoke1.png",
                    "width": 100,
                    "height": 56
                },
                "uphill_right_smoke2": {
                    "path": "uphill_right_smoke2.png",
                    "width": 100,
                    "height": 56
                },
                "downhill_straight1": {
                    "path": "downhill_straight1.png",
                    "width": 80,
                    "height": 56
                },
                "downhill_straight2": {
                    "path": "downhill_straight2.png",
                    "width": 80,
                    "height": 56
                },
                "downhill_left1": {
                    "path": "downhill_left1.png",
                    "width": 80,
                    "height": 56
                },
                "downhill_left2": {
                    "path": "downhill_left2.png",
                    "width": 80,
                    "height": 56
                },
                "downhill_right1": {
                    "path": "downhill_right1.png",
                    "width": 80,
                    "height": 56
                },
                "downhill_right2": {
                    "path": "downhill_right2.png",
                    "width": 80,
                    "height": 56
                },
                "downhill_left_smoke1": {
                    "path": "downhill_left_smoke1.png",
                    "width": 100,
                    "height": 56
                },
                "downhill_left_smoke2": {
                    "path": "downhill_left_smoke2.png",
                    "width": 100,
                    "height": 56
                },
                "downhill_right_smoke1": {
                    "path": "downhill_right_smoke1.png",
                    "width": 100,
                    "height": 56
                },
                "downhill_right_smoke2": {
                    "path": "downhill_right_smoke2.png",
                    "width": 100,
                    "height": 56
                }
            }
        }
    ]
    SPRITES = {
        "column": {
            "path": "column.png",
            "collision": [0.05, 0.05],
            "width": 90,
            "height": 126
        },
        "tunnel_entrance": {
            "width": 80,
            "height": 10,
            "path": None,
            "collision": [0, 0]
        },
        "tunnel_light": {
            "path": "tunnel_light.png",
            "width": 8,
            "height": 8
        },
        "tunnel_sign": {
            "path": "bush1.png",
            "width": 20,
            "height": 20
        },
        "over_column": {
            "path": "over_column.png",
            "width": 480,
            "height": 40
        },
        "boat_house": {
            "path": "boat_house.png",
            "collision": [0.05, 0.01],
            "width": 119,
            "height": 86
        },
        "bush1": {
            "path": "bush3.png",
            "collision": [0.4, 0.4],
            "width": 64,
            "height": 32
        },
        "bush2": {
            "path": "bush2.png",
            "collision": [0.4, 0.4],
            "width": 64,
            "height": 32
        },
        "palm_tree": {
            "path": "palm-tree2.png",
            "collision": [0.6, 0.1],
            "width": 64,
            "height": 128
        },
        "tree1": {
            "path": "tree2.png",
            "collision": [0.64, 0.1],
            "width": 144,
            "height": 144
        },
        "billboard3": {
            "path": "billboard03.png",
            "collision": [0.2, 0.2],
            "width": 92,
            "height": 88
        },
        "billboard4": {
            "path": "billboard04.png",
            "collision": [0.05, 0.05],
            "width": 107,
            "height": 68
        },
        "start": {
            "path": "toll_point.png",
            "width": 240,
            "height": 120
        },
        "boulder1": {
            "path": "boulder2.png",
            "collision": [0, 0],
            "width": 64,
            "height": 64
        },
        "post": {
            "path": "post.png",
            "collision": [0.25, 0.25],
            "width": 30,
            "height": 56
        },
        "light_post1": {
            "path": "light_post1.png",
            "width": 40,
            "height": 90
        },
        "light_post2": {
            "path": "light_post2.png",
            "width": 40,
            "height": 90
        },
        "left_sign": {
            "path": "left_sign.png",
            "width": 40,
            "height": 90
        },
        "right_sign": {
            "path": "right_sign.png",
            "width": 40,
            "height": 90
        },
        "traffic_light": {
            "path": "traffic_light.png",
            "width": 40,
            "height": 90
        },
        "competitor1": {
            "path": "competitor1.png",
            "collision": [0.05, 0.05],
            "width": 80,
            "height": 50
        },
        "competitor2": {
            "path": "competitor2.png",
            "collision": [0.05, 0.05],
            "width": 80,
            "height": 50
        },
        "competitor3": {
            "path": "competitor3.png",
            "collision": [0.05, 0.05],
            "width": 80,
            "height": 50
        },
        "bonus": {
            "path": "bonus.png",
            "collision": [0, 0],
            "bonus": True,
            "width": 25,
            "height": 25
        },
        "speed_boost": {
            "path": None,
            "collision": [0, 0],
            "speed_boost": True,
            "width": 72,
            "height": 42
        },
        "hooker1": {
            "path": "hooker1.png",
            "collision": [0.42, 0.36],
            "hooker": True,
            "width": 25,
            "height": 42
        },
        "hooker2": {
            "path": "hooker2.png",
            "collision": [0.42, 0.36],
            "hooker": True,
            "width": 25,
            "height": 42
        },
        "hooker3": {
            "path": "hooker3.png",
            "collision": [0.42, 0.36],
            "hooker": True,
            "width": 25,
            "height": 42
        },
        "barrier": {
            "path": "barrier.png",
            "collision": [0.05, 0.05],
            "width": 60,
            "height": 35
        }
    }

class Background:
    def __init__(self, name , parallax_speed, scale_height=False, convert=False):
        self.image          = pygame.image.load(os.path.join("assets/img","{0}.png".format(name)))
        self.parallax_speed = parallax_speed
        self.y              = 0
        self.width          = self.image.get_width()
        self.height         = self.image.get_height()
        self.curvature      = (self.width - GameSetting.DIMENSIONS[0]) / 2
        self.scale_height   = scale_height
        self.visible_height = 0

        if convert:
            self.image = self.image.convert()
    
    def step(self, curve, speed_percent):
        c = self.curvature

        # Background is now completely off screen, so reset it.
        if c <= -self.width:
            self.curvature = c + self.width
        elif c >= self.width:
            self.curvature = (c - self.width) + (self.width - GameSetting.DIMENSIONS[0])

        self.curvature += (curve / self.parallax_speed) * speed_percent
    
    def render(self, window):
        c = self.curvature
        w = GameSetting.DIMENSIONS[0]
        img = self.image

        # Stretch BG to fill visible area if scaling is turned on.
        if self.scale_height and self.height < self.visible_height:
            img = pygame.transform.scale(self.image, (self.width, int(self.visible_height)))

        window.blit(img,(0, self.y),(c, 0, w, GameSetting.DIMENSIONS[1]))

        # Fill empty space on the left of the screen.
        if c < 0:
            window.blit(img,(0, self.y),(self.width + c, 0, -c, GameSetting.DIMENSIONS[1]))

        # Fill empty space on the right of the screen.
        elif c > (self.width - w):
            window.blit(img,(self.width - c, self.y),(0, 0, (c - (self.width - w)), GameSetting.DIMENSIONS[1]))

class Util:
    @staticmethod
    def try_quit(e):
        if e.type == QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE and GameSetting.FULL_SCREEN):
            pygame.quit()
            sys.exit()
    
    @staticmethod
    def limit(v, low, high):
        if v < low:
            return low
        elif v > high:
            return high
        else:
            return v
    
    @staticmethod
    def render_text(text, window, font, color, position):
        text = font.render(text, 1, color)
        window.blit(text, position)
        return text
    
    @staticmethod
    def middle(surface, x_offset=0, y_offset=0, x=-1, y=-1):
        mx = x if x > -1 else ((GameSetting.DIMENSIONS[0] - surface.get_width()) / 2) + x_offset
        my = y if y > -1 else ((GameSetting.DIMENSIONS[1] - surface.get_height()) / 2) + y_offset

        return (mx, my)

class WorldObject:
    def __init__(self, quant=3):
        self.rendered_area = 0
        self.quantifier    = quant
    
    def non_renderable(self):
        return self.sprite["path"] == None
    
    def screen_dim(self, dimension, screen_pos):
        return int(self.sprite[dimension] * screen_pos * GameSetting.ROAD_WIDTH * self.quantifier)

    def render(self, window, segment):
        coords     = segment.bottom["screen"]
        s_width    = self.screen_dim("width", coords["s"])
        s_height   = self.screen_dim("height", coords["s"])
        x          = (coords["x"] - s_width) + (coords["w"] * self.offset)
        y          = GameSetting.DIMENSIONS[1] - coords["y"] - s_height
        top_clip   = GameSetting.DIMENSIONS[1] - segment.clip[1] - y
        left_clip  = 0 if not segment.in_tunnel else max(x, 0) - segment.clip[0]
        right_clip = 0 if not segment.in_tunnel else segment.clip[2]

        if right_clip > 0 and right_clip < (x + s_width):
            s_width -= int((x + s_width) - right_clip)

        if self.offset_y > 0:
            y -= (self.offset_y * 100000 * coords["s"])

        self.rendered_area = [x, x + s_width]

        if s_width > 0 and s_height > 0 and top_clip > 0 and s_width < GameSetting.DIMENSIONS[0] * 2 and s_height < GameSetting.DIMENSIONS[1] * 2 and (left_clip >= 0 or abs(left_clip) < s_width):
            if not self.non_renderable():
                offset_x = 0 if left_clip >= 0 else abs(left_clip)
                img      = self.path()
                img      = pygame.transform.scale(img, (s_width, s_height))
                window.blit(img, (x, y), (offset_x, 0, s_width, top_clip))

class Competitor(WorldObject):
    def __init__(self, position, offset, name, speed):
        self.position   = position * GameSetting.SEGMENT_HEIGHT
        self.offset     = offset
        self.offset_y   = 0.0
        self.sprite     = GameSetting.SPRITES[name]
        self.speed      = speed
        self.engine_sfx = pygame.mixer.Sound(os.path.join("assets/audio", "engine.ogg"))
        self.engine_sfx.set_volume(0)
        WorldObject.__init__(self, 1.8)
    
    def travel(self, track_length):
        # Update Z position.
        pos = self.position + (GameSetting.FRAME_RATE * self.speed)

        if pos >= track_length:
            pos -= track_length

        if pos < 0:
            pos += track_length

        self.position = pos

    def play_engine(self, player_position):
        v = self.__engine_volume(player_position)

        if v > 0:
            if self.engine_sfx.get_volume() == 0:
                self.engine_sfx.play()
        else:
            self.engine_sfx.stop()

        self.engine_sfx.set_volume(v)

    def path(self):
        return pygame.image.load(os.path.join("assets/img", self.sprite["path"]))

    def __engine_volume(self, player_position):
        distance = abs(self.position - player_position)

        if distance > GameSetting.MINIMUM_ENGINE_DIST:
            return 0
        else:
            volume = round(float(distance) / GameSetting.MINIMUM_ENGINE_DIST, 1)
            return round(volume - ((volume - 0.5) * 2), 1)

class CountDown:
    def __init__(self, level_number, level_name):
        self.level_number = level_number
        self.level_name   = level_name
        self.remaining    = 3
        self.remaining    = 3
        self.finished     = False
        self.text_font    = pygame.font.Font(GameSetting.FONTS["retro_computer"], 20)
        self.cd_font      = pygame.font.Font(GameSetting.FONTS["retro_computer"], 250)
        
    def progress(self, window):
        txt        = str(self.remaining) if self.remaining > 0 else "GO"
        cd_text    = self.cd_font.render(txt, 1, GameSetting.COLOURS["text"])
        level_text = self.text_font.render("Level %d: %s" % (self.level_number, self.level_name), 1, GameSetting.COLOURS["text"])
        freq       = 440 if self.remaining > 0 else 570
        beep       = pygame.mixer.Sound(os.path.join("assets/audio", "%d.wav" % freq))

        window.fill(GameSetting.COLOURS["black"])
        window.blit(level_text, Util.middle(level_text, y=25))
        window.blit(cd_text, Util.middle(cd_text, y_offset=(level_text.get_height())))

        beep.set_volume(0.6)
        beep.play()

        self.remaining -= 1

        if self.remaining < 0:
            self.finished = True

class Credit:
    def __init__(self):
        self.finished = False

    def progress(self, window):
        self.finished = True

class HighScore:
    def __init__(self):
        self.high_scores = self.__read_high_scores()
        self.__sort()

    def is_high_score(self, score):
        scores = self.__scores_only()
        return any(map(lambda n: score > n, scores))

    def minimum_score(self):
        scores = self.__scores_only()
        return scores[-1] if scores else 0

    def add_high_score(self, score):
        today = dt.date.today()
        self.high_scores.append([today, score])
        self.__sort()
        self.__write_high_scores()

    def __sort(self):
        self.high_scores.sort(key=lambda hs: hs[1], reverse=True)

    def __write_high_scores(self):
        hs_file_path = os.path.join("data", "highscores.json")
        with open(hs_file_path, "w") as hs:
            jdata = list(map(lambda hs: [hs[0].strftime("%Y-%m-%d"), hs[1]], self.high_scores))
            json.dump(jdata, hs)

    def __read_high_scores(self):
        hs_file_path = os.path.join("data", "highscores.json")
        if os.path.exists(hs_file_path):
            with open(hs_file_path, "r") as hs:
                try:
                    jhs = json.load(hs)
                    return list(map(lambda hs: [dt.datetime.strptime(hs[0], "%Y-%m-%d").date(), hs[1]], jhs))
                except (json.decoder.JSONDecodeError, ValueError):
                    # Handle the case where the file doesn't contain valid JSON data or is empty
                    return []
        else:
            # Handle the case where the file doesn't exist
            return []

    def __scores_only(self):
        return list(map(lambda hs: hs[1], self.high_scores))

class PlayerStatus(Enum):
    alive = 0
    game_over = 1
    level_over = 1

class Player:
    def __init__(self, high_score, selected_player):
        self.settings       = GameSetting.PLAYERS[selected_player]
        self.points         = 0
        self.high_score     = high_score
        self.next_milestone = GameSetting.POINT_MILESTONE
        self.reset()

    def reset(self, total_laps=GameSetting.LAPS_PER_LEVEL):
        self.status          = PlayerStatus.alive
        self.level_over_lag  = GameSetting.LEVEL_OVER_LAG
        self.x               = 0
        self.y               = 0
        self.position        = 0
        self.lap_percent     = 0
        self.direction       = 0
        self.acceleration    = 0
        self.speed           = 1
        self.speed_boost     = 1
        self.animation_frame = 1
        self.new_lap         = False
        self.lap_bonus       = 0
        self.time_bonus      = 0
        self.lap             = 1
        self.total_laps      = total_laps
        self.lap_time        = 0
        self.lap_margin      = 0
        self.blood_alpha     = 0
        self.in_tunnel       = False
        self.fastest_lap     = GameSetting.CHECKPOINT
        self.checkpoint      = GameSetting.CHECKPOINT
        self.time_left       = GameSetting.CHECKPOINT
        self.last_checkpoint = None
        self.crashed         = False
        self.special_text    = None
        self.screech_sfx     = None
        self.__set_checkpoint()

    def steer(self, segment):
        bounds = GameSetting.TUNNEL_BOUNDS if self.in_tunnel else GameSetting.BOUNDS
        self.x = Util.limit(self.x + self.direction, -bounds, bounds)
        # Apply centrifugal force if we are going around a corner.
        if segment.curve != 0 and self.status == PlayerStatus.alive:
            # Congratulate player if they've broken personal record.
            self.x -= (self.direction_speed() * self.speed_percent() * segment.curve * self.settings["centrifugal_force"])

    def climb(self, segment):
        top_y    = segment.top["world"]["y"]
        bottom_y = segment.bottom["world"]["y"]
        self.y = top_y + (top_y - bottom_y) * self.speed_percent()

    def detect_collisions(self, segment):
        if not self.crashed:
            for sp in segment.sprites:
                if "collision" in sp.sprite and self.__collided_with_sprite(sp):
                    if sp.is_hooker():
                        if not sp.hit:
                            sp.hit = True
                            self.__hit_hooker()
                    elif sp.is_bonus():
                        segment.remove_sprite(sp)
                        self.__hit_bonus()
                    elif sp.is_speed_boost():
                        self.__hit_speed_boost()
                    else:
                        self.__hit_world_object()
                    break
            for comp in segment.competitors:
                if self.__collided_with_sprite(comp):
                    self.__hit_competitor()
                    break

    def render(self, window, segment):
        top    = segment.top
        bottom = segment.bottom
        width  = GameSetting.DIMENSIONS[0] / 2
        height = GameSetting.DIMENSIONS[1] / 2
        scale  = GameSetting.CAMERA_DEPTH / (GameSetting.CAMERA_HEIGHT * GameSetting.CAMERA_DEPTH)
        sprite = "straight"
        if self.direction > 0:
            sprite = "right"
        elif self.direction < 0:
            sprite = "left"
        if top["world"]["y"] > bottom["world"]["y"]:
            sprite = "uphill_" + sprite
        elif top["world"]["y"] < (bottom["world"]["y"] - 10):  # TODO: Fix this. Should not need -10 here.
            sprite = "downhill_" + sprite
        if self.speed > 0:
            self.animation_frame += 1
            if self.animation_frame > (GameSetting.PLAYER_ANIM_HOLD * 2):
                self.animation_frame = 1
        # Show smoke if player is fangin' it around a corner.
        if abs(segment.curve) > GameSetting.MINIMUM_CORNER_SMOKE and self.direction != 0 and self.speed > (self.settings["top_speed"] / 1.2):
            sprite += "_smoke"
            self.__run_screech()
        elif self.screech_sfx:
            self.__stop_screech()
        sprite += "1" if (self.animation_frame < GameSetting.PLAYER_ANIM_HOLD) else "2"
        sprite   = self.settings["sprites"][sprite]
        s_width  = int(sprite["width"] * scale * GameSetting.ROAD_WIDTH * 1.2)
        s_height = int(sprite["height"] * scale * GameSetting.ROAD_WIDTH * 1.2)
        p = pygame.image.load(os.path.join("assets/img", sprite["path"]))
        p = pygame.transform.scale(p, (s_width, s_height))
        self.rendered_area = [width - (s_width / 2), width + (s_width / 2)]
        window.blit(p, (width - (s_width / 2), GameSetting.DIMENSIONS[1] - s_height - GameSetting.BOTTOM_OFFSET))
        # Finish up the round.
        if self.status != PlayerStatus.alive:
            self.level_over_lag -= 1

    def render_hud(self, window):
        center      = (75, GameSetting.DIMENSIONS[1] - 80)
        speedo_rect = (35, GameSetting.DIMENSIONS[1] - 120, 80, 80)
        orbit_pos   = (self.speed / (self.settings["top_speed"] / 4.7)) + 2.35
        start       = self.__circular_orbit(center, -10, orbit_pos)
        finish      = self.__circular_orbit(center, 36, orbit_pos)
        speed       = round((self.speed / GameSetting.SEGMENT_HEIGHT) * 1.5, 1)
        font        = pygame.font.Font(GameSetting.FONTS["retro_computer"], 16)
        st          = self.special_text
        time_colour = GameSetting.COLOURS["text"] if self.time_left > 5 else GameSetting.COLOURS["red"]
        # Speedometer.
        pygame.draw.circle(window, GameSetting.COLOURS["black"], center, 50, 2)
        pygame.draw.circle(window, GameSetting.COLOURS["black"], center, 4)
        pygame.draw.line(window, GameSetting.COLOURS["black"], start, finish, 3)
        pygame.draw.arc(window, GameSetting.COLOURS["black"], speedo_rect, 0.2, math.pi * 1.25, 5)
        pygame.draw.arc(window, GameSetting.COLOURS["red"], speedo_rect, -0.73, 0.2, 5)
        Util.render_text("kmph", window, font, GameSetting.COLOURS["text"], (110, GameSetting.DIMENSIONS[1] - 24))
        Util.render_text(str(speed), window, font, GameSetting.COLOURS["text"], (10, GameSetting.DIMENSIONS[1] - 24))
        Util.render_text("Lap", window, font, GameSetting.COLOURS["text"], (GameSetting.DIMENSIONS[0] - 130, 10))
        Util.render_text("%s/%s" % (self.lap, self.total_laps) , window, font, GameSetting.COLOURS["text"], (GameSetting.DIMENSIONS[0] - 58, 10))
        Util.render_text("Time", window, font, time_colour, (10, 10))
        Util.render_text(str(math.trunc(self.time_left)), window, font, time_colour, (90, 10))
        # Render special text.
        if st:
            td = (dt.datetime.now() - st[0])
            if td.seconds > st[1]:
                self.special_text = None
            else:
                bonus_colour = "bonus_a" if (td.microseconds / 25000.0) % 10 > 5 else "bonus_b"
                Util.render_text(st[2], window, font, GameSetting.COLOURS[bonus_colour], (10, 36))
        # Points rendering needs more care because it grows so fast.
        p_val_text  = font.render(str(math.trunc(self.points)), 1, GameSetting.COLOURS["text"])
        p_name_text = font.render("Points", 1, GameSetting.COLOURS["text"])
        p_val_x     = GameSetting.DIMENSIONS[0] - p_val_text.get_width() - 10
        window.blit(p_val_text, (p_val_x, GameSetting.DIMENSIONS[1] - 24))
        window.blit(p_name_text, (p_val_x - 112, GameSetting.DIMENSIONS[1] - 24))
        # Hit a point milestone.
        if self.points > self.next_milestone and self.status == PlayerStatus.alive:
            milestone_sfx = pygame.mixer.Sound(os.path.join("assets/audio", "excellent.ogg"))
            milestone_sfx.play()
            self.next_milestone += GameSetting.POINT_MILESTONE
            self.__set_special_text("Nice driving!", 2)
        # On the leaderboard!
        if self.high_score > 0 and self.points > self.high_score:
            high_score_sfx = pygame.mixer.Sound(os.path.join("assets/audio", "excellent.ogg"))
            high_score_sfx.play()
            self.high_score = 0
            self.__set_special_text("New High Score!", 2)
        if self.status == PlayerStatus.game_over:
            self.__game_over_overlay(window)
        elif self.status == PlayerStatus.level_over:
            self.__level_over_overlay(window)
        # Display lap difference (unless we've only done one lap).
        if self.lap_margin != 0 and self.lap > 2 and self.lap_percent < 20:
            diff = self.lap_margin
            if diff <= 0:
                colour = "red"
                sign   = "+"
            else:
                colour = "green"
                sign   = "-"
            Util.render_text(sign + str(round(abs(diff), 1)), window, font, GameSetting.COLOURS[colour], (10, 40))

    def render_blood(self, window):
        b = pygame.image.load(os.path.join("assets/img", "blood.png"))
        b.set_alpha(self.blood_alpha)
        x = (GameSetting.DIMENSIONS[0] - b.get_size()[0]) / 2
        y = ((GameSetting.DIMENSIONS[1] - b.get_size()[1]) / 2) - 30
        window.blit(b, (x, y))
        self.blood_alpha -= 1

    def accelerate(self):
        curr_speed = self.speed_boost * (self.speed + ((self.settings["top_speed"] / self.settings["acceleration_factor"]) * self.acceleration))
        self.speed = Util.limit(curr_speed, 0, self.speed_boost * self.settings["top_speed"])

    def travel(self, track_length, window):
        pos        = self.position + (GameSetting.FRAME_RATE * self.speed)
        td         = (dt.datetime.now() - self.last_checkpoint)
        total_secs = (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6 # td.total_seconds() not implemented in Python 2.6
        self.new_lap = False
        if self.speed_boost > 1:
            self.speed_boost -= GameSetting.SPEED_BOOST_DECREASE
        if self.status == PlayerStatus.alive:
            self.points   += (self.speed / GameSetting.SEGMENT_HEIGHT) / GameSetting.POINTS
            self.time_left = round(self.checkpoint - total_secs, 1) + self.lap_bonus
            if self.time_left <= 0:
                go_sfx = pygame.mixer.Sound(os.path.join("assets/audio", "loser.ogg"))
                go_sfx.play()
                self.status = PlayerStatus.game_over
            elif self.time_left == 5:
                self.__set_special_text("Hurry up!", 2)
        # New lap.
        if pos >= track_length:
            self.__set_checkpoint()
            self.lap_bonus  = 0
            self.new_lap    = True
            self.lap_time   = total_secs
            self.lap_margin = self.fastest_lap - self.lap_time
            # Finished level.
            if self.status == PlayerStatus.alive and self.lap == self.total_laps:
                self.status = PlayerStatus.level_over
            else:
                self.lap += 1
                lap_sfx = pygame.mixer.Sound(os.path.join("assets/audio", "570.wav"))
                lap_sfx.play()
            if self.status != PlayerStatus.game_over:
                # Reduce checkpoint time every lap to increase difficulty.
                checkpoint_diff = (self.checkpoint - self.lap_time) / GameSetting.LAP_DIFFICULTY_FACTOR
                bonus_points    = self.time_left * GameSetting.POINTS * self.lap
                self.checkpoint -= max(checkpoint_diff, GameSetting.MINIMUM_DIFFICULTY)
                self.time_bonus += bonus_points
                self.points     += bonus_points
                if self.__fastest_lap():
                    # Congratulate player if they've broken personal record.
                    if self.lap > 2:
                        self.points += self.lap_margin * GameSetting.POINTS * self.lap
                        fast_lap_sfx = pygame.mixer.Sound(os.path.join("assets/audio", "jim.ogg"))
                        fast_lap_sfx.play()
                    self.fastest_lap = self.lap_time
            pos -= track_length
        if pos < 0:
            pos += track_length
        self.position    = pos
        self.lap_percent = round((pos / track_length) * 100)

    def set_acceleration(self, keys):
        a = -GameSetting.FRAME_RATE
        # Slow player down if they are on the grass or crashed.
        if self.crashed:
            a = 0
        else:
            if (self.x > 1.0 or self.x < -1.0) and self.speed > (self.settings["top_speed"] / self.settings["offroad_top_speed_factor"]):
                a = a * 3
            else:
                if keys[K_UP] or keys[K_x] or GameSetting.AUTO_DRIVE or self.status != PlayerStatus.alive:
                    a = GameSetting.FRAME_RATE
                elif keys[K_DOWN]:
                    a = -(GameSetting.FRAME_RATE * self.settings["deceleration"])
        self.acceleration = a

    def set_direction(self, keys):
        d = 0
        if self.status == PlayerStatus.alive:
            if keys[K_LEFT]:
                d = -self.direction_speed()
            elif keys[K_RIGHT]:
                d = self.direction_speed()
        self.direction = d

    def speed_percent(self):
        return self.speed / self.settings["top_speed"]

    def direction_speed(self):
        return (GameSetting.FRAME_RATE * 3 * self.speed_percent())

    def segment_percent(self):
        return ((self.position + GameSetting.PLAYER_Z) % GameSetting.SEGMENT_HEIGHT) / GameSetting.SEGMENT_HEIGHT

    def handle_crash(self):
        if self.crashed:
            step = -0.025 if self.x > 0 else 0.025
            if round(self.x, 1) != 0:
                self.x += step
            else:
                pygame.mixer.music.set_volume(GameSetting.MUSIC_VOLUME)
                self.crashed = False

    def finished(self):
        return self.level_over_lag == 0

    def alive(self):
        return self.status == PlayerStatus.game_over

    def __set_special_text(self, text, time):
        st = self.special_text
        if not st or st[2] != text:
            self.special_text = [dt.datetime.now(), time, text]

    def __collided_with_sprite(self, sprite):
        r_area = list(sprite.rendered_area)
        p_area = sprite.sprite["collision"]
        width  = r_area[1] - r_area[0]
        # Apply offsets.
        r_area[0] += (width * p_area[0])
        r_area[1] -= (width * p_area[1])
        return (self.rendered_area[0] < r_area[1] and self.rendered_area[1] > r_area[0])

    def __circular_orbit(self, center, radius, t):
        theta = math.fmod(t, math.pi * 2)
        c     = math.cos(theta)
        s     = math.sin(theta)
        return center[0] + radius * c, center[1] + radius * s

    def __set_checkpoint(self):
        self.last_checkpoint = dt.datetime.now()

    def __hit_hooker(self):
        crash_sfx        = pygame.mixer.Sound(os.path.join("assets/audio", "scream.ogg"))
        splat_sfx        = pygame.mixer.Sound(os.path.join("assets/audio", "blood.ogg"))
        self.blood_alpha = 255
        # Yeah, I'm a sicko....
        if self.status == PlayerStatus.alive:
            self.points += GameSetting.POINT_GAIN_PROSTITUTE
            self.__set_special_text("+%d points!" % GameSetting.POINT_GAIN_PROSTITUTE, 2)
        crash_sfx.play()
        splat_sfx.play()

    def __hit_bonus(self):
        if self.status == PlayerStatus.alive:
            self.lap_bonus += GameSetting.BONUS_AMOUNT
        bonus_sfx = pygame.mixer.Sound(os.path.join("assets/audio", "oh_yeah.ogg"))
        bonus_sfx.play()
        self.__set_special_text("Bonus time!", 2)

    def __hit_speed_boost(self):
        if self.speed_boost == 1:
            boost_sfx = pygame.mixer.Sound(os.path.join("assets/audio", "speed_boost.ogg"))
            boost_sfx.play()
            self.__set_special_text("Speed boost!", 2)
        self.speed_boost = 1.6

    def __hit_world_object(self):
        pygame.mixer.music.set_volume(0.2)
        crash_sfx        = pygame.mixer.Sound(os.path.join("assets/audio", "you_fool.ogg"))
        self.crashed     = True
        self.speed       = 0
        self.speed_boost = 1
        crash_sfx.play()
        if self.status == PlayerStatus.alive:
            deduction    = self.points * GameSetting.POINT_LOSS_SPRITE
            self.points -= deduction
            self.__set_special_text("-%d points!" % deduction, 2)

    def __hit_competitor(self):
        crash_sfx = pygame.mixer.Sound(os.path.join("assets/audio", "car_crash.ogg"))
        crash_sfx.play()
        self.speed = self.speed / GameSetting.CRASH_DIVISOR
        if self.status == PlayerStatus.alive:
            self.points -= self.points * GameSetting.POINT_LOSS_COMP

    def __fastest_lap(self):
        return self.status != PlayerStatus.game_over and self.lap_time < self.fastest_lap

    def __run_screech(self):
        if not self.screech_sfx:
            self.screech_sfx = pygame.mixer.Sound(os.path.join("assets/audio", "screech_short.ogg"))
            self.screech_sfx.set_volume(0.4)
            self.screech_sfx.play(-1)

    def __stop_screech(self):
        self.screech_sfx.stop()
        self.screech_sfx = None

    def __game_over_overlay(self, window):
        go_font = pygame.font.Font(GameSetting.FONTS["retro_computer"], 35)
        txt_go  = go_font.render("Level Completed!", 1, GameSetting.COLOURS["red"])
        x       = (GameSetting.DIMENSIONS[0] - txt_go.get_size()[0]) / 2
        y       = (GameSetting.DIMENSIONS[1] - txt_go.get_size()[1]) / 2
        overlay = pygame.Surface(GameSetting.DIMENSIONS, pygame.SRCALPHA)
        overlay.fill((255, 255, 255, 90))
        overlay.blit(txt_go, (x, y))
        window.blit(overlay, (0,0))

    def __level_over_overlay(self, window):
        lo_font      = pygame.font.Font(GameSetting.FONTS["fipps"], 38)
        s_font       = pygame.font.Font(GameSetting.FONTS["retro_computer"], 30)
        txt_lo       = lo_font.render("Level Complete!", 1, GameSetting.COLOURS["dark_text"])
        txt_lap      = s_font.render("Best Lap", 1, GameSetting.COLOURS["dark_text"])
        txt_lap_v    = s_font.render("%.1fs" % round(self.fastest_lap, 1), 1, GameSetting.COLOURS["dark_text"])
        txt_bonus    = s_font.render("Time bonus", 1, GameSetting.COLOURS["dark_text"])
        txt_bonus_v  = s_font.render(str(math.trunc(self.time_bonus)), 1, GameSetting.COLOURS["dark_text"])
        txt_points   = s_font.render("Points", 1, GameSetting.COLOURS["dark_text"])
        txt_points_v = s_font.render(str(math.trunc(self.points)), 1, GameSetting.COLOURS["dark_text"])
        overlay      = pygame.Surface(GameSetting.DIMENSIONS, pygame.SRCALPHA)
        overlay.fill((255, 255, 255, 150))
        overlay.blit(txt_lo, (GameSetting.DIMENSIONS[0] / 2 - txt_lo.get_size()[0] / 2, 20))
        overlay.blit(txt_lap, (20, 180))
        overlay.blit(txt_lap_v, (GameSetting.DIMENSIONS[0] - txt_lap_v.get_size()[0] - 10, 190))
        overlay.blit(txt_bonus, (20, 260))
        overlay.blit(txt_bonus_v, (GameSetting.DIMENSIONS[0] - txt_bonus_v.get_size()[0] - 10, 270))
        overlay.blit(txt_points, (20, 340))
        overlay.blit(txt_points_v, (GameSetting.DIMENSIONS[0] - txt_points_v.get_size()[0] - 10, 350))
        window.blit(overlay, (0,0))

class PlayerSelect:
    def __init__(self):
        self.selected         = 0
        self.finished         = False
        self.player_chosen    = False
        self.selection_colour = 0
        self.background       = pygame.image.load(os.path.join("assets/img", "player_select.png"))
        self.fonts            = {
            "title": pygame.font.Font(GameSetting.FONTS["fipps"], 38),
            "name": pygame.font.Font(GameSetting.FONTS["retro_computer"], 18),
            "details": pygame.font.Font(GameSetting.FONTS["retro_computer"], 12),
            "stats": pygame.font.Font(GameSetting.FONTS["retro_computer"], 8)
        }
        
    def progress(self, window):
        txt_title     = self.fonts["title"].render("Player Select", 1, GameSetting.COLOURS["text"])
        player        = GameSetting.PLAYERS[self.selected]
        lpad          = 40
        start_point   = (GameSetting.DIMENSIONS[0] / 2) + (lpad / 2)
        step          = player["sprites"]["mugshot_small"]["width"]
        large_mugshot = pygame.image.load(os.path.join("assets/img", player["sprites"]["mugshot_large"]["path"]))
        self.selection_colour = 1 if self.selection_colour == 0 else 0
        window.blit(self.background, (0, 0))
        window.blit(txt_title, ((GameSetting.DIMENSIONS[0] / 2) - (txt_title.get_size()[0] / 2), 10))
        for i, p in enumerate(GameSetting.PLAYERS):
            details = p["sprites"]["mugshot_small"]
            mugshot = pygame.image.load(os.path.join("assets/img", details["path"]))
            x       = start_point + (i * (step + lpad))
            y       = 120
            window.blit(mugshot, (x, y))
            if i == self.selected:
                bw = 10
                pygame.draw.rect(window,GameSetting.COLOURS["selection"][self.selection_colour],[x - (bw / 2), y - (bw / 2), details["width"] + bw, details["width"] + bw], bw)
        # Player name and picture.
        window.blit(large_mugshot, (0, GameSetting.DIMENSIONS[1] - player["sprites"]["mugshot_large"]["height"]))
        window.blit(self.fonts["name"].render(player["name"], 1, GameSetting.COLOURS["text"]), (start_point - bw, 200))
        window.blit(self.fonts["details"].render(player["city"], 1, GameSetting.COLOURS["text"]), (start_point - bw, 228))
        # Player stats.
        desired_acceleration = int(self.normalise(player["acceleration_factor"], *GameSetting.HARD_ACCELERATION) * 155)
        desired_handling = int((1.0 - self.normalise(player["centrifugal_force"], *GameSetting.HARD_HANDLING)) * 155)
        desired_top_speed = int(self.normalise(player["top_speed"], *GameSetting.HARD_TOP_SPEED) * 155)
        window.blit(self.fonts["stats"].render("Acceleration", 1, GameSetting.COLOURS["text"]), (start_point - bw, 290))
        window.blit(self.fonts["stats"].render("Handling", 1, GameSetting.COLOURS["text"]), (start_point - bw, 314))
        window.blit(self.fonts["stats"].render("Speed", 1, GameSetting.COLOURS["text"]), (start_point - bw, 338))
        su = pygame.Surface((155, 18), pygame.SRCALPHA)
        su.fill(GameSetting.COLOURS["opaque_white"])
        window.blit(su, (start_point + 105, 285))
        window.blit(su, (start_point + 105, 309))
        window.blit(su, (start_point + 105, 333))
        pygame.draw.rect(window,GameSetting.COLOURS["text"],[start_point + 105, 285, desired_acceleration, 18])
        pygame.draw.rect(window,GameSetting.COLOURS["text"],[start_point + 105, 309, desired_handling, 18])
        pygame.draw.rect(window,GameSetting.COLOURS["text"],[start_point + 105, 333, desired_top_speed, 18])
        if self.player_chosen:
            self.finalise_selection(player)
        for e in pygame.event.get():
            Util.try_quit(e)
            if e.type == pygame.KEYDOWN and not self.player_chosen:
                if e.key == pygame.K_LEFT and self.selected > 0:
                    self.selected -= 1
                elif e.key == pygame.K_RIGHT and self.selected < len(GameSetting.PLAYERS) - 1:
                    self.selected += 1
                elif e.key == pygame.K_RETURN:
                    self.player_chosen = True

    def finalise_selection(self, player):
        pygame.mixer.music.load(os.path.join("assets/audio", player["select_sfx"]))
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        self.finished = True

    def normalise(self, v, low, high):
        return (v - low) / (high - low)

class Segment:
    def __init__(self, palette, index, curve, start_y, end_y):
        self.index         = index
        self.curve         = curve
        self.sprites       = []
        self.competitors   = []
        self.pre_polygons  = []
        self.post_polygons = []
        self.clip          = [0, 0, 0]
        self.in_tunnel     = False
        self.tunnel_end    = False
        self.speed_boost   = False
        self.palette       = palette
        self.top           = self.__initialize_line(end_y, index + 1)
        self.bottom        = self.__initialize_line(start_y, index)

    def project(self, camera_x, curve, curve_delta, position, player_y):
        self.__project_line("top", camera_x - curve - curve_delta, position, player_y)
        self.__project_line("bottom", camera_x - curve, position, player_y)

    def should_ignore(self, segment):
        return self.top["camera"]["z"] <= GameSetting.CAMERA_DEPTH or self.top["screen"]["y"] <= segment.top["screen"]["y"] or self.bottom["screen"]["y"] >= self.top["screen"]["y"]

    def render_grass(self, window):
        top    = self.top["screen"]
        bottom = self.bottom["screen"]
        height = top["y"] - bottom["y"]
        y      = GameSetting.DIMENSIONS[1] - top["y"]
        col    = GameSetting.COLOURS["tunnel"] if self.in_tunnel else self.palette["grass"]
        pygame.draw.rect(window, col,(0, y, GameSetting.DIMENSIONS[0], height),int(height <= 1))

    def render_road(self, window):
        top      = self.top["screen"]
        bottom   = self.bottom["screen"]
        y_top    = (GameSetting.DIMENSIONS[1] - top["y"])
        y_bottom = (GameSetting.DIMENSIONS[1] - bottom["y"])
        col      = self.palette
        # Road.
        points = [
            ((bottom["x"] - bottom["w"]), y_bottom),
            ((bottom["x"] + bottom["w"]), y_bottom),
            ((top["x"] + top["w"]),       y_top),
            ((top["x"] - top["w"]),       y_top)
        ]
        pygame.draw.polygon(window, col["road"], points)
        # Speed boost.
        if self.speed_boost and self.index % 5 == 0:
            points = [
                (bottom["x"], y_bottom),
                (bottom["x"] + bottom["w"], y_bottom),
                (top["x"] + (top["w"] / 2), y_top),
                (bottom["x"], y_bottom)
            ]
            pygame.draw.polygon(window, GameSetting.COLOURS["green"], points)
        top_footpath_width    = top["w"] / (GameSetting.LANES / 2.8)
        bottom_footpath_width = bottom["w"] / (GameSetting.LANES / 2.8)
        # Left footpath strip.
        if not self.in_tunnel:
            points = [
                ((bottom["x"] - bottom["w"] - bottom_footpath_width), y_bottom),
                ((bottom["x"] - bottom["w"]),                         y_bottom),
                ((top["x"] - top["w"]),                               y_top),
                ((top["x"] - top["w"] - top_footpath_width),          y_top)
            ]
            pygame.draw.polygon(window, col["footpath"], points)
            # Left gutter.
            pygame.draw.line(window, GameSetting.COLOURS["gutter"],(bottom["x"] - bottom["w"], y_bottom), (top["x"] - top["w"], y_top))
            # Right footpath strip.
            points = [
                ((bottom["x"] + bottom["w"] + bottom_footpath_width), y_bottom),
                ((bottom["x"] + bottom["w"]),                         y_bottom),
                ((top["x"] + top["w"]),                               y_top),
                ((top["x"] + top["w"] + top_footpath_width),          y_top)
            ]
            pygame.draw.polygon(window, col["footpath"], points)
            # Right gutter.
            pygame.draw.line(window, GameSetting.COLOURS["gutter"],(bottom["x"] + bottom["w"], y_bottom), (top["x"] + top["w"], y_top))
        if (self.index / GameSetting.RUMBLE_LENGTH) % 2 == 0:
            # Road lanes.
            top_line_width    = top["w"] / (GameSetting.LANES * 8)
            bottom_line_width = bottom["w"] / (GameSetting.LANES * 8)
            step              = 1 / float(GameSetting.LANES)
            # Render each lane separator.
            for lane in range(GameSetting.LANES - 1):
                lane_percent  = step * (lane + 1)
                lane_bottom_w = (bottom["w"] * 2) * lane_percent
                lane_top_w    = (top["w"] * 2) * lane_percent
                bottom_left   = bottom["x"] - bottom["w"] + lane_bottom_w
                bottom_right  = bottom_left + bottom_line_width
                top_left      = top["x"] - top["w"] + lane_top_w
                top_right     = top_left + top_line_width
                points = [
                    (bottom_left,  y_bottom),
                    (bottom_right, y_bottom),
                    (top_right,    y_top),
                    (top_left,     y_top)
                ]
                pygame.draw.polygon(window, col["line"], points)

    def render_polygons(self, window, full_clip):
        for obj in self.pre_polygons:
            obj.render(window, self.bottom["screen"], self.clip, full_clip)

    def render_world_objects(self, window):
        for obj in (self.sprites + self.competitors + self.post_polygons):
            obj.render(window, self)

    def render_tunnel_roof(self, window, highest_y):
        if not self.tunnel_end:
            pygame.draw.rect(window, GameSetting.COLOURS["tunnel"],(0, 0, GameSetting.DIMENSIONS[0], GameSetting.DIMENSIONS[1] - highest_y))
        else:
            # I am mirroring the roof and road segment heights here.
            # Not sure if this will work in all circumstances (hills, etc).
            pygame.draw.rect(window, GameSetting.COLOURS["tunnel"], (0, 0, GameSetting.DIMENSIONS[0], self.top["screen"]["y"] - (GameSetting.TUNNEL_HEIGHT / 4)))

    def render_left_tunnel(self, window):
        bottom   = self.bottom["screen"]
        y_bottom = (GameSetting.DIMENSIONS[1] - bottom["y"])
        points = [
            (0, y_bottom),
            ((bottom["x"] - bottom["w"]), y_bottom),
            ((bottom["x"] - bottom["w"]), 0),
            (0, 0)
        ]
        pygame.draw.polygon(window, GameSetting.COLOURS["tunnel"], points)

    def render_right_tunnel(self, window):
        bottom   = self.bottom["screen"]
        y_bottom = (GameSetting.DIMENSIONS[1] - bottom["y"])
        points = [
            ((bottom["x"] + bottom["w"]), y_bottom),
            (GameSetting.DIMENSIONS[0], y_bottom),
            (GameSetting.DIMENSIONS[0], 0),
            ((bottom["x"] + bottom["w"]), 0)
        ]
        pygame.draw.polygon(window, GameSetting.COLOURS["tunnel"], points)

    def remove_sprite(self, sprite):
        try:
            self.sprites.remove(sprite)
        except Exception:
            pass

    def __project_line(self, line, camera_x, camera_z, player_y):
        p      = getattr(self, line)
        width  = GameSetting.DIMENSIONS[0] / 2
        height = GameSetting.DIMENSIONS[1] / 2
        p["camera"]["x"] = p["world"].get("x", 0) - camera_x
        p["camera"]["y"] = p["world"].get("y", 0) - (GameSetting.CAMERA_HEIGHT + player_y)
        p["camera"]["z"] = p["world"].get("z", 0) - camera_z
        p["screen"]["s"] = GameSetting.CAMERA_DEPTH / p["camera"]["z"]
        p["screen"]["x"] = round(width + (p["screen"]["s"] * p["camera"]["x"] * width))
        p["screen"]["y"] = round(height + (p["screen"]["s"] * p["camera"]["y"] * height))
        p["screen"]["w"] = round(p["screen"]["s"] * GameSetting.ROAD_WIDTH * width)

    def __initialize_line(self, y, height):
        return {"world": {"y": y,"z": (height * GameSetting.SEGMENT_HEIGHT)},"camera": {},"screen": {}}

class Sprite(WorldObject):
    def __init__(self, name, x, y):
        self.offset     = x
        self.offset_y   = y
        self.sprite     = GameSetting.SPRITES[name]
        self.hit        = False
        WorldObject.__init__(self)

    def is_hooker(self):
        return "hooker" in self.sprite

    def is_speed_boost(self):
        return "speed_boost" in self.sprite

    def is_bonus(self):
        return "bonus" in self.sprite

    def path(self):
        sprite_name = self.sprite["path"]
        if self.is_hooker() and self.hit:
            sprite_name = sprite_name.replace(".", "_dead.")
        return pygame.image.load(os.path.join("assets/img", sprite_name))

class TitleScreen:
    def __init__(self):
        self.finished   = False
        self.ready      = False
        self.background = pygame.image.load(os.path.join("assets/img", "title.png"))
        self.logo_a     = pygame.image.load(os.path.join("assets/img", "title_swervin.png"))
        self.logo_b     = pygame.image.load(os.path.join("assets/img", "title_mervin.png"))
        self.bg_offset  = 0
        self.font       = pygame.font.Font(GameSetting.FONTS["retro_computer"], 22)
        self.state      = 0
        self.frame      = 0
        self.logo_a_off = -420
        self.logo_b_off = GameSetting.DIMENSIONS[0]
        
    def progress(self, window):
        self.frame += 1
        window.fill(GameSetting.COLOURS["black"])
        self.state_0_step(window)
        self.state_1_step(window)
        self.state_2_step(window)
        for e in pygame.event.get():
            Util.try_quit(e)
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN and self.ready:
                pygame.mixer.music.fadeout(1500)
                self.finished = True

    def state_0_step(self, window):
        w, h = GameSetting.DIMENSIONS
        colours = [(100, 100, 10), (120, 130, 10), (150, 160, 10), (170, 180, 10), (190, 200, 10)]
        colour = colours[int(self.frame / 5) % 5]
        window.blit(self.background, (0, 0), (0, self.bg_offset, w, h))
        pygame.draw.circle(window, colour, (88, (h + 176) - self.bg_offset), 3)
        pygame.draw.circle(window, colour, (106, (h + 176) - self.bg_offset), 3)
        pygame.draw.circle(window, colour, (287, (h + 397) - self.bg_offset), 3)
        pygame.draw.circle(window, colour, (357, (h + 397) - self.bg_offset), 3)
        pygame.draw.circle(window, colour, (492, (h + 236) - self.bg_offset), 3)
        pygame.draw.circle(window, colour, (501, (h + 233) - self.bg_offset), 3)
        pygame.draw.circle(window, colour, (506, (h + 234) - self.bg_offset), 3)
        pygame.draw.circle(window, colour, (603, (h + 192) - self.bg_offset), 3)
        pygame.draw.polygon(window, colour,((189, (h + 273) - self.bg_offset),(189, (h + 243) - self.bg_offset),(193, (h + 273) - self.bg_offset),(193, (h + 243) - self.bg_offset)))
        if self.state == 0:
            if self.bg_offset + h >= self.background.get_height():
                self.state = 1
            else:
                self.bg_offset += 2

    def state_1_step(self, window):
        if not self.state == 0:
            center_a = ((GameSetting.DIMENSIONS[0] - self.logo_a.get_width()) / 2)
            center_b = ((GameSetting.DIMENSIONS[0] - self.logo_b.get_width()) / 2)
            window.blit(self.logo_b, (self.logo_b_off, 158))
            window.blit(self.logo_a, (self.logo_a_off, 34))
            if self.state == 1:
                if self.logo_a_off < center_a:
                    self.logo_a_off += 10
                elif self.logo_b_off > center_b:
                    self.logo_b_off -= 10
                else:
                    self.state = 2
    
    def state_2_step(self, window):
        if self.state == 2:
            w, h = GameSetting.DIMENSIONS
            if (self.frame / 20) % 2 == 1:
                self.ready = True
                ic = self.font.render("Press Start", 1, GameSetting.COLOURS["red"])
                x  = (w - ic.get_size()[0]) / 2
                y  = (h - ic.get_size()[1]) - 120
                window.blit(ic, (x, y))

class TunnelEntrance:
    def __init__(self, colour):
        self.quantifier = 3
        self.colour     = colour

    def render(self, window, segment):
        coords     = segment.bottom["screen"]
        s_width    = GameSetting.DIMENSIONS[0]
        s_height   = int(GameSetting.TUNNEL_HEIGHT * coords["s"] * GameSetting.ROAD_WIDTH * self.quantifier)
        x          = 0
        y          = GameSetting.DIMENSIONS[1] - coords["y"] - s_height
        top_clip   = GameSetting.DIMENSIONS[1] - segment.clip[1] - y
        #  Player can see the tunnel approaching.
        if top_clip > 0:
            e_height = int(s_height * 0.7)
            surf     = pygame.Surface([s_width, s_height], pygame.SRCALPHA, 32)
            surf     = surf.convert_alpha()
            points   = [
                (s_width, s_height),
                (coords["x"] + coords["w"], s_height),
                (coords["x"] + coords["w"], s_height - e_height),
                (coords["x"] - coords["w"], s_height - e_height),
                (coords["x"] - coords["w"], s_height),
                (0, s_height),
                (0, 0),
                (s_width, 0)
            ]
            pygame.draw.polygon(surf, self.colour, points)
            window.blit(surf, (x, y), (0, 0, s_width, top_clip))

class TunnelInside:
    def __init__(self):
        self.quantifier = 3

    def render(self, window, coords, clip, coverage):
        # Roof.
        s_width  = GameSetting.DIMENSIONS[0]
        s_height = int(GameSetting.TUNNEL_HEIGHT * coords["s"] * GameSetting.ROAD_WIDTH * self.quantifier)
        x        = 0
        y        = GameSetting.DIMENSIONS[1] - coords["y"] - s_height
        top_clip = GameSetting.DIMENSIONS[1] - coverage[1].top["screen"]["y"]
        s_height -= ((y + s_height) - top_clip)
        points = (x, y, s_width, s_height)
        pygame.draw.rect(window, GameSetting.COLOURS["tunnel"], points)
        # Left wall.
        l_bottom = coverage[0].bottom["screen"]
        if l_bottom["w"] < GameSetting.DIMENSIONS[0] and l_bottom["w"] > 0:
            ly_bottom = (GameSetting.DIMENSIONS[1] - l_bottom["y"])
            l_x       = l_bottom["x"] - l_bottom["w"]
            points = [
                (0, ly_bottom),
                (l_x, ly_bottom),
                (l_x, y),
                (0, y)
            ]
            pygame.draw.polygon(window, GameSetting.COLOURS["tunnel"], points)
        # Right wall.
        r_bottom = coverage[2].bottom["screen"]
        if r_bottom["w"] < GameSetting.DIMENSIONS[0] and r_bottom["w"] > 0:
            ry_bottom = (GameSetting.DIMENSIONS[1] - r_bottom["y"])
            r_x       = r_bottom["x"] + r_bottom["w"]
            points = [
                (r_x, ry_bottom),
                (GameSetting.DIMENSIONS[0], ry_bottom),
                (GameSetting.DIMENSIONS[0], y),
                (r_x, y)
            ]
            pygame.draw.polygon(window, GameSetting.COLOURS["tunnel"], points)

class Level:
    def __init__(self, details):
        self.name        = details["name"]
        self.slug        = details["id"]
        self.song        = details["song"]
        self.laps        = details["laps"]
        self.backgrounds = map(lambda bg: Background(bg["id"], bg["speed"], bg["scale"], bg["convert"]), details["backgrounds"])
        self.palettes    = details["colours"]
        self.finished    = False
        self.segments    = []
        self.competitors = []

    def build(self):
        build_path = lambda p: os.path.join("vantagel", "levels", p, "{0}.csv".format(self.slug))

        with open(build_path("tracks"), "r") as csvfile:
            for row in csv.reader(csvfile):
                flts = map(lambda c: float(c), row)
                self.add_segment(*flts)

        with open(build_path("sprites"), "r") as csvfile:
            for row in csv.reader(csvfile):
                if row[1] == "speed_boost":
                    self.add_speed_boost(int(row[0]), float(row[2]))
                else:
                    segment = self.segments[int(row[0])]
                    self.add_sprite(segment, row[1], float(row[2]), float(row[3]))

        with open(build_path("competitors"), "r") as csvfile:
            for row in csv.reader(csvfile):
                self.add_competitor(int(row[0]), float(row[1]), row[2], float(row[3]))

        with open(build_path("tunnels"), "r") as csvfile:
            for row in csv.reader(csvfile):
                self.add_tunnel(int(row[0]), int(row[1]))

    def add_segment(self, curve, start_y=0, end_y=0):
        palette = "dark" if (len(self.segments) / GameSetting.RUMBLE_LENGTH) % 2 == 0 else "light"
        segment = Segment(self.palettes[palette], len(self.segments), curve, start_y, end_y)
        self.segments.append(segment)

    def add_sprite(self, segment, name, x, y=0.0):
        sprite = Sprite(name, x, y)
        segment.sprites.append(sprite)

    def add_polygon(self, segment, klass, when="pre", args=[]):
        obj = klass(*args)
        if when == "pre":
            segment.pre_polygons.append(obj)
        else:
            segment.post_polygons.append(obj)

    def insert_bonuses(self):
        segs = random.sample(self.segments, 2)
        for s in segs:
            offset = random.randint(-10, 10) / 10.0
            self.add_sprite(s, "bonus", offset)

    def add_speed_boost(self, position, offset):
        for n in range(0, GameSetting.SPEED_BOOST_LENGTH):
            segment = self.offset_segment(position + n)
            self.add_sprite(segment, "speed_boost", offset)
            segment.speed_boost = True

    def add_competitor(self, position, offset, name, speed):
        competitor = Competitor(position, offset, name, speed)
        self.competitors.append(competitor)

    def add_tunnel(self, start, end):
        for segment in self.segments[start:end]:
            segment.in_tunnel = True
            if segment.index % GameSetting.TUNNEL_LIGHT_FREQ == 0:
                self.add_sprite(segment, "tunnel_light", -1.0, 2.0)
                self.add_sprite(segment, "tunnel_light", 1.0, 2.0)
        self.segments[end-1].tunnel_end = True
        self.add_polygon(self.segments[start], TunnelInside, "pre")
        self.add_polygon(self.segments[start], TunnelEntrance, "post", [self.palettes["wall"]])
        self.add_sprite(self.segments[start], "tunnel_entrance", -1.0)
        self.add_sprite(self.segments[start], "tunnel_entrance", 1.85)

    def track_length(self):
        return len(self.segments) * GameSetting.SEGMENT_HEIGHT

    def find_segment(self, position):
        n = len(self.segments)
        i = int(round((position / GameSetting.SEGMENT_HEIGHT) % n))
        if i == n:
            i = 0
        return self.segments[i]

    def offset_segment(self, i):
        return self.segments[i % len(self.segments)]

class Game:
    def __init__(self, window, clock):
        self.window          = window
        self.clock           = clock
        self.paused          = False
        self.waiting         = False
        self.selected_player = 0
        self.player          = None
        self.level           = None
        self.high_scores     = HighScore()

    def play(self):
        if GameSetting.TITLE_SCREEN:
            self.__title_screen()
        if GameSetting.PLAYER_SELECT:
            self.__player_select()
        self.player = Player(self.high_scores.minimum_score(), self.selected_player)
        for i, lvl in enumerate(GameSetting.LEVELS):
            print(i)
            print(lvl)
            self.level = Level(lvl)

            self.player.reset(self.level.laps)
            self.level.build()

            if GameSetting.COUNTDOWN:
                self.__countdown(i + 1)

            pygame.mixer.music.load(os.path.join("assets/audio", self.level.song))
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(GameSetting.MUSIC_VOLUME)
            while not self.player.finished():
                if self.paused:
                    self.__pause_cycle()
                else:
                    self.__game_cycle()
                pygame.display.update()
                self.clock.tick(GameSetting.FPS)
            pygame.mixer.music.fadeout(1500)
            if not self.player.alive():
                break
        if self.player.alive():
            self.__credits_screen()
        ## Post-game high scores and wait for new player.
        if self.high_scores.is_high_score(self.player.points):
            self.high_scores.add_high_score(math.trunc(self.player.points))
        self.waiting = True

    def wait(self):
        heading_font = pygame.font.Font(GameSetting.FONTS["fipps"], 44)
        content_font = pygame.font.Font(GameSetting.FONTS["retro_computer"], 15)
        background   = pygame.image.load(os.path.join("assets/img", "title.png"))
        heading_text = heading_font.render("High Scores", 1, GameSetting.COLOURS["text"])
        y            = 120
        self.window.fill(GameSetting.COLOURS["black"])
        self.window.blit(background, (0, 0))
        self.window.blit(heading_text, (30, 3))
        for score in self.high_scores.high_scores:
            date_text  = content_font.render(score[0].strftime("%d %b %Y"), 1, GameSetting.COLOURS["text"])
            score_text = content_font.render(str(score[1]), 1, GameSetting.COLOURS["text"])
            self.window.blit(date_text, (30, y))
            self.window.blit(score_text, (230, y))
            y += 35
        pygame.display.update()
        while self.waiting:
            for e in pygame.event.get():
                Util.try_quit(e)
                if e.type == KEYDOWN and e.key in [K_UP, K_RETURN]:
                    self.waiting = False
            self.clock.tick(GameSetting.FPS)

    def __game_cycle(self):
        p = self.player
        l = self.level
        p.travel(l.track_length(), self.window)
        base_segment   = l.find_segment(p.position)
        player_segment = l.find_segment(p.position + GameSetting.PLAYER_Z)
        p.accelerate()
        p.steer(player_segment)
        p.climb(base_segment)
        p.detect_collisions(player_segment)
        p.handle_crash()
        # Sprinkle some random bonuses into the next lap if we are lucky.
        if p.new_lap:
            if random.randint(1, GameSetting.CHANCE_OF_BONUSES) == 1:
                l.insert_bonuses()
        # Move the other players.
        for c in l.competitors:
            old_seg = l.find_segment(c.position)
            c.travel(l.track_length())
            new_seg = l.find_segment(c.position)
            c.play_engine(p.position)
            if old_seg.index != new_seg.index:
                if c in old_seg.competitors:
                    old_seg.competitors.remove(c)
                new_seg.competitors.append(c)
        coverage    = [base_segment, base_segment, base_segment]
        tunnel_exit = base_segment
        pre_renders = []
        curve       = 0
        curve_delta = -(base_segment.curve * p.segment_percent())
        # Position backgrounds according to current curve.
        for bg in l.backgrounds:
            if base_segment.curve != 0:
                bg.step(base_segment.curve, p.speed_percent())
            bg.render(self.window)
        # Loop through segments we should draw for this frame.
        for i in range(GameSetting.DRAW_DISTANCE):
            segment            = l.offset_segment(base_segment.index + i)
            projected_position = p.position
            camera_x           = p.x * GameSetting.ROAD_WIDTH
            # Past end of track and looped back.
            if segment.index < base_segment.index:
                projected_position -= l.track_length()
            segment.project(camera_x,curve,curve_delta,projected_position,p.y)
            curve       += curve_delta
            curve_delta += segment.curve
            # Remember biggest LEFT, TOP, RIGHT coordinates so we can clip sprites later.
            segment.clip = [coverage[0].bottom["screen"]["x"] - coverage[0].bottom["screen"]["w"],coverage[1].top["screen"]["y"],coverage[2].bottom["screen"]["x"] + coverage[2].bottom["screen"]["w"]]
            if len(segment.pre_polygons) > 0:
                pre_renders.append(segment)
            if segment.tunnel_end:
                tunnel_exit = segment
            if segment.should_ignore(coverage[1]):
                continue
            segment.render_grass(self.window)
            segment.render_road(self.window)
            if (segment.top["screen"]["y"] > coverage[1].top["screen"]["y"]):
                coverage[1] = segment
            # Remember where we should draw the left and right tunnel walls.
            if segment.in_tunnel:
                s_top  = segment.top["screen"]
                tl_top = coverage[0].top["screen"]
                tr_top = coverage[2].top["screen"]
                if (s_top["x"] - s_top["w"]) > (tl_top["x"] - tl_top["w"]):
                    coverage[0] = segment
                if (s_top["x"] + s_top["w"]) < (tr_top["x"] + tr_top["w"]):
                    coverage[2] = segment
        # Draw tunnel roof and walls.
        if base_segment.in_tunnel:
            self.player.in_tunnel = True
            tunnel_exit.render_tunnel_roof(self.window, coverage[1].top["screen"]["y"])
            coverage[0].render_left_tunnel(self.window)
            coverage[2].render_right_tunnel(self.window)
        else:
            self.player.in_tunnel = False
        # Let backgrounds know how much height they need to cover on the next paint.
        for bg in l.backgrounds:
            bg.visible_height = GameSetting.DIMENSIONS[1] - coverage[1].top["screen"]["y"]
        # Draw sprites in from back to front (painters algorithm).
        for segment in reversed(pre_renders):
            segment.render_polygons(self.window, coverage)
        for i in reversed(range(1, GameSetting.DRAW_DISTANCE)):
            segment = l.offset_segment(base_segment.index + i)
            segment.render_world_objects(self.window)
        p.render(self.window, base_segment)
        p.render_hud(self.window)
        if p.blood_alpha > 0:
            p.render_blood(self.window)
        for e in pygame.event.get():
            Util.try_quit(e)
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
                pygame.mixer.music.pause()
                self.paused = True
        # Steering, acceleration.
        keys = pygame.key.get_pressed()
        p.set_acceleration(keys)
        p.set_direction(keys)

    def __pause_cycle(self):
        pause_font = pygame.font.Font(s.FONTS["retro_computer"], 64)
        pause_text = pause_font.render("Paused", 1, GameSetting.COLOURS["text"])
        x          = (GameSetting.DIMENSIONS[0] - pause_text.get_width()) / 2
        y          = (GameSetting.DIMENSIONS[1] - pause_text.get_height()) / 2
        self.window.fill(GameSetting.COLOURS["black"])
        self.window.blit(pause_text, (x, y))
        for e in pygame.event.get():
            Util.try_quit(e)
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
                pygame.mixer.music.unpause()
                self.paused = False

    def __progress(self, screen, fps):
        while not screen.finished:
            screen.progress(self.window)
            pygame.display.update()
            self.clock.tick(fps)

    def __title_screen(self):
        title_screen = TitleScreen()
        pygame.mixer.music.load(os.path.join("assets/audio", "mn84-theme.ogg"))
        pygame.mixer.music.play(-1)
        self.__progress(title_screen, GameSetting.TITLE_FPS)

    def __countdown(self, level_number):
        countdown = CountDown(level_number, self.level.name)
        self.__progress(countdown, GameSetting.COUNTDOWN_FPS)

    def __player_select(self):
        player_select = PlayerSelect()
        self.__progress(player_select, GameSetting.PLAYER_SELECT_FPS)
        self.selected_player = player_select.selected

    def __credits_screen(self):
        credits = Credit()
        self.__progress(credits, GameSetting.CREDITS_FPS)

class GameLauncher:
    @staticmethod
    def launch():
        pygame.init()
        pygame.display.set_caption("VANTAGE")
        if GameSetting.FULL_SCREEN:
            w_flag = pygame.FULLSCREEN
            pygame.mouse.set_visible(False)
        else:
            w_flag = 0
        fps_clock = pygame.time.Clock()
        window    = pygame.display.set_mode(GameSetting.DIMENSIONS, w_flag)
        game      = Game(window, fps_clock)
        while True:
            if game.waiting:
                game.wait()
            else:
                game.play()

if __name__ == "__main__":
    GameLauncher.launch()
