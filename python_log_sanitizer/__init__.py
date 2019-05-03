import re
from logging import Filter


class SanitizerFilter(Filter):
    # We should not filter those names because they belong
    # to logging.LogRecord instances
    RESERVED_ATTRIBUTES = [
        "args",
        "created",
        "exc_info",
        "exc_text",
        "filename",
        "funcName",
        "getMessage",
        "levelname",
        "levelno",
        "lineno",
        "module",
        "msecs",
        "msg",
        "name",
        "pathname",
        "process",
        "processName",
        "relativeCreated",
        "stack_info",
        "thread",
        "threadName",
    ]

    def __init__(self, patterns, placeholder):
        self.patterns = patterns
        self.placeholder = placeholder

        super(SanitizerFilter, self).__init__()

    def filter(self, record):
        for field, value in record.__dict__.items():
            if field not in self.RESERVED_ATTRIBUTES:
                setattr(record, field, self._sanitize(field, value))
        return True

    def _sanitize(self, field, data):
        if isinstance(data, dict):
            if self.matches_any_pattern(field):
                return self._sanitize_value(field, data)
            return {key: self._sanitize(key, value) for key, value in data.items()}
        if isinstance(data, list):
            return [self._sanitize(field, item) for item in data]
        return self._sanitize_value(field, data)

    def _sanitize_value(self, field, value):
        return self.placeholder if self.matches_any_pattern(field) else value

    def matches_any_pattern(self, key):
        return any(re.compile(pattern).search(key) for pattern in self.patterns)
