from screenshot import take_screenshot
from screen_recorder import ScreenRecorder


# Create one recorder instance for the entire application
recorder = ScreenRecorder()


def execute_command(command):

    command = command.lower().strip()

    # Screenshot commands
    if "screenshot" in command or "screen shot" in command:
        take_screenshot()
        return

    # Start recording commands
    if (
        "start screen recording" in command
        or "start recording" in command
        or "begin recording" in command
    ):
        recorder.start()
        return

    # Stop recording commands
    if (
        "stop screen recording" in command
        or "stop recording" in command
        or "end recording" in command
    ):
        recorder.stop()
        return

    print(f"❌ Unknown command: {command}")