import random
import string


VALID_CHARS = f'._-{string.digits}{string.ascii_letters}'


def generate_password(valid_chars: str=VALID_CHARS, size: int=20) -> str:
    """Generates random password.

    Accepts:
        valid_chars (str) [VALID_CHARS]: Acceptable characters for password.
        size (int) [20]: Count of characters for password.
    Returns:
        str: Created password.
    """
    return ''.join(random.choice(valid_chars) for _ in range(size))
