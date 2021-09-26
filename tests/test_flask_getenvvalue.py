import os
from flask import Flask


from flask_getenvvalue import GetEnvValue


def test_getenvvalue_default():
    app = Flask(__name__)
    app.config["FLASK_GETENVVALUE_TEST"] = "123456"
    os.environ["FLASK_GETENVVALUE_TEST"] = "ABCDEF"
    GetEnvValue(app, envnames=["FLASK_GETENVVALUE_TEST",
                               "FLASK_GETENVVALUE_UNDEFINED"])

    assert app.config["FLASK_GETENVVALUE_TEST"] == "ABCDEF"
    assert "FLASK_GETENVVALUE_UNDEFINED" not in app.config


def test_getenvvalue_disable_ignore_undefined():
    app = Flask(__name__)
    app.config["FLASK_GETENVVALUE_TEST"] = "123456"

    os.environ["FLASK_GETENVVALUE_TEST"] = "ABCDEF"
    GetEnvValue(app,
                envnames=["FLASK_GETENVVALUE_TEST",
                          "FLASK_GETENVVALUE_UNDEFINED"],
                ignore_undefined=False)

    assert app.config["FLASK_GETENVVALUE_TEST"] == "ABCDEF"
    assert app.config["FLASK_GETENVVALUE_UNDEFINED"] is None


def test_getenvvalue_enable_protect_exists():
    app = Flask(__name__)
    app.config["FLASK_GETENVVALUE_TEST"] = "123456"

    os.environ["FLASK_GETENVVALUE_TEST"] = "ABCDEF"
    GetEnvValue(app,
                envnames=["FLASK_GETENVVALUE_TEST"],
                protect_exists=True)

    assert app.config["FLASK_GETENVVALUE_TEST"] == "123456"
