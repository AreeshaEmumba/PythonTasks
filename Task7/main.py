import subprocess

# Function to run a shell command and return its output
def run_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        return result.stdout.strip()  # Return the command output
    else:
        return f"Error: {result.stderr}"  # Return error message if the command fails

# Define the file paths (update the file paths as necessary)
tmilt_file = "tmilt.txt"
controller_file = "controller.txt"
output_file = "parsed_information.txt"

# Open the output file for writing
with open(output_file, 'w') as f:
    # Extract information from the tmilt file using Linux commands
    f.write("Tmilt File Information:\n")
    f.write("Working dir: " + run_command(f"grep 'Initial working dir:' {tmilt_file} | awk -F': ' '{{print $2}}'") + "\n")
    f.write("Installation Location: " + run_command(f"grep 'Location of the installation:' {tmilt_file} | awk -F': ' '{{print $2}}'") + "\n")
    f.write("Log file Path: " + run_command(f"grep 'This log file is:' {tmilt_file} | awk -F': ' '{{print $2}}'") + "\n")
    f.write("Host: " + run_command(f"grep 'Running on:' {tmilt_file} | awk -F': ' '{{print $2}}'") + "\n")
    f.write("Current OS: " + run_command(f"grep 'Current OS:' {tmilt_file} | awk -F': ' '{{print $2}}'") + "\n")
    f.write("Uptime: " + run_command(f"grep 'Uptime:' {tmilt_file} | awk -F': ' '{{print $2}}'") + "\n")
    f.write("RAM: " + run_command(f"grep 'RAM:' {tmilt_file} | awk -F': ' '{{print $2}}'") + "\n")
    f.write("Build information: " + run_command(f"grep 'Build information:' {tmilt_file} | awk -F': ' '{{print $2}}'") + "\n")
    f.write("Release: " + run_command(f"grep 'Release:' {tmilt_file} | awk -F': ' '{{print $2}}'") + "\n")
    f.write("Build: " + run_command(f"grep 'Build:' {tmilt_file} | awk -F': ' '{{print $2}}'") + "\n")
    f.write("Revision: " + run_command(f"grep 'Revision:' {tmilt_file} | awk -F': ' '{{print $2}}'") + "\n")
    f.write("Sandbox: " + run_command(f"grep 'Sandbox:' {tmilt_file} | awk -F': ' '{{print $2}}'") + "\n")
    f.write("MBF exec time: " + run_command(f"grep 'MBF output generation exec time:' {tmilt_file} | awk -F': ' '{{print $2}}'") + "\n")
    f.write("QTM exec time: " + run_command(f"grep 'QTM exec time:' {tmilt_file} | awk -F': ' '{{print $2}}'") + "\n")
    
    # Extract information from the controller file using Linux commands
    f.write("\nController File Information:\n")
    f.write("Start time: " + run_command(f"grep 'Start time:' {controller_file} | awk -F': ' '{{print $2}}'") + "\n")
    f.write("Working Directory: " + run_command(f"grep 'Working Directory:' {controller_file} | awk -F': ' '{{print $2}}'") + "\n")
    f.write("Installation location: " + run_command(f"grep 'Installation location:' {controller_file} | awk -F': ' '{{print $2}}'") + "\n")
    f.write("Path to Log file: " + run_command(f"grep 'Path to Log file:' {controller_file} | awk -F': ' '{{print $2}}'") + "\n")
    f.write("Running Information: " + run_command(f"grep 'Running Information:' {controller_file}") + "\n")
    f.write("Build information: " + run_command(f"grep 'Build information:' {controller_file}") + "\n")
    f.write("Ending time: " + run_command(f"grep 'Ending time:' {controller_file} | awk -F': ' '{{print $2}}'") + "\n")
    f.write("Session Duration: " + run_command(f"grep 'Session Duration:' {controller_file} | awk -F': ' '{{print $2}}'") + "\n")
    f.write("Fatal Count: " + run_command(f"grep 'Fatal Count:' {controller_file} | awk -F': ' '{{print $2}}'") + "\n")
    f.write("Error Count: " + run_command(f"grep 'Error Count:' {controller_file} | awk -F': ' '{{print $2}}'") + "\n")
    f.write("Warning Count: " + run_command(f"grep 'Warning Count:' {controller_file} | awk -F': ' '{{print $2}}'") + "\n")
    f.write("Exit code with description: " + run_command(f"grep 'Exit code:' {controller_file} | awk -F': ' '{{print $2}}'") + "\n")

print(f"Parsed information saved to {output_file}")
