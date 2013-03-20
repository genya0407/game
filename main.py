# -*- coding: utf-8 -*-
import tweepy
import urllib
import os.path
import pygame
from pygame.locals import *

FONT_SIZE = 32

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 360
SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)

OWN_SIZE = 50
ENEMY_SIZE = 30

class Center(object):
    def __init__(self,own,enemy):
        
        #キャラクターをメンバ変数に
        self.own_party = []
        for i,c in enumerate(own):
            c.NUMBER = i
            self.own_party.append(c)
        
        #攻撃するキャラクターを選択する機構はまだ作ってないので、NUMBER=0のキャラが攻撃するという事にする
        self.oneself_number = 0
        
        self.enemy_party = []
        for i,c in enumerate(enemy):
            c.NUMBER = i
            self.enemy_party.append(c)
        
        self.display()
    
    def attack(self,own_char_number,enemy_char_number,command):
        
        #攻撃する人とされる人を特定(?)
        own_char = self.own_party[own_char_number]
        enemy_char = self.enemy_party[enemy_char_number]
        
        #攻撃方法増やすならもっと綺麗に書く方法考えたほうがいいかも
        if command == 'phisic':
            damage = own_char.ATK - enemy_char.DEF
        
        elif command == 'magic':
            damage = own_char.MGC - enemy_char.MTL
        
        #ダメージが負なら0にする
        if damage < 0:
            damage = 0
        
        #ダメージを与える
        self.enemy_party[enemy_char.NUMBER].HP = enemy_char.HP - damage
        
        #表示
        print u'%sに %d のダメージ！' % (self.enemy_party[enemy_char.NUMBER].NAME, damage)
        print u'%sのHP: %d' % (self.enemy_party[enemy_char.NUMBER].NAME, self.enemy_party[enemy_char.NUMBER].HP)
    
    def display(self):
        pygame.init()
        self.screen = pygame.display.set_mode( SCREEN_SIZE )
        pygame.display.set_caption('こんにちわ')
        
        font = pygame.font.Font('default.ttf',FONT_SIZE)
        
        #攻撃方法選択肢
        phisic = font.render(u'物理', True, (0,0,0),(0,0,102))
        p_board = pygame.Surface((240,120))
        p_board.fill((0,0,102))
        p_board.blit(phisic,Rect(p_board.get_width()/2 - FONT_SIZE, p_board.get_height()/2 - FONT_SIZE/2, p_board.get_width() , p_board.get_height()))
        
        magic = font.render(u'魔法', True, (0,0,0),(102,0,102))
        m_board = pygame.Surface((240,120))
        m_board.fill((102,0,102))
        m_board.blit(magic,Rect(m_board.get_width()/2 - FONT_SIZE, m_board.get_height()/2 - FONT_SIZE/2, m_board.get_width() , m_board.get_height()))
        
        #敵選択肢
        enemy_choices = []
        for enemy in self.enemy_party:
            c_f = font.render(enemy.NAME, True, (0,0,0),(255,255,255))
            c_board = pygame.Surface((240,60))
            c_board.fill((255,255,153))
            c_board.blit(c_f, ( c_board.get_width()/2 - c_f.get_width()/2 , c_board.get_height()/2 - c_f.get_height()/2 ) )
            
            icon = pygame.image.load(enemy.ICON).convert()
            
            c_item = [c_board,enemy.NAME,enemy.NUMBER]
            enemy_choices.append(c_item)
            self.enemy_party[enemy.NUMBER].ICON = icon
        
        means = 'false'
        target = 'false'
        while True:
            self.screen.fill((255,255,255))
            #アイコンを表示するところ　上2/3
            for i,c in enumerate(self.enemy_party):
                self.screen.blit(c.ICON,Rect(120*i,10,120,120))
            
            #下の選択肢選ぶところ　下1/3
            if means == 'false' and target == 'false':
                self.screen.blit(p_board,(0, SCREEN_HEIGHT*2/3))
                self.screen.blit(m_board,(SCREEN_WIDTH/2,SCREEN_HEIGHT*2/3))
                pygame.display.update()
            
                for event in pygame.event.get():
                    
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        x, y = event.pos
                        
                        if ( x > 0 and x < SCREEN_WIDTH / 2 ) and ( y > SCREEN_HEIGHT*2/3 and y < SCREEN_HEIGHT ):
                            print(u'物理で殴る')
                            means = 'phisic'
                        
                        elif ( x > SCREEN_WIDTH / 2 and x < SCREEN_WIDTH ) and ( y > SCREEN_HEIGHT*2/3 and y < SCREEN_HEIGHT ):
                            print(u'魔法でしばく')
                            means = 'magic'
                    
                    if event.type == QUIT:
                        exit()
                    
                    if ( event.type == KEYDOWN and event.key == K_ESCAPE):
                        exit()
            
            elif ( means != 'false' and target == 'false' ):
                self.screen.blit(enemy_choices[0][0],(0, SCREEN_HEIGHT*2/3))
                self.screen.blit(enemy_choices[1][0],(SCREEN_WIDTH/2, SCREEN_HEIGHT*2/3))
                self.screen.blit(enemy_choices[2][0],(0, SCREEN_HEIGHT*5/6))
                self.screen.blit(enemy_choices[3][0],(SCREEN_WIDTH/2, SCREEN_HEIGHT*5/6))
                
                pygame.display.update()
                
                for event in pygame.event.get():
                    
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        x, y = event.pos
                        
                        if ( x > 0 and x < SCREEN_WIDTH / 2 ) and ( y > SCREEN_HEIGHT*2/3 and y < SCREEN_HEIGHT*5/6 ):
                            print(enemy_choices[0][1] + u'に攻撃')
                            target = enemy_choices[0][2]
                            
                        if ( x > SCREEN_WIDTH / 2 and x < SCREEN_WIDTH ) and ( y > SCREEN_HEIGHT*2/3 and y < SCREEN_HEIGHT*5/6 ):
                            print(enemy_choices[2][1] + u'に攻撃')
                            target = enemy_choices[2][2]
                            
                        if ( x > 0 and x < SCREEN_WIDTH / 2 ) and ( y > SCREEN_HEIGHT*5/6 and y < SCREEN_HEIGHT ):
                            print(enemy_choices[0][1] + u'に攻撃')
                            target = enemy_choices[0][2]
                            
                        if ( x > SCREEN_WIDTH / 2 and x < SCREEN_WIDTH ) and ( y > SCREEN_HEIGHT*5/6 and y < SCREEN_HEIGHT ):
                            print(enemy_choices[0][1] + u'に攻撃')
                            target = enemy_choices[0][2]
                    
                    if event.type == QUIT:
                        exit()
                    
                    if ( event.type == KEYDOWN and event.key == K_ESCAPE):
                        exit()
            
            elif ( means != 'false' and target != 'false' ):
                if means == 'phisic':
                    print(u'%sに物理攻撃' % self.enemy_party[target].NAME)
                    
                    self.attack(self.oneself_number,target,means)
                    
                    means = 'false'
                    target = 'false'
                elif means == 'magic':
                    print(u'%sに魔法攻撃' % self.enemy_party[target].NAME)
                    
                    self.attack(self.oneself_number,target,means)
                    
                    means = 'false'
                    target = 'false'
                
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()
                    
                    if ( event.type == KEYDOWN and event.key == K_ESCAPE):
                        exit()
		


