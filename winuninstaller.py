import os
import subprocess
import shutil
import winreg

class WinUninstaller:
    def __init__(self):
        self.installed_programs = self.get_installed_programs()

    def get_installed_programs(self):
        programs = {}
        registry_paths = [
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
            r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
        ]
        
        for reg_path in registry_paths:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path) as key:
                for i in range(winreg.QueryInfoKey(key)[0]):
                    subkey_name = winreg.EnumKey(key, i)
                    with winreg.OpenKey(key, subkey_name) as subkey:
                        try:
                            display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                            uninstall_string = winreg.QueryValueEx(subkey, "UninstallString")[0]
                            programs[display_name] = uninstall_string
                        except FileNotFoundError:
                            continue
        return programs

    def list_programs(self):
        print("Installed Programs:")
        for program in self.installed_programs:
            print(f"- {program}")

    def uninstall_program(self, program_name):
        if program_name not in self.installed_programs:
            print(f"Program '{program_name}' not found.")
            return

        uninstall_string = self.installed_programs[program_name]
        print(f"Uninstalling {program_name}...")

        try:
            subprocess.run(uninstall_string, shell=True, check=True)
            print(f"Successfully uninstalled {program_name}.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to uninstall {program_name}. Error: {e}")

    def deep_clean(self, program_name):
        if program_name not in self.installed_programs:
            print(f"Program '{program_name}' not found.")
            return

        print(f"Performing deep clean for {program_name}...")

        # Assuming the deep clean involves removing leftover files and registry entries
        leftovers = [
            os.path.join("C:\\Program Files", program_name),
            os.path.join("C:\\Program Files (x86)", program_name),
            os.path.join("C:\\Users", os.getenv("USERNAME"), "AppData", "Roaming", program_name),
            os.path.join("C:\\Users", os.getenv("USERNAME"), "AppData", "Local", program_name)
        ]

        for path in leftovers:
            if os.path.exists(path):
                try:
                    shutil.rmtree(path)
                    print(f"Removed leftover files at {path}")
                except Exception as e:
                    print(f"Error removing {path}: {e}")

        # Placeholder for removing registry entries (requires specific keys)
        print(f"Deep clean for {program_name} completed.")

if __name__ == "__main__":
    uninstaller = WinUninstaller()
    uninstaller.list_programs()
    
    program_to_uninstall = input("Enter the name of the program to uninstall: ")
    uninstaller.uninstall_program(program_to_uninstall)

    deep_clean_choice = input("Do you want to perform a deep clean? (yes/no): ").strip().lower()
    if deep_clean_choice == 'yes':
        uninstaller.deep_clean(program_to_uninstall)