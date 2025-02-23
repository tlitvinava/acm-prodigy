from main.utils import Configuration


def get_available_reg():
    return (
        True
        if Configuration('registration.team.available').lower() == 'true'
        else False
    )


def get_credentials_show():
    return (
        True
        if Configuration('configuration.olympiad.credentials').lower() == 'true'
        else False
    )


def get_olympiad_type():
    return Configuration('configuration.olymp.type')


def get_test_prefix():
    return Configuration('configuration.team.prefix')

