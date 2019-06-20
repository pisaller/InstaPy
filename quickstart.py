""" Quickstart script for InstaPy usage """

# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace

# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

comments = ['Amazing shot! @{}',
            'Awesome shot! @{}',
            'Nice shot! @{}',
            'I love your profile! @{}',
            'Your feed is an inspiration :thumbsup:',
            'Just incredible :open_mouth:',
            'What camera did you use @{}?',
            'Love your posts @{}',
            'Looks awesome @{}',
            'Getting inspired by you @{}',
            ':raised_hands: Yes!',
            'I can feel your passion @{} :muscle:']

# get an InstaPy session!
session = InstaPy(username="ppisallerr", password="wpzyz63059432", headless_browser=True)

with smart_run(session):
    # activity

    session.set_smart_hashtags(
        tags=["shanghai", 'city', 'china', 'chongqing', 'sony', 'Shanghai', 'China', 'Chongqing', 'Sony', 'VT',
              'Virginia Tech', 'Virginia_Tech', 'virginia_tech', 'virginia tech', 'blacksburg', 'Blacksburg'])
    session.like_by_tags(
        ["shanghai", 'city', 'china', 'chongqing', 'sony', 'Shanghai', 'China', 'Chongqing', 'Sony', 'VT',
         'Virginia Tech', 'Virginia_Tech', 'virginia_tech', 'virginia tech', 'blacksburg', 'Blacksburg'],
        amount=10000)
    session.smart_location_hashtags()
    session.do_follow(enabled=True, percentage=25, times=10000)
    # Joining Engagement Pods
    session.set_do_comment(enabled=True, percentage=25)
    session.set_do_like(enabled=True, percentage=10000)
    session.set_comments(comments)
    session.join_pods()
