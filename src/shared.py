#!/usr/bin/env python3

from os.path import exists
from sys import argv
import traceback
from platform import system

COLUMN_1_WIDTH = 30
COLUMN_SEPARATOR = ': '
HEADING_WIDTH = 60
INDENT = '    '
NEWLINE = '\n'


# Colors ───────────────────────────────────────────────────────────────────── #

# Special Colors ───────────────────── #

DEFAULT_COLOR = '\x1B[0m'
DEFAULT_BACKGROUND = '\x1B[49m'
RESET_COLOR = '\x1B[0m'
RESET = RESET_COLOR

# Foreground ───────────────────────── #

BLACK = '\x1B[30m'
DARK_GRAY = '\x1B[90m'
LIGHT_GRAY = '\x1B[37m'
WHITE = '\x1B[97m'
BLUE = '\x1B[34m'
CYAN = '\x1B[36m'
GREEN = '\x1B[32m'
PURPLE = '\x1B[35m'
MAGENTA = '\x1B[35m'
RED = '\x1B[31m'
YELLOW = '\x1B[33m'
LIGHT_BLUE = '\x1B[94m'
LIGHT_CYAN = '\x1B[96m'
LIGHT_GREEN = '\x1B[92m'
LIGHT_PURPLE = '\x1B[95m'
LIGHT_MAGENTA = '\x1B[95m'
LIGHT_RED = '\x1B[91m'
LIGHT_YELLOW = '\x1B[93m'

# Background ───────────────────────── #

ON_BLACK = '\x1B[40m'
ON_DARK_GRAY = '\x1B[100m'
ON_LIGHT_GRAY = '\x1B[47m'
ON_WHITE = '\x1B[107m'
ON_BLUE = '\x1B[44m'
ON_CYAN = '\x1B[46m'
ON_GREEN = '\x1B[42m'
ON_PURPLE = '\x1B[45m'
ON_MAGENTA = '\x1B[45m'
ON_RED = '\x1B[41m'
ON_YELLOW = '\x1B[43m'
ON_LIGHT_BLUE = '\x1B[104m'
ON_LIGHT_CYAN = '\x1B[106m'
ON_LIGHT_GREEN = '\x1B[102m'
ON_LIGHT_YELLOW = '\x1B[103m'
ON_LIGHT_PURPLE = '\x1B[105m'
ON_LIGHT_MAGENTA = '\x1B[105m'
ON_LIGHT_RED = '\x1B[101m'
ON_LIGHT_YELLOW = '\x1B[103m'

# Styles ───────────────────────────── #

BOLD = '\x1B[1m'
BLINK = '\x1B[5m'
DIMMED = '\x1B[2m'
ITALIC = '\x1B[3m'
REVERSED = '\x1B[7m'
STRIKETHROUGH = '\x1B[9m'
UNDERLINE = '\x1B[4m'

# User Defined ─────────────────────── #

VAR = f"{ITALIC}{LIGHT_MAGENTA}"
VARIABLE = VAR


# Arguments ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ #

def argument(number, default=''):
    ''' Returns the command line parameter
            or the default if it does not exist.

            Index is 0 based.
    '''

    if len(argv) > number:
        return argv[number + 1]
    return default


def arguments():
    return argv[1:]


def argument_count():
    return len(argv) - 1


def no_arguments():
    ''' Returns True if there are
            no command line parameters
    '''
    return len(argv) <= 1


def not_enough_arguments(expected):
    return len(argv) <= expected


def outside_argument_range(min, max):
    return argument_count() < min or argument_count() > max


# General Utils ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ #

class First:

    def __init__(self):

        self._first = True

    def is_first(self):

        if not self._first:
            return False

        self._first = False
        return True

    def not_first(self):

        return not self.is_first()


def either(value_1, value_2):
    if value_1 is None:
        return value_2
    return value_1


def iif(condition, true_value, false_value=None):
    if condition:
        return true_value
    return false_value


def iif_not(condition, true_value, false_value=None):
    if condition:
        return false_value
    return true_value


def is_blank(value):
    return not value or value.isspace()


def is_comment(value):
    return value.startswith('#') and value.startswith('//')


def is_empty(value):
    return not value


def is_mac():
    return system() == 'Darwin'


def is_windows():
    return system() == 'Windows'


def not_blank(value):
    return not is_blank(value)


def not_comment(value):
    return not is_comment(value)


def not_empty(value):
    return not is_empty(value)


# Files ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ #

def file_exists(file_name):
    return exists(file_name)


def read(file_name):
    with open(file_name, 'r') as file:
        return file.read()


def read_lines(file_name):
    with open(file_name, 'r') as file:
        return [line.rstrip('\n') for line in file]


def write(file_name, contents):
    with open(file_name, 'w') as file:
        file.write(contents)


