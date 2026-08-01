import pyautogui
import os
from datetime import datetime


def take_screenshot():

    # Create folder if it doesn't exist
    os.makedirs("screenshots", exist_ok=True)

    # Create filename with timestamp
    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"

    filepath = os.path.join("screenshots", filename)

    # Take screenshot
    pyautogui.screenshot(filepath)

    print(f"📸 Screenshot saved: {filepath}")