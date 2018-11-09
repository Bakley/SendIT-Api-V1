"""Validation file."""


def check_for_blanks(variable_object):
    """Checks for blanks."""
    if variable_object.strip() == '':
        return 'All fields are required'
    return None
