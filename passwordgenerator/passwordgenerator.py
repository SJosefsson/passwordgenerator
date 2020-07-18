import random
import string


VALID_CHARS = f'._-{string.digits}{string.ascii_letters}'


def generate_password(valid_chars: str=VALID_CHARS, size: int=20) -> str:
    """Generates random password.

    Accepts:
        valid_chars (str): Characters acceptable for password construction.
        size (int): Count of characters for assembled password.
    Returns:
        str: Created password of length size from characters valid_chars.
    """
    return ''.join(random.choice(valid_chars) for _ in range(size))
