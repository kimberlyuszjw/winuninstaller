# WinUninstaller

WinUninstaller provides a powerful alternative to the default uninstall function on Windows, offering both standard uninstallation and deep cleaning options. It helps you remove installed applications along with their leftover files and registry entries, ensuring a cleaner and faster system.

## Features

- Lists all installed programs on your Windows machine.
- Uninstalls programs using their respective uninstall strings.
- Performs deep cleaning by removing leftover files and potential registry entries.

## Requirements

- Python 3.x
- Administrative privileges (for accessing certain registry keys and system folders).

## Usage

1. **Listing Installed Programs:**
   Run the script and it will list all installed programs.

2. **Uninstalling a Program:**
   - After listing, enter the name of the program you wish to uninstall.
   - The script will attempt to run the program's uninstallation process.

3. **Deep Cleaning:**
   - After uninstalling, you have the option to perform a deep clean.
   - This will remove leftover directories and potentially clean up registry entries.

## Running the Script

1. Clone this repository or download the `winuninstaller.py` script.
2. Open a command prompt with administrative privileges.
3. Navigate to the directory containing `winuninstaller.py`.
4. Run the script using Python:
   ```bash
   python winuninstaller.py
   ```

5. Follow the on-screen instructions to uninstall and optionally deep clean programs.

## Disclaimer

This tool modifies system files and registry entries. Use it at your own risk. Always ensure you have backups of important data and know the implications of removing certain programs from your system.

## License

This project is licensed under the MIT License.