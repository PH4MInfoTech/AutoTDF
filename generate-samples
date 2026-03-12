import os
import random

def generate_test_data(directory, count=50):
    """Creates dummy files with random 6-digit IDs for testing."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

    print(f"Generating {count} sample files...")
    
    for _ in range(count):
        # Generate a random 6-digit number
        random_id = f"{random.randint(0, 999999):06d}"
        
        # Mix up the formats to test the regex (some with hyphens, some without)
        formats = [
            f"Record_{random_id}.txt",
            f"{random_id[:2]}-{random_id[2:4]}-{random_id[4:]}.txt",
            f"Scan_{random_id[:2]} {random_id[2:4]} {random_id[4:]}.pdf"
        ]
        
        filename = random.choice(formats)
        file_path = os.path.join(directory, filename)
        
        with open(file_path, "w") as f:
            f.write(f"Dummy data for Patient ID: {random_id}")
            
    print(f"Success! {count} files generated in {directory}")

if __name__ == "__main__":
    # Defaulting to a local 'inbox' folder for the demo
    generate_test_data("data/inbox", count=100)
