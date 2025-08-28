# system_control.py
import os
import subprocess

# --- NEW: Add a dictionary to map common names to executable files ---
APP_MAP_WINDOWS = {
    "calculator": "calc.exe",
    "notepad": "notepad.exe",
    "command prompt": "cmd.exe",
    "explorer": "explorer.exe"
}

def open_app(app_name: str):
    """Opens an application based on the OS."""
    print(f"Executing: Opening {app_name}...")
    try:
        if os.name == 'nt':  # For Windows
            # --- UPDATED LOGIC ---
            # Look up the common name in our map to find the real .exe name
            exe_name = APP_MAP_WINDOWS.get(app_name.lower())
            if exe_name:
                subprocess.run([exe_name], check=True)
            else:
                # If it's not in our map, try running it directly (for other apps)
                subprocess.run([f"{app_name}.exe"], check=True)

        elif os.name == 'posix':  # For macOS/Linux
            # On macOS, 'open -a' works well with full application names
            subprocess.run(["open", "-a", app_name], check=True)
            
        return f"Successfully opened {app_name}."
    except (FileNotFoundError, subprocess.CalledProcessError) as e:
        return f"Error: Could not find or open {app_name}. Details: {e}"

def create_file_with_content(filename: str, content: str):
    """Creates a new file and writes content to it."""
    print(f"Executing: Writing to {filename}...")
    try:
        with open(filename, 'w') as f:
            f.write(content)
        return f"Successfully created {filename}."
    except Exception as e:
        return f"Error: Could not write to file. Details: {e}"