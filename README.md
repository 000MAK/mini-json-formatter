# Mini JSON Formatter

Validates and pretty-prints JSON. The input file is never overwritten.

## Requirements

- Python 3.10+
- Standard library only; no `pip install` step required.

## Run

```bash
python main.py --help
```

## Example

`python main.py messy.json formatted.json`

## Tests

```bash
python -m unittest discover -s tests -v
```

## Safety notes

Use copies of important files. Review output before using it in production. Do not add credentials, private data, or real customer files to Git.

## License

MIT. See [LICENSE](LICENSE).
