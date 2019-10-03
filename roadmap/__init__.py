import roadmap
from roadmap.resources import app_users, feedback, ideas, items, roadmaps, stories, subscribers

credentials = (None, None)


def init(email, token):
    roadmap.credentials = (email, token)


api_base = "https://app.roadmap.space"

app_users = app_users.AppUsers()
feedback = feedback.Feedback()
ideas = ideas.Ideas()
items = items.Items()
roadmaps = roadmaps.Roadmap()
stories = stories.Stories()
subscribers = subscribers.Subscribers()
