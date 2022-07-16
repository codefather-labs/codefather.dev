import importlib
import os
from enum import Enum

from settings.logger import system_message


# ENVIRONMENT
# ------------------------------------------------------------------------------

class Environment(Enum):
    LOCAL = "Local"
    PRODUCTION = 'Production'

    @staticmethod
    def choices():
        return [x for x in Environment._value2member_map_]


class EnvironmentSettingsModule(Enum):
    LOCAL = 'settings.environment.local'
    PRODUCTION = 'settings.environment.production'

    def __str__(self):
        return self.value


def get_settings_module():
    return importlib.import_module(os.environ.get("DJANGO_SETTINGS_MODULE"))


environment_value = str(os.environ.get("ENVIRONMENT", 'Local'))
try:
    environment: Enum = Environment(environment_value)
except ValueError:
    system_message(f"Invalid environment {environment_value}. "
                   f"Use {Environment.choices()} choices")
    exit(1)


def load_environment():
    match environment:
        case Environment.LOCAL:
            os.environ.setdefault(
                'DJANGO_SETTINGS_MODULE', str(EnvironmentSettingsModule.LOCAL)
            )

        case Environment.PRODUCTION:
            os.environ.setdefault(
                'DJANGO_SETTINGS_MODULE', str(EnvironmentSettingsModule.PRODUCTION)
            )
    # system_message(f"--- Using {environment_value} Environment ---")


load_environment()
