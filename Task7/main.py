def search_pattern(file_path, pattern):
    """
    Searches for a pattern in the file, returns the value on the same line or the next line.

    Args:
        file_path (str): The path to the file to be searched.
        pattern (str): The pattern to search for.

    Returns:
        str: The extracted value, or empty string if not found.
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if pattern in line:
                # Try to extract value from the same line
                parts = line.strip().split(pattern, 1)
                if len(parts) > 1 and parts[1].strip():
                    return parts[1].strip()
                # Else, try to get value from the next line
                elif i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    if next_line:
                        return next_line
    return ''


# Functions to extract various details from tmilt or controller files
def get_working_directory(file_path):
    return search_pattern(file_path, 'Initial working dir:') or search_pattern(file_path, 'Working Directory:')

def get_installation_location(file_path):
    return search_pattern(file_path, 'Location of installation:') or search_pattern(file_path, 'Installation location:')

def get_log_file_path(file_path):
    return search_pattern(file_path, 'This log file is:')

def get_host(file_path):
    return search_pattern(file_path, 'Host:')

def get_current_os(file_path):
    return search_pattern(file_path, 'Current OS:')

def get_uptime(file_path):
    return search_pattern(file_path, 'Uptime:')

def get_ram(file_path):
    return search_pattern(file_path, 'RAM:')

def get_build_information(file_path):
    return search_pattern(file_path, 'Build information:') or search_pattern(file_path, 'All Build information:')

def get_release(file_path):
    return search_pattern(file_path, 'Release:')

def get_build(file_path):
    return search_pattern(file_path, 'Build:')

def get_revision(file_path):
    return search_pattern(file_path, 'Revision:')

def get_sandbox(file_path):
    return search_pattern(file_path, 'Sandbox:')

def get_mbf_exec_time(file_path):
    return search_pattern(file_path, 'MBF output generation exec time')

def get_qtm_exec_time(file_path):
    return search_pattern(file_path, 'QTM exec time')

def get_start_time(file_path):
    return search_pattern(file_path, 'Start time:')

def get_all_running_information(file_path):
    return search_pattern(file_path, 'All Running Information:')

def get_ending_time(file_path):
    return search_pattern(file_path, 'Ending time:')

def get_session_duration(file_path):
    return search_pattern(file_path, 'Session Duration:')

def get_fatal_count(file_path):
    return search_pattern(file_path, 'Fatal Count:')

def get_error_count(file_path):
    return search_pattern(file_path, 'Error Count:')

def get_warning_count(file_path):
    return search_pattern(file_path, 'Warning Count:')

def get_exit_code_with_description(file_path):
    return search_pattern(file_path, 'Exit code with description:')


# Extraction functions for each file type
def extract_details_file1(file_path):
    results = {
        'Working dir': get_working_directory(file_path),
        'Installation Location': get_installation_location(file_path),
        'Log file Path': get_log_file_path(file_path),
        'Host': get_host(file_path),
        'Current OS': get_current_os(file_path),
        'Uptime': get_uptime(file_path),
        'RAM': get_ram(file_path),
        'Build information': get_build_information(file_path),
        'Release': get_release(file_path),
        'Build': get_build(file_path),
        'Revision': get_revision(file_path),
        'Sandbox': get_sandbox(file_path),
        'MBF exec time': get_mbf_exec_time(file_path),
        'QTM exec time': get_qtm_exec_time(file_path)
    }
    return results


def extract_details_file2(file_path):
    results = {
        'Start time': get_start_time(file_path),
        'Working Directory': get_working_directory(file_path),
        'Installation location': get_installation_location(file_path),
        'This log file is:': get_log_file_path(file_path),
        'All Running Information': get_all_running_information(file_path),
        'All Build information': get_build_information(file_path),
        'Ending time': get_ending_time(file_path),
        'Session Duration': get_session_duration(file_path),
        'Fatal Count': get_fatal_count(file_path),
        'Error Count': get_error_count(file_path),
        'Warning Count': get_warning_count(file_path),
        'Exit code with description': get_exit_code_with_description(file_path)
    }
    return results


def write_to_output(results, output_file):
    """
    Writes the search results to an output file.

    Args:
        results (dict): A dictionary of search results.
        output_file (str): The path to the output file.
    """
    with open(output_file, 'w') as f:
        for file_path, stats in results.items():
            f.write(f"File: {file_path}\n")
            for key, value in stats.items():
                f.write(f"{key}: {value}\n")
            f.write("\n")


if __name__ == "__main__":
    """
    Main function to process files and write the results to a single output file.
    """
    # Define the file paths
    file1_path = '/home/emumba/PythonTasks/Task7/tmilt.0.231215.075551.6BT+.3FzgZTbd.log'
    file2_path = '/home/emumba/PythonTasks/Task7/controller.231215.075537.fpMs.8qpS7S5pG.log'
    output_file_path = '/home/emumba/PythonTasks/Task7/parsed_information.txt'

    # Extract information from the files
    results_file1 = extract_details_file1(file1_path)
    results_file2 = extract_details_file2(file2_path)

    # Combine results from both files
    combined_results = {
        file1_path: results_file1,
        file2_path: results_file2
    }

    # Write the combined search results to the output file
    write_to_output(combined_results, output_file_path)

    print(f"Parsed information saved to {output_file_path}")
