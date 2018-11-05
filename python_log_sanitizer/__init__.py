import re
from logging import Filter


class SanitizerFilter(Filter):
    def __init__(self, patterns, placeholder):
        self.patterns = patterns
        self.placeholder = placeholder

    def filter(self, record):
        for field, value in record.__dict__.items():
            setattr(record, field, self._sanitize(field, value))
        return True

    def _sanitize(self, field, data):
        if isinstance(data, dict):
            return {
                key: self._sanitize(key, value)
                for key, value in data.items()
            }
        if isinstance(data, list):
            return [self._sanitize(field, item) for item in data]
        return self._sanitize_value(field, data)

    def _sanitize_value(self, field, value):
        return self.placeholder if self.matches_any_pattern(field) else value

    def matches_any_pattern(self, key):
        return any(
            re.compile(pattern).search(key) for pattern in self.patterns)
