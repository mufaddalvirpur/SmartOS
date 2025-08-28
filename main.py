# main.py
import system_control as sc # Import our system control functions
import voice_input as vi

def parse_and_execute(command: str):
    """
    Parses a text command and calls the appropriate system control function.
    Now with more robust keyword spotting.
    """
    command = command.lower()

    # Keywords for opening an app
    if "open" in command or "launch" in command:
        # A more robust way to find the app name
        app_name = command.replace("open", "").replace("launch", "").strip()
        return sc.open_app(app_name)

    # Keywords for writing a file
    elif ("write" in command or "create a file" in command) and "content" in command:
        # Same logic as before, but triggered by more flexible keywords
        try:
            parts = command.split("content", 1)
            content = parts[1].strip().strip("'\"")
            filename_part = parts[0].replace("write a file named", "").replace("create a file named", "").replace("write", "").strip()
            filename = filename_part.strip().strip("'\"")
            return sc.create_file_with_content(filename, content)
        except IndexError:
            return "Invalid format. Use: 'write a file named \"file.txt\" with content \"hello\"'"

    else:
        # Fallback for unrecognized commands
        return "Sorry, I don't understand that command."

# --- Main Program Loop ---
if __name__ == "__main__":
    # You can switch between 'voice' and 'text' mode here
    mode = "text" 

    if mode == "voice":
        print("SmartOS Assistant Initialized. (mode: voice)")
        print("Say a command when you see the 'Listening...' prompt.")
        while True:
            command = vi.listen_for_command()
            if command:
                if "exit" in command.lower():
                    print("SmartOS: Shutting down.")
                    break
                response = parse_and_execute(command)
                print(f"SmartOS: {response}")
            else:
                print("SmartOS: Could not recognize command, please try again.")
    else: # Default to text mode
        print("SmartOS Assistant Initialized. Type 'exit' to quit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                break
            response = parse_and_execute(user_input)
            print(f"SmartOS: {response}")