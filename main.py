"""
name: Madlib
author: irBabak
date_created: 2025/04/03
"""


# Validate user's inputs:
def get_valid_input(prompt, *validators):
    while True:
        user_input = input(prompt)

        valid, error_message = non_empty(user_input)
        if not valid:
            print(error_message)
            continue

        errors = []
        for validator in validators:
            valid, error_message = validator(user_input)

            if not valid:
                errors.append(error_message)

        if errors:
            print("\n".join(errors))
        else:
            return user_input


def non_empty(text: str):
    if text:
        return True, ""
    else:
        return False, "Invalid input! Input cannot be empty."


def is_alpha(text: str):
    if text.replace(" ", "").isalpha():
        return True, ""
    else:
        return False, "Invalid input! Input can only contain alphabetic and spaces."


# Gather blanks from user:
adj = get_valid_input("Enter an adjective: ", is_alpha)
noun = get_valid_input("Enter a noun: ", is_alpha)
verb = get_valid_input("Enter a verb: ", is_alpha)
place = get_valid_input("Enter a place: ", is_alpha)
plural_noun = get_valid_input("Enter a plural noun: ", is_alpha)
creature = get_valid_input("Enter a plural creature: ", is_alpha)
verb_past = get_valid_input("Enter a past tense verb: ", is_alpha)
emotion = get_valid_input("Enter an emotion: ", is_alpha)

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
