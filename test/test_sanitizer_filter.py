import pytest

from python_log_sanitizer import SanitizerFilter


@pytest.fixture
def sanitizer_filter():
    return SanitizerFilter(patterns=["cpf_cnpj"], placeholder="[*]")


@pytest.fixture
def record(mocker):
    return mocker.Mock(
        asctime="2018-08-30 20:40:57,245",
        filename="_internal.py",
        funcName="_log",
        lineno="88",
        levelname="WARNING",
        getMessage=lambda: "farofa",
        cpf_cnpj="124603771",
        request={
            "cpf_cnpj": "124603771",
            "random": {"user_cpf_cnpj": "123456789", "other": "123"},
        },
        autospec=[
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
        ],
    )


def test_filter(sanitizer_filter, record):
    assert sanitizer_filter.filter(record) is True
    assert record.asctime == "2018-08-30 20:40:57,245"
    assert record.filename == "_internal.py"
    assert record.funcName == "_log"
    assert record.lineno == "88"
    assert record.levelname == "WARNING"
    assert record.getMessage() == "farofa"
    assert record.cpf_cnpj == "[*]"
    assert record.request == {
        "cpf_cnpj": "[*]",
        "random": {"user_cpf_cnpj": "[*]", "other": "123"},
    }


def test_root_filter(sanitizer_filter, record):
    record.request = {"cpf_cnpj": {"key": "batata"}}
    assert sanitizer_filter.filter(record) is True
    assert record.asctime == "2018-08-30 20:40:57,245"
    assert record.filename == "_internal.py"
    assert record.funcName == "_log"
    assert record.lineno == "88"
    assert record.levelname == "WARNING"
    assert record.getMessage() == "farofa"
    assert record.cpf_cnpj == "[*]"
    assert record.request == {"cpf_cnpj": "[*]"}
