import subprocess
import os

def run_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0 and result.stdout.strip():
        return result.stdout.strip()  # Return the command output if successful
    else:
       return " "  # Return " " if the command fails or has empty output

# Functions to extract specific stats from tmilt files
def extract_working_dir(file_path):
    command = "grep 'Initial working dir:' {file} | awk -F': ' '{{print $2}}'".format(file=file_path)
    return run_command(command)

def extract_installation_location(file_path):
    command = "grep 'Location of the installation:' {file} | awk -F': ' '{{print $2}}'".format(file=file_path)
    return run_command(command)

def extract_log_file_path(file_path):
    command = "grep 'This log file is:' {file} | awk -F': ' '{{print $2}}'".format(file=file_path)
    return run_command(command)

def extract_host(file_path):
    command = "grep 'Running on:' {file} | awk -F': ' '{{print $2}}'".format(file=file_path)
    return run_command(command)

def extract_current_os(file_path):
    command = "grep 'Current OS:' {file} | awk -F': ' '{{print $2}}'".format(file=file_path)
    return run_command(command)

def extract_uptime(file_path):
    command = "grep 'Uptime:' {file} | awk -F': ' '{{print $2}}'".format(file=file_path)
    return run_command(command)

def extract_ram(file_path):
    command = "grep 'RAM:' {file} | awk -F': ' '{{print $2}}'".format(file=file_path)
    return run_command(command)

def extract_build_info_tmilt(file_path):
    command = "grep 'Build information:' {file} | awk -F': ' '{{print $2}}'".format(file=file_path)
    return run_command(command)

def extract_release(file_path):
    command = "grep 'Release:' {file} | awk -F': ' '{{print $2}}'".format(file=file_path)
    return run_command(command)

def extract_build(file_path):
    command = "grep 'Build:' {file} | awk -F': ' '{{print $2}}'".format(file=file_path)
    return run_command(command)

def extract_revision(file_path):
    command = "grep 'Revision:' {file} | awk -F': ' '{{print $2}}'".format(file=file_path)
    return run_command(command)

def extract_sandbox(file_path):
    command = "grep 'Sandbox:' {file} | awk -F': ' '{{print $2}}'".format(file=file_path)
    return run_command(command)

def extract_mbf_exec_time(file_path):
    command = "grep 'MBF output generation exec time:' {file} | awk -F': ' '{{print $2}}'".format(file=file_path)
    return run_command(command)

def extract_qtm_exec_time(file_path):
    command = "grep 'QTM exec time:' {file} | awk -F': ' '{{print $2}}'".format(file=file_path)
    return run_command(command)


# Functions to extract specific stats from controller files
def extract_start_time(file_path):
    command = "grep 'Start time:' {file} | awk -F': ' '{{print $2}}'".format(file=file_path)
    return run_command(command)

def extract_working_directory(file_path):
    command = "grep 'Working Directory:' {file} | awk -F': ' '{{print $2}}'".format(file=file_path)
    return run_command(command)

def extract_installation_location_controller(file_path):
    command = "grep 'Installation location:' {file} | awk -F': ' '{{print $2}}'".format(file=file_path)
    return run_command(command)

def extract_running_info(file_path):
    # Assuming multi-line, you may want to capture several lines after this keyword
    command = "grep -A 2 'Running Information:' {file}".format(file=file_path)
    return run_command(command)

def extract_build_info_controller(file_path):
    # Same as tmilt but kept separate for controller-specific context
    command = "grep 'Build information:' {file} | awk -F': ' '{{print $2}}'".format(file=file_path)
    return run_command(command)

def extract_ending_time(file_path):
    command = "grep 'Ending time:' {file} | awk -F': ' '{{print $2}}'".format(file=file_path)
    return run_command(command)

def extract_session_duration(file_path):
    command = "grep 'Session Duration:' {file} | awk -F': ' '{{print $2}}'".format(file=file_path)
    return run_command(command)

