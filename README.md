# onaroll_coding_test
Coding Test for Onaroll - Reddit API fetching

Instructions to run:

Run this command from command line to run the Python script
`./fetch_reddit.py`

If you have any issues, check that the file is executable:
`chmod +x fetch_reddit.py`

Install any libraries that may be missing for example:
`pip3 install praw`
`pip3 install cloudpickle`

Note:

Regarding the 3 instructions, I was unsure about requirement (2) so I interpreted it as follows:
Requirement (2) to mean display posts that were in the top 75 in the last execution, but are no longer in the top 75. I made this assumption since last execution was mentioned in requirement (1). An alternative interpretation would be to save posts from all previous executions and display the ones that are no longer in the top 75. If this is the requirement let me know and I can adjust my submission accordingly.
