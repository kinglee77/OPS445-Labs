#!/usr/bin/env python3

'''
OPS445 Assignment 2
'''

import argparse
import os

def parse_command_args() -> object:
    "Set up argparse here. Call this function inside main."
    parser = argparse.ArgumentParser(description="Memory Visualiser -- See Memory Usage Report with bar charts", epilog="Copyright 2023")
    parser.add_argument("-l", "--graph_length", type=int, default=20, help="Specify the length of the graph. Default is 20.")
    parser.add_argument("-H", "--human_readable_format", action="store_true", help="Print sizes in human readable format")
    parser.add_argument("target_program", type=str, nargs='?', help="If a program is specified, show memory use of all associated processes. Show only total use if not.")
    return parser.parse_args()

def percent_to_graph(percent: float, length: int = 20) -> str:
    "Turns a percent 0.0 - 1.0 into a bar graph of specified length"
    num_hashes = int(percent * length)
    num_spaces = length - num_hashes
    return '#' * num_hashes + ' ' * num_spaces

def get_sys_mem() -> int:
    "Return total system memory (in kB)"
    with open("/proc/meminfo", "r") as meminfo:
        for line in meminfo:
            if line.startswith("MemTotal:"):
                return int(line.split()[1])  # Return the memory value as an integer

def get_avail_mem() -> int:
    "Return available memory (in kB)"
    with open("/proc/meminfo", "r") as meminfo:
        for line in meminfo:
            if line.startswith("MemAvailable:"):
                return int(line.split()[1])  # Return the available memory value as an integer

def pids_of_prog(app_name: str) -> list:
    "Given an app name, return all PIDs associated with the app"
    pids = os.popen(f'pidof {app_name}').read().strip()
    return pids.split() if pids else []

def rss_mem_of_pid(proc_id: str) -> int:
    "Given a process ID, return the Resident memory used (in kB)"
    rss_total = 0
    try:
        with open(f"/proc/{proc_id}/smaps", "r") as smaps:
            for line in smaps:
                if line.startswith("Rss:"):
                    rss_total += int(line.split()[1])
    except FileNotFoundError:
        pass  # Process might have terminated, so we handle the error gracefully
    return rss_total

def bytes_to_human_r(kibibytes: int, decimal_places: int = 2) -> str:
    "Converts kilobytes to a human-readable format"
    suffixes = ['KiB', 'MiB', 'GiB', 'TiB', 'PiB']
    suffix_index = 0
    size = kibibytes
    
    while size >= 1024 and suffix_index < len(suffixes) - 1:
        size /= 1024
        suffix_index += 1
    
    return f"{size:.{decimal_places}f} {suffixes[suffix_index]}"

if __name__ == "__main__":
    args = parse_command_args()

    if not args.target_program:
        # No specific program provided, display overall system memory usage
        total_memory = get_sys_mem()  # Get the system's total memory
        available_memory = get_avail_mem()  # Get the available system memory
        consumed_memory = total_memory - available_memory  # Calculate the used memory
        memory_usage_ratio = consumed_memory / total_memory  # Calculate the percentage of memory used

        if args.human_readable_format:
            # Convert memory values to a human-readable format
            total_memory_str = bytes_to_human_r(total_memory)
            consumed_memory_str = bytes_to_human_r(consumed_memory)
            # Display the memory usage in a human-readable format
            print(f"{'System Memory':<15} [{percent_to_graph(memory_usage_ratio, args.graph_length)}] {consumed_memory_str}/{total_memory_str}")
        else:
            # Display the memory usage in raw values
            print(f"{'System Memory':<15} [{percent_to_graph(memory_usage_ratio, args.graph_length)}] {consumed_memory}/{total_memory} KiB")

    else:
        # A specific program is provided, display memory usage for its processes
        process_ids = pids_of_prog(args.target_program)  # Retrieve process IDs for the specified program

        if not process_ids:
            print(f"{args.target_program} not found.")
        else:
            cumulative_rss = 0  # Initialize the total RSS memory
            total_memory = get_sys_mem()  # Retrieve the system's total memory

            if args.human_readable_format:
                total_memory_str = bytes_to_human_r(total_memory)  # Convert total memory to a human-readable format
            else:
                total_memory_str = f"{total_memory} KiB"  # Use the raw total memory value

            for pid in process_ids:
                rss_memory = rss_mem_of_pid(pid)  # Retrieve the RSS memory for each process ID
                cumulative_rss += rss_memory  # Accumulate the RSS memory
                memory_usage_ratio = rss_memory / total_memory  # Calculate the memory usage percentage for each process

                if args.human_readable_format:
                    rss_memory_str = bytes_to_human_r(rss_memory)  # Convert RSS memory to a human-readable format
                    # Display the RSS memory usage for each process in a human-readable format
                    print(f"{pid:<15} [{percent_to_graph(memory_usage_ratio, args.graph_length)}] {rss_memory_str}/{total_memory_str}")
                else:
                    # Display the RSS memory usage for each process in raw values
                    print(f"{pid:<15} [{percent_to_graph(memory_usage_ratio, args.graph_length)}] {rss_memory}/{total_memory} KiB")

            overall_usage_ratio = cumulative_rss / total_memory  # Calculate the overall memory usage percentage for the program

            if args.human_readable_format:
                cumulative_rss_str = bytes_to_human_r(cumulative_rss)  # Convert cumulative RSS memory to a human-readable format
                # Display the total RSS memory usage for the program in a human-readable format
                print(f"{args.target_program:<15} [{percent_to_graph(overall_usage_ratio, args.graph_length)}] {cumulative_rss_str}/{total_memory_str}")
            else:
                # Display the total RSS memory usage for the program in raw values
                print(f"{args.target_program:<15} [{percent_to_graph(overall_usage_ratio, args.graph_length)}] {cumulative_rss}/{total_memory} KiB")
