from pathlib import Path
import os


class Scan:
    def __init__(self, root):
        self.root = Path(root)
        self.records = []

        # hardcoded ignore for now
        self.ignore_dirs = {
            ".git",
            "__pycache__",
            "node_modules"
        }

    def run(self):
        """
        Entry Point.
        Returns a list of file records
        """
        self._validate_root()
        self._walk()
        return self.records

    def _validate_root(self):
        """
        Ensure root exists and is a directory
        """
        if not self.root.exists():
            raise FileNotFoundError(f"Path does not exists: {self.root}")

        if not self.root.is_dir():
            raise NotADirectoryError(f"Not a directory: {self.root}")

    def _walk(self):
        """
        Walk directory tree and collect file records
        """
        for current_dir, dirnames, filenames in os.walk(self.root):
            # modufy dirnames in-place to skip ignored directions
            dirnames[:] = [
                d for d in dirnames
                if not self._should_ignore_dir(d)
            ]

            for filename in filenames:
                filepath = Path(current_dir)/filename

                try:
                    record = self._build_record(filepath)
                except (OSError, PermissionError):
                    # skil files we can't access 
                    continue

                self.records.append(record)

    def _should_ignore_dir(self, dirname):
        """
        Decide whether to skip a directory
        """
        return dirname in self.ignore_dirs

    def _build_record(self, filepath):
        """
        Extract metadata for a single file
        """
        stat = filepath.stat()

        return {
            "name": filepath.name,
            "path": str(filepath.resolve()),
            "ext": filepath.suffix.lstrip("."),
            "size": stat.st_size,
            "mtime": stat.st_mtime,
        }
