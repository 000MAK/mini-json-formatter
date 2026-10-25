# Mini JSON Formatter

A small Python command-line utility that validates JSON syntax and writes a consistently indented, human-readable JSON file.

**Independent demonstration project** · Python 3.10+ · Standard library only · MIT license

## Features

- Parses JSON input using Python's standard `json` library.
- Formats valid JSON with two-space indentation.
- Preserves non-ASCII characters in the output.
- Reads UTF-8 text with an optional UTF-8 BOM.
- Rejects identical input and output paths.
- Refuses to overwrite an existing destination.

## Quick start

```bash
python main.py --help
python main.py messy.json formatted.json
```

Use a new destination filename. The input file remains unchanged.

## Tests

```bash
python -m unittest discover -s tests -v
```

## Scope and limitations

This tool checks JSON syntax and formatting; it does not validate a domain-specific schema, verify business rules, or repair malformed input automatically. Review formatted output before integrating it into another system.

## Related Quantix projects

- [Mini JSON–CSV Converter](https://github.com/000MAK/mini-json-csv-converter)
- [Mini CSV Cleaner](https://github.com/000MAK/mini-csv-cleaner)
- [Quantix — 100 Mini Python Projects](https://github.com/000MAK/quantix-100-new-mini-projects)

## Safety

Use synthetic input in public examples and keep private records out of public repositories.

## License

MIT. See [LICENSE](LICENSE).
