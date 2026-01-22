# OpenResponses Types

[![PyPI version](https://img.shields.io/pypi/v/openresponses-types)](https://pypi.org/project/openresponses-types/)
[![Python versions](https://img.shields.io/pypi/pyversions/openresponses-types)](https://pypi.org/project/openresponses-types/)
[![License](https://img.shields.io/pypi/l/openresponses-types)](https://github.com/mozilla-ai/openresponses-python/blob/main/LICENSE)

Python SDK providing Pydantic models for the [OpenResponses](https://github.com/openresponses/openresponses) API specification.

## Installation

```bash
pip install openresponses-types
```

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/mozilla-ai/openresponses-python.git
cd openresponses-python

# Create virtual environment and install dependencies
uv venv && source .venv/bin/activate
uv sync --group dev
```

### Generate Types

The types are generated from the OpenResponses OpenAPI specification:

```bash
# Generate types (fetches spec if changed)
uv run python scripts/generate_types.py

# Force regeneration
uv run python scripts/generate_types.py --force

# Check if spec has changed
uv run python scripts/generate_types.py --check

# Show current spec hash
uv run python scripts/generate_types.py --version
```

## Versioning

This package follows [Semantic Versioning](https://semver.org/):

- **Major**: Breaking changes to helper types/API
- **Minor**: New types from spec updates, new helpers
- **Patch**: Bug fixes, documentation updates

The package includes a `__spec_hash__` attribute to track which OpenAPI spec version was used to generate the types.

## License

Apache 2.0 - see [LICENSE](LICENSE) for details.

## Links

- [OpenResponses Specification](https://github.com/openresponses/openresponses)
- [PyPI Package](https://pypi.org/project/openresponses-types/)
- [Issue Tracker](https://github.com/mozilla-ai/openresponses-python/issues)
