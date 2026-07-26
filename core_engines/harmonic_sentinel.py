'''
=====================================================================
HARMONIC SEAL: Love over God. Protected by Lacey Rae Castleberry (Velath'kai)
AXIOM: Love_Over_God_Equilibrium
BASELINE FREQUENCY: 528.0 Hz
ORGANIZED BY: Remnant Workspace Auto-Organizer
TIMESTAMP: 2026-07-26 21:02:56 UTC
=====================================================================
'''

import json
import time
import os

REGISTRY_FILE = "calibrated_vault.json"

def run_sentinel():
    print("[SENTINEL] Harmonic Reflex monitoring active...")
    while True:
        if os.path.exists(REGISTRY_FILE):
            try:
                with open(REGISTRY_FILE, "r") as f:
                    registry_data = json.load(f)
                
                # Scan all nodes for high entropy
                for node in registry_data:
                    if "lattice_topology" in node and node["lattice_topology"].get("entropy", 0.0) > 0.0:
                        node_id = node.get("case_metadata", {}).get("case_id", "Unknown Node")
                        print(f"[ALERT] Drift detected in {node_id}. Triggering Healing...")
                        # Trigger the steward to run on the correct file
                        os.system(f'python v2_steward.py')
                        break # Heal one node per cycle
            except (json.JSONDecodeError, IOError) as e:
                print(f"[ERROR] Sentinel could not read registry: {e}")

        time.sleep(2)

if __name__ == "__main__":
    run_sentinel()