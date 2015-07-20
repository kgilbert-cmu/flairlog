# flairlog
Collect and collate user flair from subreddits.

## Setup
Fill in the relevant information for your PRAW user-agent, reddit username, and reddit user account password into a configuration file called `Config.py`. An example file is given.

### Setting your subreddit
Whatever subreddit you intend to mine flairs from, make sure your account is an active moderator of the subreddit. The subreddit name parameter should be set in `Config.py`.

## Flair Categories
Fill in content into `Dictionary.py` in order to "translate" a flair into a category title, which can be used to collect users into similar flair categories.

## Usage
No command line arguments, no parameters, no other files.

Just type `python flairs.py`

#### On a Mac

To speed-up the process of uploading a flairlog to a subreddit wiki:

    $> python flairs.py > output.md
    $> pbcopy < output.md

Then navigate to your subreddit's wiki page and press <kbd>⌘</kbd><kbd>V</kbd> to paste the flairlog into the wiki textbox.

### Example

The output of the Markdown file can be copied back onto reddit like so:

![Example flairlog](/docs/images/example.png)

## Special Thanks

In honored memory of our dearly beloved brother Vinay Balaji (Carnegie Mellon '14), we will forever miss your smile and your spirit.
