"""
name: Madlib
author: irBabak
date_created: 2025/04/03
"""

# Gather blanks from user:
adj = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
place = input("Enter a place: ")
plural_noun = input("Enter a plural noun: ")
creature = input("Enter a creature: ")
verb_past = input("Enter a past tense verb: ")
emotion = input("Enter an emotion: ")

# Generate story with user's inputs"
story = f"""
Once upon a time in a {adj} kingdom, there lived a {noun} who loved to {verb}.
Every day, the {noun} journeyed to the {place} where it met countless {plural_noun}.
One remarkable day, a mysterious {creature} appeared, and soon the {noun} had {verb_past} with joy.
The entire kingdom overflowed with {emotion}, bringing magic to every corner.
"""

# Display the Madlib story:
print("=" * 50)
print(story)
