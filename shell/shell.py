import os
import subprocess
import threading

command_history = []
aliases = {}

def execute_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode(), error.decode(), process.returncode

def run_background(command):
    threading.Thread(target=lambda: os.system(command)).start()

while True:
    user_input = input("$ ")

    if user_input.lower() == "exit":
        break

    command_parts = user_input.split()
    command = command_parts[0]
    arguments = command_parts[1:]

    try:
        if command == "cd":
            if arguments:
                os.chdir(arguments[0])
            else:
                print("Usage: cd <directory>")
        elif command == "ls":
            result = os.listdir()
            print("\n".join(result))
        elif command == "alias":
            if len(arguments) >= 2:
                aliases[arguments[0]] = " ".join(arguments[1:])
                print(f"Alias '{arguments[0]}' created.")
            else:
                print("Usage: alias <alias_name> <command>")
        elif command in aliases:
            full_command = aliases[command] + " " + " ".join(arguments)
            output, error, result_code = execute_command(full_command)
            if error:
                print(f"Error: {error}")
            if output:
                print(output)
        elif "&" in arguments:
            arguments.remove("&")
            background_command = " ".join([command] + arguments)
            run_background(background_command)
        else:
            output, error, result_code = execute_command(user_input)
            if error:
                print(f"Error: {error}")
            if output:
                print(output)
            
        command_history.append(user_input)
    except Exception as e:
        print(f"Error executing '{user_input}': {e}")
