import os

_config = None


def get_config():
    """ Singleton construct for config object """
    global _config
    if _config is None:
        config = Config()
    return config


class Config:
    """ Secrets and environment variables """

    BLINK_USERNAME = os.environ.get("BLINK_USERNAME", None)
    BLINK_PASSWORD = os.environ.get("BLINK_PASSWORD", None)

    def __getitem__(self, item):
        return getattr(self, item)
