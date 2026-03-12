# TDF-Automator: Healthcare Record Sorting Engine

## 📄 Overview
Terminal Digit Filing (TDF) is the gold standard for high-volume medical record management. Unlike alphabetic filing, TDF prevents "bottlenecks" by distributing records evenly across 100 primary sections (00-99).

This project automates the digital transition of TDF. It parses 6-digit Patient IDs, validates them, and routes files into a structured, triple-tier directory system.

## 🚀 Key Features
* **Regex-Based Extraction:** Identifies 100-20-45 patterns even in messy filenames.
* **Dynamic Directory Creation:** Automatically builds the `Primary/Secondary/Tertiary` folder tree.
* **Audit Logging:** Generates a CSV manifest of every file move for HIPAA-compliant tracking.
* **Batch Processing:** Handles thousands of records in seconds.

## 🛠️ How It Works
The engine treats a 6-digit ID (e.g., `12-34-56`) as a hierarchical path:
1.  **Primary (Last two digits):** `56` (The main drawer/folder)
2.  **Secondary (Middle two digits):** `34` (The sub-divider)
3.  **Tertiary (First two digits):** `12` (The final sequential file)



## 📥 Installation & Usage
1. Clone the repo:
   ```bash
   git clone [https://github.com/YourUsername/TDF-Automator.git](https://github.com/YourUsername/TDF-Automator.git)
