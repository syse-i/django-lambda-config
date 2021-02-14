from .mixins import DisableSecurityMixin
from .production import Settings as ProductionSettings


class Settings(DisableSecurityMixin, ProductionSettings):
    DEBUG = True
