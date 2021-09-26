# Flask-GetEnvValue

![GitHub Actions Testing CI status](https://github.com/yukkeorg/Flask_GetEnvValue/actions/workflows/tests.yml/badge.svg)


Loading a values from environment variable and set to `app.config`.


## Example

```sh
export APP_TWITTER_CLIENT_ID="id"
export APP_TWITTER_CLIENT_SECRET="xxxxxxxxxxxxxxx"
```

``` python
from flask import Flask
from flask_getenvvalue import GetEnvValue

app = Flask(__name__)
GetEnvValue(app, ["APP_TWITTER_CLIENT_ID",
                  "APP_TWITTER_CLIENT_SECRET"])

print(app.config["APP_TWITTER_CLIENT_ID"])
# => "id"
print(app.config["APP_TWITTER_CLIENT_SECRET"])
# => "xxxxxxxxxxxxxxx"
```

## License

MIT
