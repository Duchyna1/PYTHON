import praw

def getMemes(number, subreddit):
    r = praw.Reddit(user_agent='SlafBot', client_id='RPjI0JvXom0ApQ', client_secret='t_3sz4rFfZ0EjRY-xgaoQnDYosE')
    submissions = r.subreddit(subreddit).rising(limit=number)
    for submission in submissions:
        return submission.url + '\n**' + submission.author.name + '**\n*' + submission.title + '*\n```diff\n-   ' + str(submission.score) + ' upvotes\n```'
    
