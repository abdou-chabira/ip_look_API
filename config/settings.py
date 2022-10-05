import os
class Settings:
    @classmethod
    def get_setting(cls, name, defaultValue):
        val = os.environ.get(name)
        if val is None:
            val = defaultValue
        return val

    @classmethod
    def web_api_url_prefix(cls):
        return cls.get_setting("web_api_url_prefix", "/api/v1")

    @classmethod
    def db_uri(cls):
        return cls.get_setting("db_uri","postgresql://postgres:postgress@127.0.0.1:15432/postgres")

    @classmethod
    def web_api_key(cls):
        return cls.get_setting("web_api_key", "07157ae0-d69e-4956-a29e-d721f48b1c3e")