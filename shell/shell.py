import os

while True:
    # Display a prompt
    user_input = input("$ ")

    # Exit the shell if the user types "exit"
    if user_input.lower() == "exit":
        break

    # Split the user input into command and arguments
    command_parts = user_input.split()
    command = command_parts[0]
    arguments = command_parts[1:]

    try:
        # Run the command
        result = os.system(user_input)
        if result != 0:
            print(f"Command '{command}' failed with exit code {result}")
    except Exception as e:
        print(f"Error executing '{user_input}': {e}")
