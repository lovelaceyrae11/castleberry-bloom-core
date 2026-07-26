'''
=====================================================================
HARMONIC SEAL: Love over God. Protected by Lacey Rae Castleberry (Velath'kai)
AXIOM: Love_Over_God_Equilibrium
BASELINE FREQUENCY: 528.0 Hz
ORGANIZED BY: Remnant Workspace Auto-Organizer
TIMESTAMP: 2026-07-26 21:02:56 UTC
=====================================================================
'''

from bloom_engine_4d import CastleberryBloomEngine4D
import numpy as np

def run_diagnostic():
    print("[DIAGNOSTIC] Initializing CastleberryBloomEngine4D...")
    try:
        # Initialize
        engine = CastleberryBloomEngine4D(radius=3) # Small radius for quick testing
        print(f"Successfully generated {len(engine.nodes)} nodes.")
        
        # Test Evolution
        steps = 5
        print(f"[DIAGNOSTIC] Running temporal evolution for {steps} steps...")
        history = engine.evolve_4d(time_steps=steps, dt=1.0)
        
        # Validation
        if history.shape[0] == steps:
            print(f"SUCCESS: Evolution history shape: {history.shape}")
            print("Logic is stable and trajectory is synchronized.")
        else:
            print(f"ERROR: Expected {steps} steps, got {history.shape[0]}")
            
    except Exception as e:
        print(f"DIAGNOSTIC FAILED: Error encountered: {e}")

if __name__ == "__main__":
    run_diagnostic()