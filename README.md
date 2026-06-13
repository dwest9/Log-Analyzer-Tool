# Automated System Log Analyzer & Verification Tool

## Project Overview
This project features a modular, high-performance **Python text-parsing utility** designed to automate the ingestion, analysis, and auditing of unstructured enterprise system logs. 

In a production environment, reading through thousands of lines of log files manually to find system failures is functionally impossible. This tool programmatically categorizes system log event levels (INFO, WARNING, ERROR), tracks error frequencies to isolate recurring infrastructural bottlenecks, and filters out malformed or corrupted log strings to ensure operational data integrity.

---

## Core Technical Features
* **Pattern-Based Boundary Parsing:** Implements granular string-manipulation algorithms to safely dissect standard log tokens (`[LEVEL] Message`) without relying on expensive, heavy third-party regex overhead.
* **Algorithmic Error Aggregation:** Utilizes hash-map (dictionary) data structures to dynamically aggregate specific error occurrences, automatically bubbling up the most frequent root-cause system fault.
* **Data Sanitization & Quarantine:** Built with strict validation checkpoints to detect, count, and isolate malformed strings or invalid log signatures, preventing data corruption during automated reporting.
* **Production-Ready Reporting Layer:** Outputs a clean, structured terminal diagnostic report detailing event type distributions and the exact frequency of critical errors.

---

2. Live Terminal Output Report
When executed, the script processes the dataset and prints out a comprehensive infrastructure health summary:

 --- Log Analysis Report ---
 
INFO messages: 2

WARNING messages: 1

ERROR messages: 3

Malformed entries: 1


Most frequent ERROR:

'Database connection failed' occurred 2 times

--->>> How to Run the Tool Locally
Clone the Repository:
-> git clone [https://github.com/dwest9/Log-Analyzer-Tool.git](https://github.com/dwest9/Log-Analyzer-Tool.git)

cd Log-Analyzer-Tool

Verify Dataset:
Ensure a text file named David_sample_log.txt exists in the same root directory as the script.

Execute the Script:
python Log_Analyzer_Tool.py
