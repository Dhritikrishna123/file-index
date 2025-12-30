class Search:
    def __init__(self, records):
        """
        records: list of file record dics produced by scan
        """
        self.records = records

    def by_name(self, query):
        """
        Case insensitive substring matching on filename
        """
        query = query.lower()
        return[
            r for r in self.records
            if query in r["name"].lower()
        ]

    def by_extension(self, ext):
        """
        Exact extension match (without a dot)
        """
        ext = ext.lower().lstrip(".")
        return [
            r for r in self.records
            if r["ext"].lower() == ext
        ]

    def by_size(self, min_size=None, max_size=None):
        """
        filter by file size
        """
        results = self.records

        if min_size is not None:
            results = [r for r in results if r["size"] >= min_size]

        if max_size is not None:
            result = [r for r in result if r["size"] <= max_size]

        return results

    def by_path(self, substring):
        """
        Case-insensitive substring match on full path
        """
        substring = substring.lower()
        return [
            r for r in self.records
            if substring in r["path"].lower()
        ]
