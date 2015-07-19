import Config
import Dictionary
import praw

def main():
	r = praw.Reddit(user_agent = Config.user_agent)
	r.login(Config.username, Config.password)
	subreddit = r.get_subreddit(Config.subreddit)
	people = []
	for flair in subreddit.get_flair_list():
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
			college = text
		print user, "(" + college + ")"

def die():
	sys.exit(1)

if __name__ == "__main__":
	try:
		main()
	except SystemError:
		print "Bot was killed."
	
