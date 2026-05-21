def make_new_guess(words, previous_guesses, previous_feedback):
    guessed = set(previous_guesses)

    for word in words:
        if word not in guessed:
            return word

    return words[0] if words else ""
