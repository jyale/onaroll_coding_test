# onaroll_coding_test
Coding Test for Onaroll - Reddit API fetching

## **Onaroll Backend Coding Test:**

## **Parameters**

**Time expectations:** 60 - 90 minutes

**Language:** Any suitable backend language (Python, Ruby, NodeJS, etc)

**Frameworks:** Any, though note that if a framework or package solves 90% of the problem, you should use any extra time to add tests, etc.

## **Challenge**

Build a command line tool that communicates with the public Reddit API, stores information about posts, and on subsequent executions can tell which posts are new, which posts have dropped off, and which had vote changes.

[https://www.reddit.com/r/popular.json](https://www.reddit.com/r/popular.json)

A little-known hack on Reddit is that there is a free & public read-only API simply by appending .json to most URLs to get the page contents in JSON format.

On each run of your program, you should fetch the top 75 posts from r/popular.

Your program should then print out:

1. Which posts (ID & Headline) are new from the last program execution,
2. Which posts are no longer within the top 75 posts, and
3. Which posts have had their vote counts increase or decrease, and by how much.

Your program should be written clearly. External libraries are allowed. While unit or integration tests are not required, you should model your code to make it easily testable in the future. Your program should be commented appropriately.

**Extensions:** Not all of these are required, but we have seen candidates do some of these to demonstrate skills that are above and beyond the scope of the challenge.

**Tests:** Write tests around

**Mock data:**  Provide mock data so your program can demonstrate usage even without internet connectivity.

**Docker:**  Containerize your app to make it easy to spin up and down.

## **Submission**

Submit your code by creating a private repo on Github and sharing it with:

1. [https://github.com/peterginsberg](https://github.com/peterginsberg), and
2. [https://github.com/pavelm](https://github.com/pavelm) 

Make sure to include instructions on how to run your program.
