import random
import string


def get_random_string(length):
    var = ''.join(
        [
            random.choice(string.ascii_letters + string.digits)
            for n in range(length)
        ]
    )
    return var


def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['pdf'])
    return '.' in filename\
        and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
