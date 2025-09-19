# simscanner.py

import json
import sys
import os

# Load simulated hosts from hosts.json
def load_hosts(file_path="hosts.json"):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return {}
    with open(file_path, "r") as f:
        return json.load(f)

# Simulate scanning ports
def simulate_scan(host, ports, hosts_map):
    results = []
    host_map = hosts_map.get(host, {})
    for port in ports:
        status = host_map.get(str(port), "closed")
        results.append((port, status))
    return results

# Parse ports from user input
def parse_ports(port_str):
    ports = set()
    parts = port_str.split(",")

    for part in parts:
        part = part.strip()
        if not part:
            continue

        if "-" in part:
            try:
                start_str, end_str = part.split("-")
                start, end = int(start_str), int(end_str)
                if start < 1 or end > 65535 or start > end:
                    print(f"Invalid range: {part}")
                    continue
                ports.update(range(start, end + 1))
            except ValueError:
                print(f"Invalid range format: {part}")
        else:
            try:
                p = int(part)
                if 1 <= p <= 65535:
                    ports.add(p)
                else:
                    print(f"Invalid port: {p}")
            except ValueError:
                print(f"Invalid port format: {part}")

    return sorted(ports)

# Main entry point
if __name__ == "__main__":
    hosts_map = load_hosts()

    if len(sys.argv) >= 3:
        # CLI mode
        host_name = sys.argv[1]
        port_str = sys.argv[2]
        parsed_ports = parse_ports(port_str)
        if host_name not in hosts_map:
            print("Unknown host")
            sys.exit(1)
        results = simulate_scan(host_name, parsed_ports, hosts_map)
        for port, status in results:
            print(f"{port}: {status}")
    else:
        # Interactive mode
        host_name = input("Add host name: ").strip()
        if host_name not in hosts_map:
            print("Unknown host")
            sys.exit(1)

        sample_ports = input("Add ports: ")
        parsed_ports = parse_ports(sample_ports)
        results = simulate_scan(host_name, parsed_ports, hosts_map)
        for port, status in results:
            print(f"{port}: {status}")
