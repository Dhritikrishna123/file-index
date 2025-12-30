# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-12-30

### Added
- Initial release of fileindex
- Directory scanning with recursive file indexing
- Smart JSON-based caching system (~/.fileindex/index.json)
- Advanced search with multiple filters:
  - Search by filename (case-insensitive substring matching)
  - Filter by file extension
  - Filter by file size (min/max range)
  - Filter by path (case-insensitive substring matching)
- Duplicate file detection based on SHA256 content hashing
- Chainable search filters for complex queries
- Incremental scanning with hash reuse optimization
- Cache status monitoring
- Beautiful CLI with color-coded output
- Cross-platform support (Windows, macOS, Linux)
- Entry point for system-wide command execution
- Comprehensive test suite with 61+ unit tests
- Full documentation with examples

### Features
- Lightning-fast file indexing (~1000-5000 files/second)
- Instant search (<100ms for cached index)
- Incremental scanning optimization (50-90% faster rescans)
- Automatic directory ignoring (.git, __pycache__, node_modules)
- Zero external dependencies
- Python 3.8+ support
- PyPI-ready package distribution

### Documentation
- Comprehensive README.md
- Inline code documentation

## Future Releases

### [0.2.0] - Planned
- Config file support (.fileindexrc)
- Custom ignore patterns
- Regex-based search support
- Watch mode for real-time indexing

### [0.3.0] - Planned
- SQLite database backend for large indices
- Export results to CSV/JSON
- Parallel directory scanning
- Python library API (programmatic usage)

### [0.4.0] - Planned
- Fuzzy matching support
- Case-sensitive search options
- Desktop GUI application
- Plugin system for custom search providers

---

For more details, visit the [GitHub repository](https://github.com/Dhritikrishna123/file-index).
