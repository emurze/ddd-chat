from config.config import AppConfig
from config.container import container

test_config = AppConfig(app_title="Test App")
container.config.override(test_config)
