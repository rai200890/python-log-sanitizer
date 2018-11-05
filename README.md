    # python_log_sanitizer

<!-- [![CircleCI](https://circleci.com/gh/rai200890/python_google_cloud_logger.svg?style=svg&circle-token=cdb4c95268aa18f240f607082833c94a700f96e9)](https://circleci.com/gh/rai200890/python_google_cloud_logger) -->
[![PyPI version](https://badge.fury.io/py/python-log-sanitizer.svg)](https://badge.fury.io/py/python-log-sanitizer)
<!-- [![Maintainability](https://api.codeclimate.com/v1/badges/e988f26e1590a6591d96/maintainability)](https://codeclimate.com/github/rai200890/python_google_cloud_logger/maintainability) -->

Python log sanitizer

## Instalation

### Pipenv

```
    pipenv install python_log_sanitizer 
```

### Pip

```
    pip install python_log_sanitizer 
```

## Usage

To run this example please install [python-json-logger](https://github.com/madzak/python-json-logger):

```pip
pip install python-json-logger
```

```python
LOG_CONFIG = {
    "version": 1,
    "formatters": {
        "json": {
            "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
        }
    },
    "filters": {
        "sanitizer": {
            "()" : "python_log_sanitizer.SanitizerFilter",
            "patterns": ["extra"],
            "placeholder": "*"
        }
    },
    "handlers": {
        "json": {
            "class": "logging.StreamHandler",
            "formatter": "json"
        }
    },
    "loggers": {
        "root": {
            "level": "INFO",
            "handlers": ["json"],
            "filters": ["sanitizer"]
        }
    }
}
import logging

from logging import config

config.dictConfig(LOG_CONFIG) # load log config from dict

logger = logging.getLogger("root") # get root logger instance


logger.info("farofa", extra={"extra": "farofa"}) # log message with extra arguments  
```

Example output:

```json
{"asctime": "2018-11-04 23:01:55,804", "levelname": "INFO", "module": "<ipython-input-8-f8c68848bfbe>", "message": "farofa", "extra": "*"}
```