def write_lines(file_name, lines):
    with open(file_name, 'w') as file:
        file.write('\n'.join(lines))


# Strings ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ #

def after(text, match):
    if match in text:
        return text.split(match)[1]
    return text


def after_last(text, match):
    if match in text:
        return text[text.rfind(match) + 1:]
    return text


def before(text, match):
    if match in text:
        return text.split(match)[0]
    return text


def ignore_blanks(lines):
    return [line for line in lines if not_blank(line)]


def ignore_comments(lines):
    return [line for line in lines if not_comment(line) and not_blank(line)]


def pad(value, length):
    return value.ljust(length)


def to_lines(value):
    return value.split('\n')


# Print ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ #

def dot_dot_dot(text, length):

    if text and len(text) > length:
        return text[:length + 1] + "..."

    return text


def heading(heading):
    print_heading(heading)


def indent(value, value_2, value_3=None):
    print_indent(value, value_2, value_3)


def nl():
    """Prints a new line."""
    print("")


def nl2():
    """Prints 2 new lines."""
    print("")
    print("")


def print_(value, value_2=None):

    if value == None:
        print_("[None]", value_2)
        return

    if value_2 == None:
        print(value)
        return

    try:
        print(value.ljust(COLUMN_1_WIDTH) + COLUMN_SEPARATOR + value_2)
    except TypeError:
        try:
            print(value.ljust(COLUMN_1_WIDTH) +
                  COLUMN_SEPARATOR + str(value_2))
        except TypeError:
            print(value.ljust(COLUMN_1_WIDTH) +
                  COLUMN_SEPARATOR + "[Non Printable Type]")


def print_2(value, value_2=None):
    print_(value, value_2)


def print_bin(value, value_2):
    if value_2 >= 0:
        print_(value, f"{bin(value_2)[2:]:>8}    {value_2:>3}")
    else:
        print_(value, f"{'-' + bin(value_2)[3:]:>8}    {value_2:>3}")


def print_double(value, value_2=None):
    print_(value, value_2)
    nl()


def print_error(value, value_2=None, show_trace=False):

    if value_2:
        print_("Error", value)
        error = value_2
    else:
        print_("Error")
        error = value

    nl()
    print_indent(1, "Type", type(error))

    if error.args and error.args[0]:
        print_indent(1, "Message", error.args[0])
    nl()

    if show_trace:
        print(traceback.format_exc())
        nl()


def print_head(heading):
    print_heading(heading)


def print_heading(heading):

    print(LIGHT_GREEN + ("──  " + heading +
          "  ").ljust(HEADING_WIDTH, "─") + RESET_COLOR)
    nl()


def print_indent(value, value_2, value_3=None):

    indent = INDENT * value

    if type(value_3) is str and "\n" in value_3:
        value_3 = "\n\n" + indent + ("\n" + indent).join(value_3.splitlines())

    print_(indent + value_2, value_3)


def print_is_empty(value):

    print_("value", str(value))
    nl()

    # Test Is List

    if type(value) is list:
        print("  is list:    List")
    else:
        print("  is list:    Not List")

    if type(value) == list:
        print("  = list:     List")
    else:
        print("  = list:     Not List")

    nl()

    if value:
        print("  value:      Not Empty")
    else:
        print("  value:      Empty")

    if not value:
        print("  not value:  Empty")
    else:
        print("  not value:  Not Empty")

    nl()

    if value is None:
        print("  is None:    None")
    else:
        print("  is None:    Not None")

    if isinstance(value, list):
        if len(value):
            print("  len:        Not Empty")
        else:
            print("  len:        Empty")

    nl()


def print_lines(value, value_2=None):
    if value_2:
        print(value + COLUMN_SEPARATOR)
        nl()
        for item in value_2:
            print_indent(1, item)
    else:
        for item in value:
            print(item)
    nl()


def print_list(value, value_2=None):
    print_lines(value, value_2)


def print_middle(value, value_2=None):
    nl()
    print_(value, value_2)
    nl()


def print_short_heading(heading):
    nl()
    print(("── " + heading + " ──"))
    nl()


def print_title(title):

    nl()
    print(GREEN + '┌─' + '─' * (HEADING_WIDTH - 4) + '─┐')
    print(('│ ' + title).ljust(HEADING_WIDTH - 2) + ' │')
    print('└─' + '─' * (HEADING_WIDTH - 4) + '─┘' + RESET_COLOR)
    nl()


def print_type(value, value_2=None):
    if value_2:
        print_(value, type(value_2))
        print_(" ", value_2)
    else:
        print(type(value))
        print(value)


def print_value(value, value_2=None):
    if value_2:
        print_(value, repr(value_2))
    else:
        print(repr(value))


def print2(value, value_2=None):
    print_(value, value_2)


def short_heading(heading):
    print_short_heading(heading)


def title(title):
    print_title(title)