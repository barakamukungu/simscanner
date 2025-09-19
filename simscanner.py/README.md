SimScanner

A safe, simulated port scanner written in Python.
This project mimics how a real port scanner works without touching the network — perfect for learning and demonstrating concepts without security risks.

Features

Simulated hosts & ports (defined in hosts.json)

Interactive mode (type host and ports manually)

CLI mode (run with arguments directly)

Supports single ports and ranges

Input validation (rejects invalid ports/ranges)

Clean, modular design

Project Structure
.
├── simscanner.py   # main program
├── hosts.json      # simulated host data
└── README.md       # project documentation

Usage
Interactive Mode

Run:

python simscanner.py


Example:

Add host name: localhost_sim
Add ports: 22,80,443,8080
22: open
80: closed
443: open
8080: closed

CLI Mode

Run:

python simscanner.py localhost_sim 20-23,443


Output:

20: closed
21: closed
22: open
23: closed
443: open

Configuration

Edit hosts.json to add or modify simulated hosts and their ports:

{
    "localhost_sim": {
        "22": "open",
        "80": "closed",
        "443": "open"
    },
    "dev_server": {
        "21": "open",
        "22": "closed",
        "8080": "open"
    }
}

Learning Goals

This project demonstrates:

Working with functions and modular design in Python

Parsing and validating user input

Using JSON for configuration

Handling command-line arguments

Writing safe simulations of real-world tools

License

This project is licensed under the MIT License — feel free to use, modify, and share.