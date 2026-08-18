import cv2
import numpy as np
import mss
import os
import threading
from datetime import datetime


class ScreenRecorder:

    def __init__(self, fps=20):

        self.fps = fps
        self.recording = False
        self.thread = None
        self.writer = None

    def start(self):

        if self.recording:
            print("⚠ Already recording.")
            return

        self.recording = True

        self.thread = threading.Thread(target=self._record)

        self.thread.start()

    def stop(self):

        if not self.recording:
            print("⚠ Recorder is not running.")
            return

        self.recording = False

        self.thread.join()

        print("✅ Recording stopped.")

    def _record(self):

        os.makedirs("recordings", exist_ok=True)

        filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".mp4"

        filepath = os.path.join("recordings", filename)

        with mss.mss() as sct:

            monitor = sct.monitors[1]

            width = monitor["width"]
            height = monitor["height"]

            fourcc = cv2.VideoWriter_fourcc(*"mp4v")

            self.writer = cv2.VideoWriter(
                filepath,
                fourcc,
                self.fps,
                (width, height)
            )

            print("🎥 Recording Started...")

            while self.recording:

                img = sct.grab(monitor)

                frame = np.array(img)

                frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

                self.writer.write(frame)

            self.writer.release()

        print(f"💾 Saved to: {filepath}")