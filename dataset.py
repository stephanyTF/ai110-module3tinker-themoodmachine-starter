"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much", # positive
    "Today was a terrible day", # negative
    "Feeling tired but kind of hopeful", # mixed
    "This is fine", # neutral
    "So excited for the weekend", # positive
    "I am not happy about this", # negative
    #personally added 10 new posts
    "thats so funny lol", #positive
    "It's actually a good thing I ran into traffic because I got to listen to more of my podcast", #postive
    "hah yea, i bet he has a greeeeaaat personality", #sarcastic negative
    "bruh 💀", #negative
    "i'm ok with it", #neutral
    "don't worry about it lol", #neutral
    "right now im not sure but I'll let you know later", #neutral
    "hmmmm 🙂", #mixed
    "hey i'd be happy to drive over to see you but i have to work late tonight", #mixed
    "i'm not sure how my future will look like but I hope I'll figure it out later" #mixed



]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
    "positive",  # "thats so funny lol"
    "positive",  # "It's actually a good thing I ran into traffic because I got to listen to more of my podcast"
    "negative",  # "hah yea, i bet he has a greeeeaaat personality"
    "neutral",   # "i'm ok with it"
    "neutral",   # "right now im not sure but I'll let you know later"
    "mixed",     # "hey i'd be happy to drive over to see you but i have to work late tonight"
    "mixed",     # "i'm not sure how my future will look like but I hope I'll figure it out later"
    "negative",  # "bruh 💀"
    "mixed",     # "hmmmm 🙂"
    "neutral",   # "don't worry about it lol"

]

# TODO: Add 5-10 more posts and labels. - done
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#print(len(SAMPLE_POSTS) == len(TRUE_LABELS))
