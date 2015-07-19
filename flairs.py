import Config
import praw

def main():
	r = praw.Reddit(user_agent = Config.user_agent)
	r.login(Config.username, Config.password)
	subreddit = r.get_subreddit(Config.subreddit)
	people = []
	for flair in subreddit.get_flair_list(limit = None):
		(_, user, text) = flair.values()
		if "'" in text:
			text = text[:text.index("'")]
		if "(" in text:
			text = text[:text.index("(")]
		if "-" in text:
			text = text[:text.index("-")]
		text = text.strip().lower()
		print user, "(" + text + ")"

def die():
	sys.exit(1)

if __name__ == "__main__":
	try:
		main()
	except SystemError:
		print "Bot was killed."
	
