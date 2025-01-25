#This code installs the Piper Linux version into the home directory.
import os
import tarfile


def run_piper_installer():
    # Define the paths
    source_path = "/home/user/app"
    #source_path = "/home/user/app"
    destination_path = "/home/user/piper_installation"
    #destination_path = "/home/user/piper_installation"
    # Step 1: Fetch the .tar.gz file from the source path
    print("Step 1: Searching for .tar.gz file in", source_path)

    tar_files = [file for file in os.listdir(source_path) if file == "piper_amd64.tar.gz"]

    if not tar_files:
        print("Error: No .tar.gz file found in", source_path)
        exit(1)

    tar_file = os.path.join(source_path, tar_files[0])
    print(f"Found tar.gz file: {tar_file}")

    # Step 2: Create the directory 'piper_installation'
    print("Step 2: Creating directory", destination_path)
    os.makedirs(destination_path, exist_ok=True)
    print(f"Directory '{destination_path}' is ready.")

    # Step 3: Change into the directory and unpack the tar.gz file
    print("Step 3: Extracting tar.gz file...")
    with tarfile.open(tar_file, "r:gz") as tar:
        tar.extractall(path=destination_path)
    print(f"Extracted contents to {destination_path}")

    # Step 4: Set execution permissions for files inside 'piper'
    piper_path = os.path.join(destination_path, "piper")

    if not os.path.exists(piper_path):
        print(f"Error: 'piper' directory not found in {destination_path}")
        exit(1)

    print("Step 4: Setting execution permissions for files in 'piper'")
    exec_files = ["piper"]
    for file_name in exec_files:
        file_path = os.path.join(piper_path, file_name)
        if os.path.exists(file_path):
            os.chmod(file_path, 0o755)  # Read, write, and execute permissions for the owner
            print(f"Set execute permission for {file_name}")
        else:
            print(f"Warning: {file_name} not found in {piper_path}")

    # Step 5: Create 'output_files' directory inside 'piper' and set permissions
    output_files_path = os.path.join(piper_path, "output_files")
    print("Step 5: Creating 'output_files' directory")
    os.makedirs(output_files_path, exist_ok=True)
    os.chmod(output_files_path, 0o777)  # Read, write, and execute permissions for everyone
    print(f"'output_files' directory is ready with read/write permissions at {output_files_path}")

    print("All tasks completed successfully.")
