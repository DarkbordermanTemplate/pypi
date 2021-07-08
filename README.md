# Pypi
Python module packaging template, with an example Pypi server.

Each moudle are separated into folders (Ex: `db_model/`) for isolation.

![Integration](https://github.com/DarkbordermanTemplate/pypi/workflows/Integration/badge.svg)

## Development

### Prerequisitive

| Name | Version |
| --- | --- |
| Python | 3.8 |
| pipenv(Python module) | 2018.11.26 or up |

### Environment setup

0. Initialize Python environment
```
make init
```

1. Enter the environment and start developing
```
pipenv shell
```

2. Start related components
```
make service_up
```

3. Create python package
```
make package
```

4. Publish to example Pypi server
```
make upload
```

5. (Optional)Stop related components
```
make service_down
```

### Linting

This project uses `pylint` and `flake8` for linting
```
make lint
```

## Contribution

* Darkborderman/Divik(reastw1234@gmail.com)
