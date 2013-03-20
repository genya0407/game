# -*- coding: utf8 -*-
import pickle

Character = {
    "hp":           0, #HitPoint   体力
    "mp":           0, #MagicPoint マジックポイント
    "spd":          0, #Speed      すばやさ
    "atk":          0, #Attack     物理攻撃力
    "def":          0, #Defence    物理防御力
    "mgc":          0, #Magic      魔法攻撃力
    "mtl":          0, #Mental     魔法防御力
    "name": "someone", #Name       名前
    "id":           0, #Id         キャラ固有の番号 000~999
    "number":       0, #Number     パーティ内で一意に決める番号
    "act_flag":  True, #Act_flag   そのターンの攻撃権
    "dead_flag":False  #Dead_flag  瀕死状態であるかどうか
}

Party = {
	"name":    None,
    "first":   None,
    "second":  None,
    "third":   None,
    "fourth":  None
}

def create_character(params,number):
    
    character = {
        "hp":       params[0] , #HitPoint       体力
        "mp":       params[1] , #MagicPoint     マジックポイント
        "spd":      params[2] , #Speed          すばやさ
        "atk":      params[3] , #Attack         物理攻撃力
        "def":      params[4] , #Defence        物理防御力
        "itl":      params[5] , #Intelligence   魔法攻撃力
        "spl":      params[6] , #Spirit         魔法防御力
        "name":     params[7] , #Name           名前
        "id":       params[8] , #Id             キャラ固有の番号 000~999
        "number":   number    , #Number         パーティ内で一意に決める番号 0~3
        "act_flag": params[9] , #Act_flag       そのターンの攻撃権
        "dead_flag":params[10]  #Dead_flag      瀕死状態であるかどうか
    }
    
    return character

def create_party(parameters,name):

    a = create_character(parameters[0],0)
    b = create_character(parameters[1],1)
    c = create_character(parameters[2],2)
    d = create_character(parameters[3],3)
    
    party = {
		"name"  : name,
		"first" : a,
		"second": b,
		"third" : c,
		"fourth": d
    }
    
    return party

def main():
    #キャラクターは、暫定的に、[戦士、武闘家、魔導師、僧侶] とする
    #         [HP、MP、SPD、ATK、DEF、ITL、SPL、NAME、      ID、NUMBER、ACT_FLAG、DEAD_FLAG、ICON]
    soldier = [500,0  ,200, 500, 400, 100, 200, "せんし"  , 0,  None,   False,    False]
    mars    = [500,0  ,300, 500, 300, 100, 200, "ぶとうか", 1,  None,   False,    False]
    wizard  = [300,200,250, 100, 200, 500, 400, "まどうし", 2,  None,   False,    False]
    monk    = [300,200,250, 100, 200, 500, 400, "そうりょ", 3,  None,   False,    False]
    
    party_params = [soldier,mars,wizard,monk]
    player_party = create_party(party_params,"player")
    
    f = open('player_party.pt', 'w')
    pickle.dump(player_party,f)
    f.close()
        
    #敵キャラは、暫定的に[トークン*4] とする
    token_a = [300,300,300, 300, 300, 300, 300, "トークンA",4,  None,   False,    False]
    token_b = [300,300,300, 300, 300, 300, 300, "トークンB",5,  None,   False,    False]
    token_c = [300,300,300, 300, 300, 300, 300, "トークンC",6,  None,   False,    False]
    token_d = [300,300,300, 300, 300, 300, 300, "トークンD",7,  None,   False,    False]
    
    party_params = [token_a,token_b,token_c,token_d]
    cpu_party = create_party(party_params,"cpu")
    
    f = open('cpu_party.pt','w')
    pickle.dump(cpu_party,f)
    f.close()

if __name__ == '__main__':
    main()
