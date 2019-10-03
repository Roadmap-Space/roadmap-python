# Roadmap for Python

Version: v1.0.0

## Summary

Official Python API client library for [Roadmap](https://roadmap.space)'s API.

## Installation

```shell
pip install roadmap-py
```

## Documentation

For a comprehensive list of examples, check out the [API documentation](http://api.roadmap.space).

Here are some examples:

### Get the ideas shown on the widget

```python
from roadmap-py import roadmap

client = roadmap.new("email", "token")
try:
  ideas = client.roadmaps.get_widget_ideas("[roadmap id here]")
except:
  print("An error occured.")
```
