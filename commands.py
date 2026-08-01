from screenshot import take_screenshot


def execute_command(command):

    command = command.lower()

    if "screenshot" in command:
        take_screenshot()

    else:
        print("❌ Unknown command")