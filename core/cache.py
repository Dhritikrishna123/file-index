import json
import time
from pathlib import Path


class IndexCache:
    def __init__(self):
        self.cache_dir = Path.home()/"/fileindex"
        self.cache_file = self.cache_dir/"index.json"

    def save(self, root, records):
        """
        Save scan results to disk
        """
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        data = {
            "root": str(Path(root).resolve()),
            "scanned_at": time.time()
            "file_count": len(records)
            "records": records,
        }

        with self.cache_file.open("w", encoding="utf-8") as f:
            json.dump(data, f)

        def load(self):
            """
            Load cached indexed file
            """
            data = self.load()
            if not data:
                return False

            return data["root"] == str(Path(root).resolve())
