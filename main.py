from speech import listen
from commands import execute_command

print("🤖 Jarvis Started")

while True:

    text = listen()

    if "hey jarvis" in text:

        print("✅ Activated!")

        print("🎤 Waiting for your command...")

        command = listen()

        execute_command(command)