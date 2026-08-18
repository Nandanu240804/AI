from speech import listen
from commands import execute_command

print("🤖 Jarvis Started")

while True:

    text = listen()

    if "hey jarvis" in text:

        print("✅ Activated!")

        while True:

            command = listen()

            if command == "":
                continue

            if "goodbye" in command or "exit" in command:
                print("👋 Jarvis going back to sleep...")
                break

            execute_command(command)