"""Given a reddit submission id, shows the top 5 comments from the 200 newest comments. 
Pressing return shows a new set of comments, without repeating any comments shown before.
"""
import praw, time, os, sys

sub_id = sys.argv[1]

user_agent = ("Game comment scraper 1.0 by /u/NosajReddit" "https://github.com/NosajGithub/game_comment_scraper")
r = praw.Reddit(user_agent=user_agent)

clear = lambda: os.system('clear')
cached_comments = []

def output_comments():

    comments = []
    
    submission = r.get_submission(submission_id=sub_id, comment_sort='new')
    flat_comments = praw.helpers.flatten_tree(submission.comments)
    
    for comment in flat_comments:
        if (not isinstance(comment,praw.objects.MoreComments)):
            if comment.id not in cached_comments:
                comments.append((int(comment.score), comment.body.encode('utf-8'), comment.id, time.time() - comment.created_utc, 
                                 comment.author_flair_text))
        
    comments = sorted(comments, reverse = True)
    for score, text, comment_id, sec_ago, flair in comments[:5]:
        cached_comments.append(comment_id)
        print "Score: " + str(score) + ", Seconds Ago: " + str(int(sec_ago)) + ", Flair: " + str(flair)
        print text + "\n"

input_text = ""    
while input_text != "Exit":
    clear()
    output_comments()
    input_text = raw_input("Press \"Enter\" to get more comments, \"Exit\" to exit...")    