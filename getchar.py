# coding : utf-8
import tweepy

def get_char(screen_names):
	
	CK = 'vsSKClk3Ns1RMluhnRSlZg'
	CS = 'NFUjQsGXhtEMkIEIRugYBELYQEAmm6CEO0oJkdyzryE'
	AT = '264147645-yRyNecmabuptv164633gf9tpEgJ2MFygLOUT22yA'
	AS = 'qQxPgJe5YODfP61rrFg5Z2KSckAT37oKEKiOuO0rmwo'

	auth = tweepy.OAuthHandler(CK,CS)
	auth.set_access_token(AT,AS)
	api = tweepy.API(auth)
	
	users = []
	for screen_name in screen_names:
		users.append(api.get_user(screen_name=screen_name))
	
	return users

if __name__ == '__main__':
	List =  get_char(['genya0407','bot_nakatsu','klppts','penguin2716'])
	
	for i in List:
		print i.name,i.statuses_count,i.friends_count,i.followers_count,i.favourites_count
