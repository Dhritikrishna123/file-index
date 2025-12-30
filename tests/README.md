# Unit Tests for fileindex

This directory contains comprehensive unit tests for the fileindex project.

## Test Files

### `test_style.py`
Tests for the CLI styling module (`cli/style.py`):
- Style constant definitions
- Color and formatting options
- Style application and composition

### `test_scan.py`
Tests for the directory scanning module (`core/scan.py`):
- Directory traversal
- File metadata extraction
- Hash computation (SHA256)
- Incremental scanning with cache optimization
- Ignored directory handling (.git, __pycache__, node_modules)

### `test_search.py`
Tests for the search module (`core/search.py`):
- Search by filename (substring matching, case-insensitive)
- Search by file extension
- Search by file size (min/max range)
- Search by path (substring matching)
- Duplicate file detection (based on content hash)
- Filter chaining

### `test_cache.py`
Tests for the caching module (`core/cache.py`):
- Cache file creation and storage
- Loading cached data
- Cache validation
- Clearing cache
- Incremental scan record retrieval

### `test_integration.py`
Integration tests for the complete workflow:
- Scan → Search workflow
- Scan → Cache → Load → Search workflow
- Incremental scanning with cache
- Multiple filter combination
- Duplicate file detection
- File metadata accuracy

## Running the Tests

### Run all tests:
```bash
python -m pytest tests/
```

### Run specific test file:
```bash
python -m pytest tests/test_scan.py
```

### Run with verbose output:
```bash
python -m pytest tests/ -v
```

### Run with coverage:
```bash
python -m pytest tests/ --cov=core --cov=cli
```

### Run with unittest (alternative):
```bash
python -m unittest discover -s tests -p "test_*.py"
```

## Test Coverage

The test suite covers:
- ✅ Core scanning functionality (113+ assertions)
- ✅ Search and filtering operations (50+ assertions)
- ✅ Caching mechanisms (30+ assertions)
- ✅ CLI styling (15+ assertions)
- ✅ Integration workflows (25+ assertions)
- ✅ Edge cases and error handling

Total: 230+ test assertions across 5 test modules

## Test Dependencies

- `unittest` - Python standard library
- `tempfile` - For temporary directories and files
- `pathlib` - Path operations
- `unittest.mock` - Mocking for cache home directory

## Notes

- Tests use temporary directories to avoid affecting the actual filesystem
- Mocking is used to isolate cache tests from actual home directory
- File hashes use SHA256 for content comparison
- All tests are isolated and can run in any order
