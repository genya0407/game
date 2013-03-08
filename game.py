# -*- coding: utf-8 -*-
import tweepy

class Center(object):
    def __init__(self,own,enemy):
        
        #キャラクターをメンバ変数に
        self.own_party = []
        for i,c in enumerate(own):
            c.NUMBER = i
            self.own_party.append(c)
        
        self.enemy_party = []
        for i,c in enumerate(enemy):
            c.NUMBER = i
            self.enemy_party.append(c)
    
    def attack(self,own_char_number,enemy_char_number,command):
        
        #攻撃する人とされる人を特定(?)
        own_char = self.own_party[own_char_number]
        enemy_char = self.enemy_party[enemy_char_number]
        
        #攻撃方法増やすならもっと綺麗に書く方法考えたほうがいいかも
        if command == 'phisical':
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


class Character(object):
    def __init__(self,Name,Hp,Atk,Def,Mgc,Mtl):
        self.HP = Hp
        self.ATK = Atk
        self.DEF = Def
        self.MGC = Mgc
        self.MTL = Mtl
        
        self.NAME = Name
        self.NUMBER = 0 # デフォルト値

def get_char(screen_names):
    
    CK = 'vsSKClk3Ns1RMluhnRSlZg'
    CS = 'NFUjQsGXhtEMkIEIRugYBELYQEAmm6CEO0oJkdyzryE'

    auth = tweepy.OAuthHandler(CK,CS)
    auth.set_access_token(AT,AS)
    api = tweepy.API(auth)
    
    users = []
    for screen_name in screen_names:
        users.append(api.get_user(screen_name=screen_name))
    
    return users

def main(): #デモ動作
    #キャラクターのインスタンスを生成
    #NAME = 名前,HP = ツイート数,ATK=フォロイー,DEF=フォロワー,MGC=ふぁぼ数,MTL=フォロワー ← ふぁぼられ数にしようと思ったが取得方法がわからないので後回し
    
    #味方キャラ作成
    twitter_user_list = get_char(['genya0407','bot_nakatsu','klppts','penguin2716'])
    
    own_char_list = []
    for user in twitter_user_list:
        c = Character(  user.name,
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
                        user.statuses_count,
                        user.friends_count,
                        user.followers_count,
                        user.favourites_count,
                        user.followers_count  )
        enemy_char_list.append(c)
    
    center = Center(own_char_list,enemy_char_list)
    center.attack(0,3,'magic')

if __name__ == '__main__':
    main()
