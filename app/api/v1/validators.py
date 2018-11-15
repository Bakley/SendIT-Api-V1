"""Validation file."""


def check_for_blanks(variable_object):
    """Check for blanks."""
    if variable_object.strip() == '':
        return 'All fields are required'
    return None


def check_for_intergers(new_object):
    """Check if value is a number."""
    value = new_object == int(new_object)
    if not value:
        return 'The value need to be an interger'
    return None
