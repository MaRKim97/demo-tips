import paramiko
import cv2
from time import time

def execute_remote_command_and_download_file(host, port, username, password, command, remote_file_path, local_file_path):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname=host, port=port, username=username, password=password)
        # Execute the remote command (like running your script)
        stdin, stdout, stderr = client.exec_command(command)
        # Wait for the command to complete
        stdout.channel.recv_exit_status()

        # Use SFTP to download the file generated by the script
        sftp = client.open_sftp()
        sftp.get(remote_file_path, local_file_path)
        sftp.close()

    finally:
        client.close()

def execute_remote_command(host, port, username, password, command):
    # Initialize the SSH client
    client = paramiko.SSHClient()

    # Add the remote server's SSH key automatically (not recommended for production)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the remote server
        client.connect(hostname=host, port=port, username=username, password=password)

        # Execute the command
        stdin, stdout, stderr = client.exec_command(command)

        # Read the standard output and standard error streams
        stdout = stdout.read().decode('utf-8')
        stderr = stderr.read().decode('utf-8')

        return stdout, stderr

    finally:
        # Close the client to free resources
        client.close()

# Parameters
host = '61.108.166.16'
port = 22
username = 'team002'
password = 'paju@2345'
#prompt = 'Korea Chamber of Commerce and Industry classroom'
prompt = 'An unknown monster is smiling in the Valley of Fire, where the legendary dragon seems to appear.'
command = '/home/team002/workspace/server_test/run-2.sh' + ' ' + prompt  # Make sure the script is executable
remote_file_path = '/home/team002/workspace/server_test/result2.png'  # The path where 'result.png' is saved on the remote machine
local_file_path = './result2.png'  # Where to save 'result.png' locally

start = time()
execute_remote_command_and_download_file(host, port, username, password, command, remote_file_path, local_file_path)
print(f"time = {time() - start}")
#stdout, stderr = execute_remote_command(host, port, username, password, command)
# Check the output
#if stdout:
#    print("Output:", stdout)
#if stderr:
#    print("Error:", stderr)


image = cv2.imread(local_file_path)
cv2.namedWindow("image window", cv2.WINDOW_GUI_NORMAL | cv2.WINDOW_AUTOSIZE)
cv2.imshow('image window', image)
# add wait key. window waits until user presses a key
cv2.waitKey(0)
# and finally destroy/close all open windows
cv2.destroyAllWindows()
