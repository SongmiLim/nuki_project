

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

class AuthFileIOError(NukiException):
    """
    로그인과 관련한 파일 생성 및 입출력에 실패한 경우
    """
    pass
class DictTypeError(NukiException):
    """
    입력으로 들어온 dict의 type이 부적절한 경우
    """
    pass
class WorkingFileExistsError(NukiException):
    """
    생성하고자 하는 working file 경로에 파일이 이미 존재하는 경우
    """
    pass