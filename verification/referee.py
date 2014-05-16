
from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee
from checkio.referees import cover_codes
from checkio.referees import checkers

from tests import TESTS

cover = """def cover(f, data):
    return f(tuple(data[0]), data[1], data[2])
"""

api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        cover_code={
            'python-27': cover,  # or None
            'python-3': cover
        },
        function_name="check_connection"
        # checker=None,  # checkers.float.comparison(2)
        # add_allowed_modules=[],
        # add_close_builtins=[],
        # remove_allowed_modules=[]
    ).on_ready)
