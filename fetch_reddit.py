#!/usr/bin/env python3

# Instructions to run:

# Run this command from command line to run the Python script
# `./fetch_reddit.py`

# If you have any issues, check that the file is executable:
# `chmod +x fetch_reddit.py`

# Install any libraries that may be missing for example:
# `pip3 install praw`
# `pip3 install cloudpickle`

import praw, cloudpickle
import os.path
from os import path

print("\nFetching top posts from r/popular...\n")

reddit = praw.Reddit(client_id="DpRMmWJIniC52A",
     client_secret="Y4N1L3C_CvJ0xlf8WfQkA9dmC8Ou9w", # in a real production system we would not commit the client_secret to the github repository
     user_agent="get latest posts from r/popular"
)

# Post refers to a post on reddit and the relevant information
class Post:
	def __init__(self, id, title, score):
		self.id = id
		self.title = title
		self.score = score
	def __str__(self):
		return f'Post({self.id},{self.title},{self.score})'

# helper method to print a list of posts with a title
def printPosts(title, posts):
	print("\n")
	print(title + "\n")
	for post in posts:
		print(post.id + " - " + post.title)

# helper method to print a list of posts with title and change in votes
def printChangeVotesPosts(title, posts):
	print("\n")
	print(title + "\n")
	for post in posts:
		print(post.id + " - " + post.title, end='')
		if post.score > 0:
			print(" - increased votes by ", end='')
		else:
			print(" - decreased votes by ", end='')
		print(abs(post.score))

# results lists
newPosts, noLongerTopPosts, postWithChangedVotes = list(), list(), list()

# file to store previous posts in
filename = 'posts.cloudpickle'

# make a dict to read previous posts, and one to save new posts
posts_dictionary, save_dictionary = dict(), dict()

# if we have run the program before, load the previous posts
if path.exists(filename):
	with open(filename, 'rb') as handle:
		posts_dictionary = cloudpickle.load(handle)

# get the latest posts from the popular subreddit
got = reddit.subreddit('popular').hot(limit=75)
# iterate over the submissions in the popular subreddit
for submission in got:
	# add to the save dictionary in correct format to save for next execution
	save_dictionary[submission.id] = Post(submission.id, submission.title, submission.score)
	if submission.id not in posts_dictionary:
		# if the ID was not previously seen, we have a new post, so add it to the new posts list
		newPosts.append(Post(submission.id, submission.title, submission.score))
	else:
		if posts_dictionary[submission.id].score != submission.score:
			# if the post was previously seen, check if the votes have changed, if so store it as a post with changed votes
			postWithChangedVotes.append(Post(submission.id, submission.title, submission.score - posts_dictionary[submission.id].score)) # save the change in score
		# remove the post if the score has not changed - the post was previously seen with no score change
		del posts_dictionary[submission.id]	

# dictionary now contains the posts that are no longer top posts
# convert the no longer top posts from dict to a list
for post in posts_dictionary.values():
	noLongerTopPosts.append(Post(post.id, post.title, post.score))

# save the recent posts back to file
with open(filename, 'wb') as handle:
    cloudpickle.dump(save_dictionary, handle)

# print the relevant outputs - new posts, no longer top posts, and posts with changed votes
printPosts("New Posts [post ID - post title]:", newPosts)
printPosts("No longer top posts [post ID - post title]:", noLongerTopPosts)
printChangeVotesPosts("Posts with changed votes [post ID - post title - change in votes]:", postWithChangedVotes)

