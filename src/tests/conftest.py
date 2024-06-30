from api.config import AppConfig
from api.container import container

test_config = AppConfig(app_title="Test App")
container.config.override(test_config)
