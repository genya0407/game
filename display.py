# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

FONT_SIZE = 32

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 360
SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)

OWN_SIZE = 50
ENEMY_SIZE = 30

def main():
	pygame.init()
	screen = pygame.display.set_mode( SCREEN_SIZE )
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
	for enemy in ['pyooooon157','lef_sou_220_w','amanae410','inagaku0715']:
		c_f = font.render(enemy, True, (0,0,0),(255,255,255))
		c_board = pygame.Surface((240,60))
		c_board.fill((255,255,153))
		c_board.blit(c_f, ( c_board.get_width()/2 - c_f.get_width()/2 , c_board.get_height()/2 - c_f.get_height()/2 ) )
		c_item = [c_board,enemy]
		enemy_choices.append(c_item)
	
	print(enemy_choices)
	
	means = 0
	target = 0
	while True:
		screen.fill((255,255,255))
		
		if means == 0 and target == 0:
			screen.blit(p_board,(0, SCREEN_HEIGHT*2/3))
			screen.blit(m_board,(SCREEN_WIDTH/2,SCREEN_HEIGHT*2/3))
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
		
		elif ( means != 0 and target == 0 ):
			screen.blit(enemy_choices[0][0],(0, SCREEN_HEIGHT*2/3))
			screen.blit(enemy_choices[1][0],(SCREEN_WIDTH/2, SCREEN_HEIGHT*2/3))
			screen.blit(enemy_choices[2][0],(0, SCREEN_HEIGHT*5/6))
			screen.blit(enemy_choices[3][0],(SCREEN_WIDTH/2, SCREEN_HEIGHT*5/6))
			
			pygame.display.update()
			
			for event in pygame.event.get():
				
				if event.type == MOUSEBUTTONDOWN and event.button == 1:
					x, y = event.pos
					
					if ( x > 0 and x < SCREEN_WIDTH / 2 ) and ( y > SCREEN_HEIGHT*2/3 and y < SCREEN_HEIGHT*5/6 ):
						print(enemy_choices[0][1] + ' に攻撃')
						target = enemy_choices[0][1]
						
					if ( x > SCREEN_WIDTH / 2 and x < SCREEN_WIDTH ) and ( y > SCREEN_HEIGHT*2/3 and y < SCREEN_HEIGHT*5/6 ):
						print(enemy_choices[2][1] + ' に攻撃')
						target = enemy_choices[2][1]
						
					if ( x > 0 and x < SCREEN_WIDTH / 2 ) and ( y > SCREEN_HEIGHT*5/6 and y < SCREEN_HEIGHT ):
						print(enemy_choices[0][1] + ' に攻撃')
						target = enemy_choices[0][1]
						
					if ( x > SCREEN_WIDTH / 2 and x < SCREEN_WIDTH ) and ( y > SCREEN_HEIGHT*5/6 and y < SCREEN_HEIGHT ):
						print(enemy_choices[0][1] + ' に攻撃')
						target = enemy_choices[0][1]
				
				if event.type == QUIT:
					exit()
				
				if ( event.type == KEYDOWN and event.key == K_ESCAPE):
					exit()
		
		elif ( means != 0 and target != 0 ):
			if means == 'phisic':
				print('%s に物理攻撃' % target)
			elif means == 'magic':
				print('%s に魔法攻撃' % target)
			
			for event in pygame.event.get():
				if event.type == QUIT:
					exit()
				
				if ( event.type == KEYDOWN and event.key == K_ESCAPE):
					exit()
		
if __name__ == '__main__':
	main()
