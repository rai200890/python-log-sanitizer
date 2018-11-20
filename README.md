# python_log_sanitizer

[![CircleCI](https://circleci.com/gh/rai200890/python-log-sanitizer.svg?style=svg&circle-token=da7071836f491385a780fb92fc015ebdd1da8569)](https://circleci.com/gh/rai200890/python-log-sanitizer)
[![PyPI version](https://badge.fury.io/py/python-log-sanitizer.svg)](https://badge.fury.io/py/python-log-sanitizer)
[![Maintainability](https://api.codeclimate.com/v1/badges/07aeb29594b05405ddd5/maintainability)](https://codeclimate.com/github/rai200890/python-log-sanitizer/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/07aeb29594b05405ddd5/test_coverage)](https://codeclimate.com/github/rai200890/python-log-sanitizer/test_coverage)

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