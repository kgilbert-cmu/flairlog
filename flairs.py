import Config
import Dictionary
import praw

def main():
	r = praw.Reddit(user_agent = Config.user_agent)
	r.login(Config.username, Config.password)
	subreddit = r.get_subreddit(Config.subreddit)
	collect = {}
	for flair in subreddit.get_flair_list(limit = None):
		(_, user, text) = flair.values()
		# flair pre-processing
		postfix = ["'", "(", "-"]
		for char in postfix:
			if char in text:
				text = text[:text.index(char)]
		text = text.strip().lower()
		if text in Dictionary.translate:
			college = Dictionary.translate[text]
		else:
			college = "{ Flair not set }"
		if college in collect:
			collect[college].append('/u/' + user)
		else:
			collect[college] = ['/u/' + user]
	for college in sorted(collect):
		print "###", college, "\n*", "\n* ".join(collect[college]), "\n"

def die():
	sys.exit(1)

if __name__ == "__main__":
	try:
		main()
	except SystemError:
		print "Bot was killed."
	
