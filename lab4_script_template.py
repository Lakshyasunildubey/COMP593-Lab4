import sys
import os
import re
import csv

def main(log_file_path):
    log_file = get_log_file_path_from_cmd_line(log_file_path)
    return

# TODO: Step 3
def get_log_file_path_from_cmd_line(log_file_path):
    return

# TODO: Steps 4-7
   print("Checking for SSHD records...")
sshd_records, _ = filter_log_by_regex(log_file, 'sshd', ignore_case=True, print_summary=True, print_records=True)

print("Checking for invalid user records...")
invalid_user_records, _ = filter_log_by_regex(log_file, 'invalid user', ignore_case=True, print_summary=True, print_records=True)

print("Checking for specific invalid user IP records...")
specific_invalid_user_records, _ = filter_log_by_regex(log_file, 'invalid user.*220.195.35.40', ignore_case=True, print_summary=True, print_records=True)

print("Checking for error records...")
error_records, _ = filter_log_by_regex(log_file, 'error', ignore_case=True, print_summary=True, print_records=True)

print("Checking for PAM records...")
pam_records, _ = filter_log_by_regex(log_file, 'pam', ignore_case=True, print_summary=True, print_record=True)

"""Gets a list of records in a log file that match a specified regex.

    Args:
        log_file (str): Path of the log file
        regex (str): Regex filter
        ignore_case (bool, optional): Enable case insensitive regex matching. Defaults to True.
        print_summary (bool, optional): Enable printing summary of results. Defaults to False.
        print_records (bool, optional): Enable printing all records that match the regex. Defaults to False.

    Returns:
        (list, list): List of records that match regex, List of tuples of captured data
    """
return

# TODO: Step 8
def tally_port_traffic(log_file):
  port_traffic = {}

with open(log_file, 'r') as file:
        for line in file:
            match = re.search(r'DPT=(\d+)', line)
            if match:
                port = match.group(1)
                if port in port_traffic:
                    port_traffic[port] += 1
                else:
                    port_traffic[port] = 1 
    return

# TODO: Step 9
def generate_port_traffic_report(log_file, port_number):
    report_file = f"destination_port_{port}_report.csv"

    with open(log_file, 'r') as file, open(report_file, 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Time', 'Source IP', 'Destination IP', 'Source Port', 'Destination Port']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for line in file:
            match = re.search(rf'(\w+ \d+ \d+:\d+:\d+) .*SRC=(.*?) DST=(.*?) .*SPT=(.*?) DPT={port}', line)
            if match:
                date_time = match.group(1).split()
                date = date_time[0]
                time = date_time[1]
                src_ip = match.group(2)
                dst_ip = match.group(3)
                src_port = match.group(4)

                writer.writerow({
                    'Date': date,
                    'Time': time,
                    'Source IP': src_ip,
                    'Destination IP': dst_ip,
                    'Source Port': src_port,
                    'Destination Port': port
                })
    return

# TODO: Step 11
def generate_invalid_user_report(log_file):
    return

# TODO: Step 12
def generate_source_ip_log(log_file, ip_address):
    return

if __name__ == '__main__':
    main()