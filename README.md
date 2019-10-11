# Roadmap for Python

Version: v1.0.2

## Summary

Official Python API client library for [Roadmap](https://roadmap.space)'s API.

## Installation

```shell
pip install roadmap-py
```

## Documentation

For a comprehensive list of examples, check out the [API documentation](http://api.roadmap.space).

Here are some examples:

### Get the roadmap

```python
from roadmap-py import roadmap

roadmap.init("email", "token")

roadmap.roadmaps.get_roadmap(
  "[roadmap id here]",
  lambda err, result: print(err, result)
)
```
