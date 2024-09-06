import subprocess

# Function to run a shell command and return its output
def run_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        return result.stdout.strip()  # Return the command output
    else:
        return f"Error: {result.stderr}"  # Return error message if the command fails

# Define the file paths (update the file paths as necessary)
tmilt_file = "/home/emumba/PythonTasks/Task7/tmilt.0.231215.075551.6BT+.3FzgZTbd.log"
controller_file = "/home/emumba/PythonTasks/Task7/controller.231215.075537.fpMs.8qpS7S5pG.log"
output_file = "/home/emumba/PythonTasks/Task7/parsed_information.txt"

# Open the output file for writing
with open(output_file, 'w') as f:
    # Extract information from the tmilt file using Linux commands
    f.write("Tmilt File Information:\n")
    f.write(f"Working dir: {run_command(f'grep \"Initial working dir:\" {tmilt_file} | awk -F\': \' \'{{print $2}}\')} \n")
    f.write(f"Installation Location: {run_command(f'grep \"Location of the installation:\" {tmilt_file} | awk -F\': \' \'{{print $2}}\')} \n")
    f.write(f"Log file Path: {run_command(f'grep \"This log file is:\" {tmilt_file} | awk -F\': \' \'{{print $2}}\')} \n")
    f.write(f"Host: {run_command(f'grep \"Running on:\" {tmilt_file} | awk -F\': \' \'{{print $2}}\')} \n")
    f.write(f"Current OS: {run_command(f'grep \"Current OS:\" {tmilt_file} | awk -F\': \' \'{{print $2}}\')} \n")
    f.write(f"Uptime: {run_command(f'grep \"Uptime:\" {tmilt_file} | awk -F\': \' \'{{print $2}}\')} \n")
    f.write(f"RAM: {run_command(f'grep \"RAM:\" {tmilt_file} | awk -F\': \' \'{{print $2}}\')} \n")
    f.write(f"Build information: {run_command(f'grep \"Build information:\" {tmilt_file} | awk -F\': \' \'{{print $2}}\')} \n")
    f.write(f"Release: {run_command(f'grep \"Release:\" {tmilt_file} | awk -F\': \' \'{{print $2}}\')} \n")
    f.write(f"Build: {run_command(f'grep \"Build:\" {tmilt_file} | awk -F\': \' \'{{print $2}}\')} \n")
    f.write(f"Revision: {run_command(f'grep \"Revision:\" {tmilt_file} | awk -F\': \' \'{{print $2}}\')} \n")
    f.write(f"Sandbox: {run_command(f'grep \"Sandbox:\" {tmilt_file} | awk -F\': \' \'{{print $2}}\')} \n")
    f.write(f"MBF exec time: {run_command(f'grep \"MBF output generation exec time:\" {tmilt_file} | awk -F\': \' \'{{print $2}}\')} \n")
    f.write(f"QTM exec time: {run_command(f'grep \"QTM exec time:\" {tmilt_file} | awk -F\': \' \'{{print $2}}\')} \n")
    
    # Extract information from the controller file using Linux commands
    f.write("\nController File Information:\n")
    f.write(f"Start time: {run_command(f'grep \"Start time:\" {controller_file} | awk -F\': \' \'{{print $2}}\')} \n")
    f.write(f"Working Directory: {run_command(f'grep \"Working Directory:\" {controller_file} | awk -F\': \' \'{{print $2}}\')} \n")
    f.write(f"Installation location: {run_command(f'grep \"Installation location:\" {controller_file} | awk -F\': \' \'{{print $2}}\')} \n")
    f.write(f"Path to Log file: {run_command(f'grep \"Path to Log file:\" {controller_file} | awk -F\': \' \'{{print $2}}\')} \n")
    f.write(f"Running Information: {run_command(f'grep \"Running Information:\" {controller_file}')} \n")
    f.write(f"Build information: {run_command(f'grep \"Build information:\" {controller_file}')} \n")
    f.write(f"Ending time: {run_command(f'grep \"Ending time:\" {controller_file} | awk -F\': \' \'{{print $2}}\')} \n")
    f.write(f"Session Duration: {run_command(f'grep \"Session Duration:\" {controller_file} | awk -F\': \' \'{{print $2}}\')} \n")
    f.write(f"Fatal Count: {run_command(f'grep \"Fatal Count:\" {controller_file} | awk -F\': \' \'{{print $2}}\')} \n")
    f.write(f"Error Count: {run_command(f'grep \"Error Count:\" {controller_file} | awk -F\': \' \'{{print $2}}\')} \n")
    f.write(f"Warning Count: {run_command(f'grep \"Warning Count:\" {controller_file} | awk -F\': \' \'{{print $2}}\')} \n")
    f.write(f"Exit code with description: {run_command(f'grep \"Exit code:\" {controller_file} | awk -F\': \' \'{{print $2}}\')} \n")

print(f"Parsed information saved to {output_file}")
