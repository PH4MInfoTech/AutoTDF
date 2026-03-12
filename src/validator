import re
import hashlib
import os

class RecordValidator:
    def __init__(self):
        # Matches formats like 12-34-56, 123456, or 12 34 56
        self.tdf_pattern = re.compile(r'^(\d{2})[- ]?(\d{2})[- ]?(\d{2})$')

    def is_valid_id(self, file_id):
        """Checks if the extracted ID is exactly 6 digits."""
        clean_id = "".join(filter(str.isdigit, file_id))
        return bool(self.tdf_pattern.match(clean_id))

    def calculate_checksum(self, file_path):
        """Generates an MD5 hash to ensure file integrity."""
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def verify_transfer(self, source, destination):
        """Compares hashes before and after moving a record."""
        return self.calculate_checksum(source) == self.calculate_checksum(destination)

# Example Usage for your README/Tests:
# validator = RecordValidator()
# if validator.is_valid_id("12-34-56"):
#     print("Ready for TDF routing.")
