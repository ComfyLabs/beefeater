import base64


def decode_credentials(value):
    """
    Decodes the base64 encoded value of username:password combination

    Args:
        value (str): base64 encoded string of username:password

    Returns:
        username, password (tuple of str)
    """
    decoded = base64.b64decode(value).split(b':')

    return map(
        lambda x: x.decode('utf-8'), decoded
    )
