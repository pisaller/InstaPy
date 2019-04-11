""" Quickstart script for InstaPy usage """

# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace


# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

# get an InstaPy session!
session = InstaPy(username="superfkndopetho", 
        password="$t0rmd4t4!")

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_dont_include(["friend1", "friend2", "friend3"])
    session.set_do_follow(enabled=True, percentage=10, times=2)

    # activity
    session.like_by_tags(["natgeo"], amount=10)
    session.like_by_tags(["natgeo"], amount=10)
