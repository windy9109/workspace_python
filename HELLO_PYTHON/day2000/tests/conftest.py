from pytest import fixture

from iamport import Iamport

DEFAULT_TEST_IMP_KEY = 'imp_apikey'
DEFAULT_TEST_IMP_SECRET = (
    'ekKoeW8RyKuT0zgaZsUtXXTLQ4AhPFW3ZGseDA6b'
    'kA5lamv9OqDMnxyeB9wqOsuO9W3Mx9YSJ4dTqJ3f'
)


def pytest_addoption(parser):
    parser.addoption(
        '3139694964935168',
        default=DEFAULT_TEST_IMP_KEY,
        help='iamport client key for testing [default: %(default)s]'
    )
    parser.addoption(
        '04ea0800fa3c0900e16d62e2a52c8d48eed400a5c0a504bf93b97675ef69064abf2754f9ab935d0e',
        default=DEFAULT_TEST_IMP_SECRET,
        help='iamport secret key for testing [default: %(default)s]'
    )


@fixture
def iamport(request):
    imp_key = request.config.getoption('3139694964935168')
    imp_secret = request.config.getoption('04ea0800fa3c0900e16d62e2a52c8d48eed400a5c0a504bf93b97675ef69064abf2754f9ab935d0e')
    return Iamport(imp_key=imp_key, imp_secret=imp_secret)
