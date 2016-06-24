"""This script logs into a user's reddit account, accesses
     one of their subreddits, collects all user flair, and
     builds a browse-able log of users grouped by flair
"""
import praw
import Config
import Dictionary


def main():
	"""Log into reddit, get subreddit data, print log to stdout
	"""
	r = praw.Reddit(user_agent=Config.user_agent)
	r.login(Config.username, Config.password)
	subreddit = r.get_subreddit(Config.subreddit)
	collect = {}
	for flair in subreddit.get_flair_list(limit=None):
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
		print "###", link(college), "\n*", "\n* ".join(collect[college]), "\n"


def link(college):
	"""string -> string
	    Sigma Chi customization: convert headers into FB links
	    Users can click on the name of a school to find friends
	"""
	if '{' in college:
		return college
	html = clean(college)
	fof = "https://www.facebook.com/search/people/?q=friends%20of%20my%20friends%20who%20are%20men%20and%20go%20to%20{}%20and%20like%20Sigma%20Chi%20Fraternity"
	return "[{}]({})".format(college, fof.format(html))


def clean(text):
	"""string -> string
	    remove non-compliant HTML text from school strings
	"""
	array = list(text)
	cleaned = []
	while len(array) > 0:
		char = array.pop(0)
		if char == " ":
			cleaned.append("%20")
		elif char == "(" or char == "[":
			counter = 1
			char = array.pop(0)
			while len(array) > 0 and counter >= 1:
				if char == "(" or char == "[":
					counter += 1
				elif char == ")" or char == "]":
					counter -= 1
				char = array.pop(0)
		else:
			cleaned.append(char)
	return "".join(cleaned)


if __name__ == "__main__":
	try:
		main()
	except SystemError:
		print "Bot was killed."

