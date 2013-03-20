# -*- coding: utf-8 -*-

class Center(object):
	def __init__(self, player_party, cpu_party):
		self.player_party = player_party
		self.cpu_party = cpu_party
		
		self.partyname_dict = {
			"player" : self.player_party,
			"cpu"    : self.cpu_party
		}
		
		self.battle()
		
	def standby_phase(self):
		#どちらが攻撃するか決める。 とりあえず、プレイヤーが攻撃すると固定してしまう。
		for key in self.player_party.keys():
			self.player_party[key][""]
		return self.player_party["name"]
		
	def battle_phase(self, attacking_party_name):
		while self.partyname_dict[attacking_party_name]["first"][]
		
		
		
	def end_phase()
		
		
		

	def battle(self):
		while True:
			
			attacking_party_name = self.standby_phase()
			
			self.battle_phase(attacking_party_name)
			
			self.end_phase()
