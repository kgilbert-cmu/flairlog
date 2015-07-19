# flairlog
Collect and collate user flair from subreddits

## Setup
Fill in the relevant information for your PRAW user-agent, reddit username, and reddit user account password into a configuration file called `Config.py`. An example file is given.

## Setting your subreddit
Whatever subreddit you intend to mine flairs from, make sure your account is an active moderator of the subreddit. The option to select the subreddit name is also in `Config.py`.

## Flair Categories
Fill in content into `Dictionary.py` in order to "translate" a flair into a category title, which can be used to collect users into similar flair categories.

## Usage
No command line arguments, no parameters, no other files.

Just type `python flairs.py`
