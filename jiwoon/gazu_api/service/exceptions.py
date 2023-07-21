

class NukiException(Exception):
    """
    Nuki 예외사항.
    """
    pass


class UnconnectedHostError(NukiException):
    """
    host에 연결되어 있지 않은 상태에서 login을 시도한 경우
    """
    pass


class InvalidAuthError(NukiException):
    """
    유효하지 않은 host, id, pw 값으로 연결을 시도한 경우.
    """
    pass