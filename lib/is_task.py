def is_task(note):
    if note == "" or type(note) != str:
        raise Exception("I need a string to check!")
    return "#TODO" in note