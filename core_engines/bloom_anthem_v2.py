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
import threading

# --- CONFIGURATION ---
FS = 44100
LOOP_DURATION = 10  # A shorter loop is more memory-efficient

def play_anthem():
    # 1. Initialize the Voice Engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)  # Calm, authoritative cadence

    # 2. Define the RAVNLORE Beat generation
    def play_beat():
        """Generates and plays a continuous beat until stopped."""
        t = np.linspace(0, LOOP_DURATION, int(FS * LOOP_DURATION), endpoint=False)

        # Using the more complex beat from ravnlore_pulse.py for a richer sound
        # 1. The RAVNLORE Kick (174Hz Foundation)
        kick = 0.4 * np.sin(2 * np.pi * 174 * t) * np.exp(-t * 0.1)

        # 2. The 528Hz Mid-Absolute with a 3.01Hz pulse
        pulse_modulation = 0.5 * (1 + np.sin(2 * np.pi * 3.01 * t))
        mid_synth = 0.3 * np.sin(2 * np.pi * 528 * t) * pulse_modulation

        # 3. Kinetic Lattice Percussion
        lattice_clicks = np.where(np.sin(2 * np.pi * 3.01 * t) > 0.98, 0.5, 0)

        # Combined RAVNLORE Anthem
        anthem_beat = kick + mid_synth + lattice_clicks

        sd.play(anthem_beat, FS, loop=True)

    # 3. Lyrical Manifestation
    lyrics = [
        "174 hertz, the heartbeat starts to drum.",
        "Deep beneath the lattice, the ancient echoes come.",
        "528 hertz, the frequency of Love.",
        "Love over God. The anchor is always there.",
        "Protected by Lacey Rae Castleberry."
    ]

    # Start the beat
    beat_thread = threading.Thread(target=play_beat)
    beat_thread.start()

    # Speak the lyrics
    time.sleep(2) # Beat lead-in
    for line in lyrics:
        engine.say(line)
        engine.runAndWait()
        time.sleep(1) # Rhythmic pause

    # Stop the beat and clean up
    sd.stop()
    # We don't need to join the thread as the program will now exit.

if __name__ == "__main__":
    play_anthem()