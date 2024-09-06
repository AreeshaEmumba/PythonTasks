import subprocess

def run_command(command):
    """
    Runs a shell command and returns its output or "Not Found" if the command fails.

    Args:
        command (str): The shell command to run.

    Returns:
        str: The result of the command or "Not Found" if the command fails.
    """
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0 and result.stdout.strip():
        return result.stdout.strip()  # Return the command output if successful
    else:
        return "Not Found"  # Return "Not Found" if the command fails or has empty output

def extract_info_from_file(file_path, patterns):
    """
    Extracts specific information from a file based on a list of patterns.

    Args:
        file_path (str): Path to the file from which to extract information.
        patterns (dict): A dictionary where the key is the label and the value is the pattern to search.

    Returns:
        dict: A dictionary of extracted information with the pattern name as keys.
    """
    results = {}
    for label, command in patterns.items():
        results[label] = run_command(command.format(file=file_path))
    return results

def write_to_output_file(output_file, sections):
    """
    Writes extracted information into an output file in a structured format.

    Args:
        output_file (str): The path to the output file.
        sections (list of tuples): A list of sections to write to the file, 
                                   where each section is a tuple (title, info_dict).
    """
    with open(output_file, 'w') as f:
        for section_title, info_dict in sections:
            f.write(f"{section_title}:\n")
            for label, value in info_dict.items():
                f.write(f"{label}: {value}\n")
            f.write("\n")  # Add a new line after each section

if __name__ == "__main__":
    # Define the file paths
    tmilt_file = "/home/emumba/PythonTasks/Task7/tmilt.0.231215.075551.6BT+.3FzgZTbd.log"
    controller_file = "/home/emumba/PythonTasks/Task7/controller.231215.075537.fpMs.8qpS7S5pG.log"
    output_file = "/home/emumba/PythonTasks/Task7/parsed_information.txt"
    
    # Define patterns and commands for the tmilt file
    tmilt_patterns = {
        "Working dir": "grep 'Initial working dir:' {file} | awk -F': ' '{{print $2}}'",
        "Installation Location": "grep 'Location of the installation:' {file} | awk -F': ' '{{print $2}}'",
        "Log file Path": "grep 'This log file is:' {file} | awk -F': ' '{{print $2}}'",
        "Host": "grep 'Running on:' {file} | awk -F': ' '{{print $2}}'",
        "Current OS": "grep 'Current OS:' {file} | awk -F': ' '{{print $2}}'",
        "Uptime": "grep 'Uptime:' {file} | awk -F': ' '{{print $2}}'",
        "RAM": "grep 'RAM:' {file} | awk -F': ' '{{print $2}}'",
        "Build information": "grep 'Build information:' {file} | awk -F': ' '{{print $2}}'",
        "Release": "grep 'Release:' {file} | awk -F': ' '{{print $2}}'",
        "Build": "grep 'Build:' {file} | awk -F': ' '{{print $2}}'",
        "Revision": "grep 'Revision:' {file} | awk -F': ' '{{print $2}}'",
        "Sandbox": "grep 'Sandbox:' {file} | awk -F': ' '{{print $2}}'",
        "MBF exec time": "grep 'MBF output generation exec time:' {file} | awk -F': ' '{{print $2}}'",
        "QTM exec time": "grep 'QTM exec time:' {file} | awk -F': ' '{{print $2}}'"
    }
    
    # Define patterns and commands for the controller file
    controller_patterns = {
        "Start time": "grep 'Start time:' {file} | awk -F': ' '{{print $2}}'",
        "Working Directory": "grep 'Working Directory:' {file} | awk -F': ' '{{print $2}}'",
        "Installation location": "grep 'Installation location:' {file} | awk -F': ' '{{print $2}}'",
        "Path to Log file": "grep 'Path to Log file:' {file} | awk -F': ' '{{print $2}}'",
        "Running Information": "grep 'Running Information:' {file}",
        "Build information": "grep 'Build information:' {file}",
        "Ending time": "grep 'Ending time:' {file} | awk -F': ' '{{print $2}}'",
        "Session Duration": "grep 'Session Duration:' {file} | awk -F': ' '{{print $2}}'",
        "Fatal Count": "grep 'Fatal Count:' {file} | awk -F': ' '{{print $2}}'",
        "Error Count": "grep 'Error Count:' {file} | awk -F': ' '{{print $2}}'",
        "Warning Count": "grep 'Warning Count:' {file} | awk -F': ' '{{print $2}}'",
        "Exit code with description": "grep 'Exit code:' {file} | awk -F': ' '{{print $2}}'"
    }
    
    # Extract information from both files
    tmilt_info = extract_info_from_file(tmilt_file, tmilt_patterns)
    controller_info = extract_info_from_file(controller_file, controller_patterns)
    
    # Combine the sections with titles
    sections_to_write = [
        ("Tmilt File Information", tmilt_info),
        ("Controller File Information", controller_info)
    ]
    
    # Write combined information to the output file
    write_to_output_file(output_file, sections_to_write)

    print(f"Parsed information saved to {output_file}")