class Character(object):
    def __init__(self,Name,Icon,Hp,Atk,Def,Mgc,Mtl):
        self.HP = Hp
        self.ATK = Atk
        self.DEF = Def
        self.MGC = Mgc
        self.MTL = Mtl
        
        self.NAME = Name
        self.ICON = Icon
        self.NUMBER = 0 # デフォルト値

def get_char(screen_names):
    
    CK = 'vsSKClk3Ns1RMluhnRSlZg'
    CS = 'NFUjQsGXhtEMkIEIRugYBELYQEAmm6CEO0oJkdyzryE'
    
    AT = '264147645-YGnNcCKeW7tSQhIgjlcQ3kOsKrRlOmuP5C14eB8y'
    AS = '8NbYpNolDmUUjlmT1olHLfT4girkqGyQXg8cKdg1c'
    
    auth = tweepy.OAuthHandler(CK,CS)
    auth.set_access_token(AT,AS)
    api = tweepy.API(auth)
    
    u = []
    for screen_name in screen_names:
        u.append(api.get_user(screen_name=screen_name))

    users = []
    path = '/home/yusuke/github/game/icon/'
    for user in u:
        root, ext = os.path.splitext(user.profile_image_url)
        savepath = path + user.screen_name + ext
        urllib.urlretrieve( user.profile_image_url , savepath )
        user.icon = savepath
        users.append(user)
    
    return users

def main(): #デモ動作
    #キャラクターのインスタンスを生成
    #NAME = 名前,HP = ツイート数,ATK=フォロイー,DEF=フォロワー,MGC=ふぁぼ数,MTL=フォロワー ← ふぁぼられ数にしようと思ったが取得方法がわからないので後回し
    

    #味方キャラ作成
    twitter_user_list = get_char(['genya0407','bot_nakatsu','klppts','penguin2716'])
    
    own_char_list = []
    for user in twitter_user_list:
        c = Character(  user.name,
                        user.icon,
                        user.statuses_count,
                        user.friends_count,
                        user.followers_count,
                        user.favourites_count,
                        user.followers_count  )
        own_char_list.append(c)
    
    #敵キャラ作成
    twitter_user_list = get_char(['pyooooon157','lef_sou_220_w','amanae410','inagaku0715'])
    
    enemy_char_list = []
    for user in twitter_user_list:
        c = Character(  user.name,
                        user.icon,
                        user.statuses_count,
                        user.friends_count,
                        user.followers_count,
                        user.favourites_count,
                        user.followers_count  )
        enemy_char_list.append(c)
    
    center = Center(own_char_list,enemy_char_list)

if __name__ == '__main__':
    main()
