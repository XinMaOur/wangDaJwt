class InvalidTokenError(Exception):
    pass


class InvalidPaloadError(InvalidTokenError):
    pass


class TimeoutTokenError(InvalidPaloadError):
    pass


class LosedError(InvalidTokenError):
    pass


class FormatError(InvalidTokenError):
    pass


class ExpLosedError(InvalidPaloadError):
    pass


class ExpTypeError(InvalidPaloadError):
    pass

