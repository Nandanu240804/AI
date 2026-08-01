import cv2
import numpy as np
import mss
import os
from datetime import datetime


def record_screen(duration=5, fps=20):

    os.makedirs("recordings", exist_ok=True)

    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".mp4"
    filepath = os.path.join("recordings", filename)

    with mss.mss() as sct:

        monitor = sct.monitors[1]

        width = monitor["width"]
        height = monitor["height"]

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")

        out = cv2.VideoWriter(
            filepath,
            fourcc,
            fps,
            (width, height)
        )

        total_frames = duration * fps

        print("🎥 Recording...")

        for _ in range(total_frames):

            img = sct.grab(monitor)

            frame = np.array(img)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

            out.write(frame)

        out.release()

    print(f"✅ Recording saved:\n{filepath}")