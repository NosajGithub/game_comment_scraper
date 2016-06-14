game_comment_scraper
====================

Allows redditors to follow a thread for a game in real time. Perfect for NFL, MLB, NBA, and NHL games - or any thread with a lot of new comments flooding in, really.    

The script loads in the top 200 comments for the given submission sorted by new, and displays the top 5 with the highest scores.
Pressing 'Enter' loads and shows the comments again, excluding any comments that have been shown before.  

## Setup  
Requires Python 2, and PRAW v3. To install the latter with pip, enter on the command line:
```
sudo pip install --ignore-installed six 'praw==3.5.0'
```

## Usage   
```
game_comment_scraper.py [sub_id]  
```
sub_id = the id of the submission whose comments you want to follow  

## Example  
For the reddit thread at http://www.reddit.com/r/nfl/comments/2r95sg/game_thread_baltimore_ravens_106_at_pittsburgh/  
```
python game_comment_scraper.py 2r95sg
```

Video of it in use here:  
https://www.youtube.com/watch?v=4Q_zCWlof0Y  
