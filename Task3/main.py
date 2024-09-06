import os
import subprocess

def run_command(command):
    """Run a shell command and return the output as a string."""
    return subprocess.check_output(command, shell=True).decode('utf-8').strip()

def get_hardware_info():
    # Collecting hardware details using Linux commands
    hardware_details = {}
    
    # Get Byte Order
    byte_order = run_command("lscpu | grep 'Byte Order' | awk '{print $3, $4}'")
    hardware_details['Byte Order'] = byte_order
    
    # Get Core(s) per socket and Socket(s)
    cores_per_socket = run_command("lscpu | grep 'Core(s) per socket' | awk '{print $4}'")
    hardware_details['Core(s) per socket'] = cores_per_socket
    
    sockets = run_command("lscpu | grep 'Socket(s)' | awk '{print $2}'")
    hardware_details['Socket(s)'] = sockets
    
    # Get Model name
    model_name = run_command("lscpu | grep 'Model name' | cut -d ':' -f 2")
    hardware_details['Model name'] = model_name.strip()
    
    # Get CPU MHz, CPU max MHz, CPU min MHz
    cpu_mhz = run_command("lscpu | grep 'CPU MHz' | awk '{print $3}'")
    hardware_details['CPU MHz'] = cpu_mhz
    
    cpu_max_mhz = run_command("lscpu | grep 'CPU max MHz' | awk '{print $4}'")
    hardware_details['CPU max MHz'] = cpu_max_mhz
    
    cpu_min_mhz = run_command("lscpu | grep 'CPU min MHz' | awk '{print $4}'")
    hardware_details['CPU min MHz'] = cpu_min_mhz
    
    # Check if Virtualization is supported
    virtualization = run_command("lscpu | grep 'Virtualization' | awk '{print $2}'")
    hardware_details['Virtualization Support'] = virtualization if virtualization else "Not supported"
    
    # Get L1, L2, L3 cache sizes
    l1_cache = run_command("lscpu | grep 'L1d cache' | awk '{print $3}'")
    hardware_details['L1 cache'] = l1_cache
    
    l2_cache = run_command("lscpu | grep 'L2 cache' | awk '{print $3}'")
    hardware_details['L2 cache'] = l2_cache
    
    l3_cache = run_command("lscpu | grep 'L3 cache' | awk '{print $3}'")
    hardware_details['L3 cache'] = l3_cache
    
    # Get total RAM memory
    ram_memory = run_command("free -m | grep Mem | awk '{print $2}'")
    hardware_details['RAM Memory'] = ram_memory + "MB"
    
    return hardware_details

def save_specs_to_file():
    # Get the username of the current user
    username = os.getlogin()
    
    # Define the directory and file path
    directory = f"/home/{username}/Details"
    file_path = os.path.join(directory, "Specs.txt")

    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Get hardware info
    hardware_details = get_hardware_info()
    
    # Write details to the file
    with open(file_path, "w") as file:
        for key, value in hardware_details.items():
            file.write(f"{key}: {value}\n")
    
    print(f"Hardware details saved to {file_path}")

if __name__ == "__main__":
    save_specs_to_file()
