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
		cleaned = text
		# flair pre-processing
		if cleaned.count(" ") >= 2:
			cleaned = " ".join(cleaned.split(" ")[0:2])
		postfix = ["'", "(", "-"]
		for char in postfix:
			if char in cleaned:
				cleaned = cleaned[:cleaned.index(char)]
		cleaned = cleaned.strip().lower()
		if cleaned in Dictionary.translate:
			college = Dictionary.translate[cleaned]
		elif cleaned == "":
			college = "{ Flair not set }"
		else:
			college = "{ Flair not recognized }"
			user = user + ' (' + (cleaned).encode('ascii', 'replace') + ')'
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
	
