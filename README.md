DATA ENCODER DECODER is a Python-based data transformation tool that converts plain text into an encoded format and decodes it back when needed. It also includes session-based decoded output handling and an activity logging system that tracks encoding/decoding actions and file storage locations.
Overview:

This project is a Python-based Data Encoder–Decoder system designed to convert readable text into an encoded format and restore it back to its original form when required.
The system also includes:
Temporary decoded data display (session-based)
Activity logging system
File location tracking for encoded data
It is built for educational purposes to demonstrate how basic data transformation and logging systems work.

Features:
Encode plain text into a coded format
Decode encoded data back to original text
Encoded data is stored in the system
Decoded output is shown temporarily during runtime
Decoded data disappears when session ends
Activity log tracks all encoding/decoding operations
Stores file paths for encoded data recovery

How It Works:

1. Encoding Process
Input data is passed through a transformation function that converts it into an encoded format. This encoded data is then stored in the system.

2. Decoding Process:
When requested, encoded data is decoded back into readable form. The decoded output is shown temporarily and is cleared when the session ends.

3. Logging System:
The tool maintains a log file that records:
Encoding events
Decoding events
File storage locations
Operation timestamps

Project Structure:
Plain text
DATA-ENCODER-DECODER/
│
├── encoder.py # Handles encoding logic
├── decoder.py # Handles decoding logic
├── logger.py # Handles activity logging (if included)
├── main.py # Main program entry point
├── logs/ # Stores activity logs
└── README.md # Documentation

Modules Used:
This project mainly uses Python standard library modules, such as:
os → for file handling and directory management
sys → for system-level operations and program control
time → for timestamps in logs
json (if used) → for structured data storage
logging (if used) → for activity logging system


Example:
Input:
     hello
Encoded Output:
      aGVsbG8
Decoded Output:
     hello

Purpose of This Project
This project is designed for learning and experimentation in:
Data transformation concepts
Reversible encoding systems
Basic logging mechanisms
File handling in Python
It demonstrates how data can be encoded, stored, decoded, and tracked within a simple system.

Important Note:
This tool is created by a student (not a professional developer or cybersecurity engineer).
It is intended for educational purposes only and demonstrates basic encoding and system design concepts. It does not provide cryptographic security or protection against attacks
