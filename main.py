from speech import listen

print("🤖 Jarvis Started")

while True:

    text = listen()

    if "hey jarvis" in text:

        print("✅ Activated!")
        break