"""
Log Analyzer Tool
Author: David Emmanuel

Description:
This my simple program reads a system log file and analyzes it to identify
errors, warnings, and informational messages. I will say it also detects
malformed log entries and reports the most frequent error in the system. I will say more of a verification type of tool I came up with

"""

def parse_log_line(line):
    """
    this parses a single log line in the system

    Expected format:
    [LEVEL] Message text

    Example:
    [ERROR] Database connection failed

    Returns:
        tuple(level, message) or (None, None) if malformed
    """
    line = line.strip()

    if not line.startswith("[") or "]" not in line:
        return None, None

    try:
        level_end = line.index("]")
        level = line[1:level_end]
        message = line[level_end + 1:].strip()

        if not message:
            return None, None

        return level, message
    except ValueError:
        return None, None


def analyze_log_file(file_path):
    """
    this will read and analyze the log file.

    Returns:
        dict with analysis results
    """
    stats = {
        "ERROR": 0,
        "WARNING": 0,
        "INFO": 0,
        "malformed": 0,
        "error_messages": {}
    }

    try:
        with open(file_path, "r") as file:
            for line_number, line in enumerate(file, start=1):
                level, message = parse_log_line(line)

                if level is None:
                    stats["malformed"] += 1
                    continue

                if level in stats:
                    stats[level] += 1

                    if level == "ERROR":
                        if message not in stats["error_messages"]:
                            stats["error_messages"][message] = 1
                        else:
                            stats["error_messages"][message] += 1
                else:
                    stats["malformed"] += 1

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

    return stats


def get_most_common_error(error_messages):
    
    """
    this determines the most frequent error message in the system

    """
    if not error_messages:
        return None, 0

    most_common = max(error_messages.items(), key=lambda item: item[1])
    return most_common


def print_report(stats):
    """
    this will print a formatted analysis report.
    """
    print("\n--- Log Analysis Report ---")
    print(f"INFO messages: {stats['INFO']}")
    print(f"WARNING messages: {stats['WARNING']}")
    print(f"ERROR messages: {stats['ERROR']}")
    print(f"Malformed entries: {stats['malformed']}")

    error, count = get_most_common_error(stats["error_messages"])
    if error:
        print(f"\nMost frequent ERROR:")
        print(f"'{error}' occurred {count} times")
    else:
        print("\nNo error messages found.")


def main():
    """
    the main entry point of the program
    """
    log_file_path = "David_sample_log.txt" # this where i specify any log file path here 
    results = analyze_log_file(log_file_path)

    if results:
        print_report(results)


if __name__ == "__main__":
    main()


# end of my simple program code