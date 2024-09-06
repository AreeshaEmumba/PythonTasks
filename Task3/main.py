import os  # Import the os module to interact with the operating system.
import subprocess  # Import the subprocess module to run shell commands.

def run_command(command):
    """Run a shell command and return the output as a string."""
    # Execute the command in the shell and capture its output.
    # shell=True allows the command to be run as a shell command.
    # decode('utf-8') converts the output from bytes to a string.
    # strip() removes any leading or trailing whitespace from the output.
    return subprocess.check_output(command, shell=True).decode('utf-8').strip()

def get_hardware_info():
    """Collect hardware details from the system."""
    hardware_details = {}  # Create an empty dictionary to store hardware information.
    
    # Get Byte Order information from 'lscpu' and extract the relevant part.
    byte_order = run_command("lscpu | grep 'Byte Order' | awk '{print $3, $4}'")
    hardware_details['Byte Order'] = byte_order  # Add Byte Order to the dictionary.
    
    # Get Core(s) per socket and extract the relevant part.
    cores_per_socket = run_command("lscpu | grep 'Core(s) per socket' | awk '{print $4}'")
    hardware_details['Core(s) per socket'] = cores_per_socket  # Add Core(s) per socket to the dictionary.
    
    # Get the number of sockets and extract the relevant part.
    sockets = run_command("lscpu | grep 'Socket(s)' | awk '{print $2}'")
    hardware_details['Socket(s)'] = sockets  # Add Socket(s) to the dictionary.
    
    # Get the CPU model name and extract the part after the colon.
    model_name = run_command("lscpu | grep 'Model name' | cut -d ':' -f 2")
    hardware_details['Model name'] = model_name.strip()  # Add Model name to the dictionary, removing extra whitespace.
    
    # Get CPU MHz (current speed) and extract the relevant part.
    cpu_mhz = run_command("lscpu | grep 'CPU MHz' | awk '{print $3}'")
    hardware_details['CPU MHz'] = cpu_mhz  # Add CPU MHz to the dictionary.
    
    # Get CPU max MHz (maximum speed) and extract the relevant part.
    cpu_max_mhz = run_command("lscpu | grep 'CPU max MHz' | awk '{print $4}'")
    hardware_details['CPU max MHz'] = cpu_max_mhz  # Add CPU max MHz to the dictionary.
    
    # Get CPU min MHz (minimum speed) and extract the relevant part.
    cpu_min_mhz = run_command("lscpu | grep 'CPU min MHz' | awk '{print $4}'")
    hardware_details['CPU min MHz'] = cpu_min_mhz  # Add CPU min MHz to the dictionary.
    
    # Check if virtualization is supported and extract the relevant part.
    virtualization = run_command("lscpu | grep 'Virtualization' | awk '{print $2}'")
    hardware_details['Virtualization Support'] = virtualization if virtualization else "Not supported"
    # Add Virtualization Support to the dictionary, defaulting to "Not supported" if no information is found.
    
    # Get L1 cache size and extract the relevant part.
    l1_cache = run_command("lscpu | grep 'L1d cache' | awk '{print $3}'")
    hardware_details['L1 cache'] = l1_cache  # Add L1 cache size to the dictionary.
    
    # Get L2 cache size and extract the relevant part.
    l2_cache = run_command("lscpu | grep 'L2 cache' | awk '{print $3}'")
    hardware_details['L2 cache'] = l2_cache  # Add L2 cache size to the dictionary.
    
    # Get L3 cache size and extract the relevant part.
    l3_cache = run_command("lscpu | grep 'L3 cache' | awk '{print $3}'")
    hardware_details['L3 cache'] = l3_cache  # Add L3 cache size to the dictionary.
    
    # Get total RAM memory in MB and extract the relevant part.
    ram_memory = run_command("free -m | grep Mem | awk '{print $2}'")
    hardware_details['RAM Memory'] = ram_memory + "MB"  # Add RAM Memory to the dictionary, appending "MB" to the value.
    
    return hardware_details  # Return the dictionary containing all the hardware details.

def save_specs_to_file():
    """Save hardware specifications to a file."""
    username = os.getlogin()  # Get the username of the current user.
    
    # Define the directory path where the file will be saved.
    directory = f"/home/{username}/Details"
    # Define the full file path for the specifications file.
    file_path = os.path.join(directory, "Specs.txt")

    # Check if the directory exists; if not, create it.
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Get the hardware information by calling the get_hardware_info function.
    hardware_details = get_hardware_info()
    
    # Open the file in write mode.
    with open(file_path, "w") as file:
        # Write each key-value pair from the dictionary to the file.
        for key, value in hardware_details.items():
            file.write(f"{key}: {value}\n")
    
    # Print a message indicating that the hardware details have been saved.
    print(f"Hardware details saved to {file_path}")

# Check if this script is being run directly (not imported).
if __name__ == "__main__":
    save_specs_to_file()  # Call the function to save the hardware specifications to a file.