def extract_fatal_count(file_path):
    command = "grep 'Fatal Count:' {file} | awk -F': ' '{{print $2}}'".format(file=file_path)
    return run_command(command)

def extract_error_count(file_path):
    command = "grep 'Error Count:' {file} | awk -F': ' '{{print $2}}'".format(file=file_path)
    return run_command(command)

def extract_warning_count(file_path):
    command = "grep 'Warning Count:' {file} | awk -F': ' '{{print $2}}'".format(file=file_path)
    return run_command(command)

def extract_exit_code(file_path):
    command = "grep 'Exit code:' {file} | awk -F': ' '{{print $2}}'".format(file=file_path)
    return run_command(command)

def process_tmilt_files(files):
    tmilt_results = []
    for file_path in files:
        if os.path.exists(file_path):
            result = {
                "Working dir": extract_working_dir(file_path),
                "Installation Location": extract_installation_location(file_path),
                "Log file Path": extract_log_file_path(file_path),
                "Host": extract_host(file_path),
                "Current OS": extract_current_os(file_path),
                "Uptime": extract_uptime(file_path),
                "RAM": extract_ram(file_path),
                "Build information": extract_build_info_tmilt(file_path),
                "Release": extract_release(file_path),
                "Build": extract_build(file_path),
                "Revision": extract_revision(file_path),
                "Sandbox": extract_sandbox(file_path),
                "MBF exec time": extract_mbf_exec_time(file_path),
                "QTM exec time": extract_qtm_exec_time(file_path),
            }
            tmilt_results.append((file_path, result))
        else:
            print(f"File not found: {file_path}")
    return tmilt_results


def process_controller_files(files):
    controller_results = []
    for file_path in files:
        if os.path.exists(file_path):
            result = {
                "Start time": extract_start_time(file_path),
                "Working Directory": extract_working_directory(file_path),
                "Installation location": extract_installation_location_controller(file_path),
                "Running Information": extract_running_info(file_path),
                "Build information": extract_build_info_controller(file_path),
                "Ending time": extract_ending_time(file_path),
                "Session Duration": extract_session_duration(file_path),
                "Fatal Count": extract_fatal_count(file_path),
                "Error Count": extract_error_count(file_path),
                "Warning Count": extract_warning_count(file_path),
                "Exit code with description": extract_exit_code(file_path),
            }
            controller_results.append((file_path, result))
        else:
            print(f"File not found: {file_path}")
    return controller_results


def write_to_output_file(output_file, tmilt_sections, controller_sections):
    with open(output_file, 'w') as f:
        for file_path, info_dict in tmilt_sections:
            f.write(f"Tmilt File: {file_path}\n")
            for label, value in info_dict.items():
                f.write(f"{label}: {value}\n")
            f.write("\n")  # Add a new line after each file's stats

        for file_path, info_dict in controller_sections:
            f.write(f"Controller File: {file_path}\n")
            for label, value in info_dict.items():
                f.write(f"{label}: {value}\n")
            f.write("\n")  # Add a new line after each file's stats

if __name__ == "__main__":
    # Define the file paths (multiple files)
    tmilt_files = [
        "/home/emumba/PythonTasks/Task7/tmilt.0.231215.075551.6BT+.3FzgZTbd.log",
        # Add more tmilt files here
    ]
    
    controller_files = [
        "/home/emumba/PythonTasks/Task7/controller.231215.075537.fpMs.8qpS7S5pG.log",
        # Add more controller files here
    ]
    
    output_file = "/home/emumba/PythonTasks/Task7/parsed_information.txt"
    
    # Process tmilt and controller files
    tmilt_info = process_tmilt_files(tmilt_files)
    controller_info = process_controller_files(controller_files)
    
    # Write combined information to the output file
    write_to_output_file(output_file, tmilt_info, controller_info)

    print(f"Parsed information saved to {output_file}")
