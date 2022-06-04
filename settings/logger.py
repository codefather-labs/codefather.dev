import logging
from typing import Any, AnyStr

system_handler = logging.Handler(level=logging.INFO)


class SystemHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        print(self.formatter.format(record))


class SystemFormatter(logging.Formatter):
    default_time_format = "%d/%b/%Y %H:%M:%S"
    default_msec_format = None


system_formatter = SystemFormatter(
    "[%(levelname)s][%(name)s][%(asctime)s]: %(message)s"
)

system_handler = SystemHandler(level=logging.INFO)
system_handler.setFormatter(system_formatter)

system = logging.Logger(name="SYSTEM", level=logging.INFO)
system.addHandler(system_handler)


def system_message(msg: Any, log_level: int = None):
    if not isinstance(msg, str):
        msg = str(msg)

    log_level = log_level if log_level else logging.INFO

    system.log(msg=msg, level=log_level)
