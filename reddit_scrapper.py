import praw
import smtplib
import requests

def main():
    user_agent = "Top Posts on Sysadmin per Day 1.0 by /u/reddit_user_name"
    r = praw.Reddit(user_agent)
    subreddits = r.get_subreddit("sysadmin").get_top_from_day(limit=10)
    top_submissions = get_subreddit(subreddits)
    message = makeMessage(top_submissions)
    mailme = send_email(message)

def get_subreddit(subreddits):  # Takes top 10 posts and adds it to a dictionary with title being key and url being value
    dict_of_submissions = dict()
    for submission in subreddits:
        title = submission.title
        url = submission.short_link
        dict_of_submissions[title] = url
    return dict_of_submissions

def makeMessage(dict_of_submissions):    # Creates message in email
    d = dict_of_submissions
    posts = list()
    for key, value in d.iteritems():
        posts.append("{0}\n{1}".format(key,value))
    return posts

def send_email(posts):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("email", "password")
    msg = "\n\n".join(posts)
    server.sendmail("from_address", "to_addr", msg)
    server.quit()
# don't need to return anything here bc nothing to return

main()
