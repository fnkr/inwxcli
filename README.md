# [inwxcli](https://github.com/fnkr/inwxcli)

Command line interface for [inwx.com](https://www.inwx.com).

## Examples

### domain.check

```
$ inwxcli --username foo --password bar domain.check domain=example.com
{'msg': 'Command completed successfully', 'code': 1000, 'svTRID': '20180107-91698974', 'resData': {'domain': [{'avail': 0, 'status': 'used', 'domain': 'example.com', 'premium': '', 'checktime': 353.0}]}, 'runtime': 2.334}
```

```
$ inwxcli --username foo --password bar --format '{resData[domain][0][status]}' domain.check domain=example.com
used
```

## API reference

A complete list of API methods is available at
https://www.inwx.de/en/help/apidoc/f/index.html (DomRobot XML-RPC API Documentation).
