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
    credentials = list(
        map(
            lambda x: x.decode('utf-8'), decoded
        )
    )

    return {'username': credentials[0], 'password': credentials[1]}


def encode_credentials(value):
    """
    Encodes the base64 encoded value of username:password combination

    Args:
        value (str): base64 encoded string of username:password

    Returns:
        username, password (tuple of str)
    """
    # not sure what the best way to handle these bytearrays is exactly.
    return base64.b64encode(
        value.encode('utf-8')
    ).decode('utf-8')
