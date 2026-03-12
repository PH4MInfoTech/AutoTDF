import logging

# Configure logging to write to the file
logging.basicConfig(
    filename='tdf_audit.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def sort_records(source_dir, dest_dir):
    # ... your setup code ...
    
    for filename in tqdm(files, desc="Processing Records"):
        # Log the start of the attempt
        logging.info(f"Attempting to process: {filename}")
        
        record_id = validator.extract_id(filename)
        if record_id:
            # logic to move file...
            logging.info(f"SUCCESS: Moved {filename} to TDF {record_id}")
        else:
            logging.warning(f"SKIPPED: No valid 6-digit ID found in {filename}")

class TDFSorter:
    def __init__(self, source_dir, archive_dir):
        self.source = source_dir
        self.archive = archive_dir
        self.validator = RecordValidator()

    def process_files(self):
        if not os.path.exists(self.source):
            print(f"Error: Source directory {self.source} not found.")
            return

        for filename in os.listdir(self.source):
            file_path = os.path.join(self.source, filename)
            
            # Skip directories
            if os.path.isdir(file_path):
                continue

            # 1. Extract and Validate ID (looking for 6 digits)
            clean_id = "".join(filter(str.isdigit, filename))
            
            if self.validator.is_valid_id(clean_id):
                # TDF Logic: 12-34-56 -> Primary: 56, Secondary: 34, Tertiary: 12
                tertiary, secondary, primary = clean_id[:2], clean_id[2:4], clean_id[4:]
                
                # 2. Build Destination Path
                dest_dir = os.path.join(self.archive, primary, secondary)
                os.makedirs(dest_dir, exist_ok=True)
                dest_path = os.path.join(dest_dir, filename)

                # 3. Secure Move with Integrity Check
                try:
                    # Calculate checksum before move
                    original_hash = self.validator.calculate_checksum(file_path)
                    
                    shutil.move(file_path, dest_path)
                    
                    # Verify integrity after move
                    if self.validator.verify_transfer(dest_path, original_hash if 'original_hash' in locals() else ""):
                        logging.info(f"SUCCESS: Moved {filename} to {dest_dir}")
                    else:
                        logging.error(f"CORRUPTION: {filename} hash mismatch after move!")
                
                except Exception as e:
                    logging.error(f"FAILURE: Could not move {filename}. Error: {e}")
            else:
                logging.warning(f"SKIPPED: {filename} does not contain a valid 6-digit TDF ID.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automate Terminal Digit Filing System")
    parser.add_argument("--source", required=True, help="Path to unsorted files")
    parser.add_argument("--dest", required=True, help="Path to TDF archive root")
    
    args = parser.parse_args()
    
    sorter = TDFSorter(args.source, args.dest)
    print(f"Starting TDF Sort: {args.source} -> {args.dest}")
    sorter.process_files()
    print("Check tdf_audit.log for details.")
