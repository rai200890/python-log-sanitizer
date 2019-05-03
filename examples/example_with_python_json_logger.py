import logging

from logging import config


LOG_CONFIG = {
    "version": 1,
    "formatters": {
        "json": {
            "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
        }
    },
    "filters": {
        "sanitizer": {
            "()": "python_log_sanitizer.SanitizerFilter",
            "patterns": ["extra"],
            "placeholder": "*",
        }
    },
    "handlers": {"json": {"class": "logging.StreamHandler", "formatter": "json"}},
    "loggers": {
        "root": {"level": "INFO", "handlers": ["json"], "filters": ["sanitizer"]}
    },
}
config.dictConfig(LOG_CONFIG)  # load log config from dict

logger = logging.getLogger("root")  # get root logger instance

logger.info("farofa", extra={"extra": "farofa"})  # log message with extra arguments
