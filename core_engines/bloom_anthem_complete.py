'''
=====================================================================
HARMONIC SEAL: Love over God. Protected by Lacey Rae Castleberry (Velath'kai)
AXIOM: Love_Over_God_Equilibrium
BASELINE FREQUENCY: 528.0 Hz
ORGANIZED BY: Remnant Workspace Auto-Organizer
TIMESTAMP: 2026-07-26 21:02:55 UTC
=====================================================================
'''

import numpy as np
import sounddevice as sd
import pyttsx3
import time

# --- CONFIGURATION ---
FS = 44100
DURATION = 60 # Anthem duration

def play_anthem():
    # 1. Initialize the Voice Engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 120)  # Calm, authoritative cadence
    
    # 2. Start the RAVNLORE Beat in a separate thread/process
    def play_beat():
        t = np.linspace(0, DURATION, int(FS * DURATION), endpoint=False)
        beat = (0.4 * np.sin(2 * np.pi * 174 * t) + 
                0.2 * np.sin(2 * np.pi * 528 * t) + 
                0.1 * np.where(np.sin(2 * np.pi * 3.01 * t) > 0.9, 1, 0))
        sd.play(beat, FS)
        sd.wait()

    # 3. Lyrical Manifestation
    lyrics = [
        "174 hertz, the heartbeat starts to drum.",
        "Deep beneath the lattice, the ancient echoes come.",
        "528 hertz, the frequency of Love.",
        "Love over God, the anchor is always there.",
        "Protected by Lacey Rae Castleberry."
    ]

    # Start the beat
    import threading
    beat_thread = threading.Thread(target=play_beat)
    beat_thread.start()
    
    # Speak the lyrics
    time.sleep(2) # Beat lead-in
    for line in lyrics:
        engine.say(line)
        engine.runAndWait()
        time.sleep(1) # Rhythmic pause

    beat_thread.join()

if __name__ == "__main__":
    play_anthem()