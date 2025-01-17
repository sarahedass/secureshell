import os
import socket
import paramiko
import getpass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SecureShell")

class SecureShell:
    def __init__(self, hostname, port=22):
        self.hostname = hostname
        self.port = port
        self.client = None

    def connect(self, username, password):
        try:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            logger.info(f"Connecting to {self.hostname}:{self.port} as {username}")
            self.client.connect(self.hostname, port=self.port, username=username, password=password)
            logger.info("Connection established successfully")
        except paramiko.AuthenticationException:
            logger.error("Authentication failed, please verify your credentials")
        except paramiko.SSHException as sshException:
            logger.error(f"Unable to establish SSH connection: {sshException}")
        except Exception as e:
            logger.error(f"Exception in connecting to the server: {e}")

    def execute_command(self, command):
        if self.client:
            logger.info(f"Executing command: {command}")
            stdin, stdout, stderr = self.client.exec_command(command)
            output = stdout.read().decode()
            errors = stderr.read().decode()
            if output:
                logger.info(f"Output:\n{output}")
            if errors:
                logger.error(f"Errors:\n{errors}")
        else:
            logger.error("Connection not established. Cannot execute command.")

    def close_connection(self):
        if self.client:
            logger.info("Closing connection")
            self.client.close()
        else:
            logger.error("Connection not established. Nothing to close.")

if __name__ == "__main__":
    host = input("Enter the remote host address: ")
    port = int(input("Enter the port number (default 22): ") or 22)
    user = input("Enter your username: ")
    passwd = getpass.getpass("Enter your password: ")

    ssh = SecureShell(host, port)
    ssh.connect(user, passwd)

    while True:
        cmd = input("Enter a command to execute on the remote shell (or 'exit' to quit): ")
        if cmd.lower() == 'exit':
            break
        ssh.execute_command(cmd)
    
    ssh.close_connection()