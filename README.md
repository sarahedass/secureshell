# SecureShell

SecureShell is a Python application designed to improve security for remote desktop operations on Windows by implementing enhanced encryption and authentication mechanisms using the SSH protocol.

## Features

- Connect to remote systems securely over SSH using Paramiko.
- Execute shell commands remotely with encrypted SSH sessions.
- Auto-add host keys for a seamless connection experience.
- Logging for connection attempts, command executions, and errors.

## Prerequisites

- Python 3.x
- Paramiko library

Install Paramiko using pip:

```bash
pip install paramiko
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/SecureShell.git
cd SecureShell
```

2. Run the script:

```bash
python SecureShell.py
```

3. Follow the prompts to enter the remote host address, port, username, and password.

4. Enter commands to execute on the remote server. Type `exit` to close the connection.

## Security Considerations

- Ensure that your SSH server is configured properly and uses a strong password or key-based authentication.
- Be cautious about executing commands remotely, as they can affect the remote system's integrity and security.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## Support

For any issues or support needed, please open an issue on the GitHub repository.