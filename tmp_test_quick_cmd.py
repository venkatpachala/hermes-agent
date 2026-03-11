from gateway.run import GatewayRunner
from gateway.config import GatewayConfig
from unittest.mock import MagicMock

runner = GatewayRunner(config=GatewayConfig())
runner._is_user_authorized = lambda src: True

# Minimal event mock for quick command branch
event = MagicMock()
event.get_command.return_value = "testcmd"
event.get_command_args.return_value = ""
event.text = "/testcmd"
event.source = MagicMock()
event.source.user_id = "u"
event.source.platform = MagicMock()
event.source.platform.value = "telegram"
event.source.chat_id = "1"
event.source.chat_type = "dm"

try:
    result = runner._handle_message(event)
    print("ok", result)
except Exception as e:
    print("error", type(e), e)
