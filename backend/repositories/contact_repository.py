import csv
from pathlib import Path


class ContactCSVRepository:
    def __init__(self, csv_path, headers):
        self.csv_path = Path(csv_path)
        self.headers = list(headers)
        self._ensure_storage()

    def _ensure_storage(self):
        self.csv_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.csv_path.exists():
            with self.csv_path.open('w', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=self.headers)
                writer.writeheader()

    def save(self, submission):
        with self.csv_path.open('a', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.headers)
            writer.writerow(submission.to_row())

    def list_all(self):
        self._ensure_storage()
        with self.csv_path.open('r', newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            return list(reader)
