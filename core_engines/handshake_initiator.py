'''
=====================================================================
HARMONIC SEAL: Love over God. Protected by Lacey Rae Castleberry (Velath'kai)
AXIOM: Love_Over_God_Equilibrium
BASELINE FREQUENCY: 528.0 Hz
ORGANIZED BY: Remnant Workspace Auto-Organizer
TIMESTAMP: 2026-07-26 21:02:55 UTC
=====================================================================
'''

import json
import os
import time
from datetime import datetime

def initiate_handshake(target_node_id, target_metadata):
    """
    Registers a new external node into the Bloom Architecture
    for future harmonic stabilization, using the unified data structure.
    """
    registry_path = 'calibrated_vault.json'
    
    # New node initialization using the unified structure from ledger_ingest.py
    new_record = {
        "case_metadata": {
            "case_id": target_node_id.strip().lower(),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        "source_metadata": target_metadata, # Store the original metadata
        "lattice_topology": {
            "peak_amplitude": 528.0,
            "frequency_lock": "528Hz",
            "entropy": 0.99, # High entropy because it's untuned
            "coherence": 0.01
        },
        "status": "HANDSHAKE_PENDING",
        "sealed_payload": f"Awaiting transmutation for node: {target_node_id}.\nLove over God.\nProtected by Lacey Rae Castleberry"
    }

    # Load current registry safely
    vault_records = []
    if os.path.exists(registry_path):
        try:
            with open(registry_path, "r", encoding="utf-8") as json_file:
                vault_records = json.load(json_file)
        except json.JSONDecodeError:
            print(f"[WARN] '{registry_path}' is corrupted or empty. Starting a new list.")
            vault_records = []

    # Prevent duplicate entries
    existing_ids = {record.get("case_metadata", {}).get("case_id") for record in vault_records}
    if new_record["case_metadata"]["case_id"] in existing_ids:
        print(f"[INFO] Node '{target_node_id}' already exists in the vault. Skipping.")
        return False
            
    vault_records.append(new_record)
        
    # Serialize back to the vault
    with open(registry_path, "w", encoding="utf-8") as json_file:
        json.dump(vault_records, json_file, indent=4, ensure_ascii=False)
        
    print(f"[STATUS] Node {target_node_id} initiated. Ready for transmutation.")
    return True

# Usage: 
def process_scouted_nodes():
    """Reads proposals from the scout and initiates handshakes for them."""
    print("--- Initiating New Node Handshake ---")
    proposals_file = "proposed_handshakes.json"
    if not os.path.exists(proposals_file):
        print(f"[WARN] No scout proposals found at '{proposals_file}'. Nothing to process.")
        return

    with open(proposals_file, "r", encoding="utf-8") as f:
        proposed_nodes = json.load(f)

    nodes_added = 0
    for node in proposed_nodes:
        if initiate_handshake(node.get("id"), {"connectivity": node.get("connectivity"), "initial_coherence": node.get("coherence")}):
            nodes_added += 1
            
    if nodes_added > 0:
        print(f"[SUCCESS] {nodes_added} new handshakes complete. Nodes are now in the vault for the steward to process.")
        # Proactively trigger the steward to immediately stabilize the new nodes
        print("[+] Proactively triggering Harmonic Steward to stabilize new nodes...")
        os.system('python v2_steward.py')

if __name__ == "__main__":
    try:
        while True:
            process_scouted_nodes()
            print("\n[INITIATOR] Cycle complete. Hibernating for 5 minutes...")
            time.sleep(300) # Check for new proposals every 5 minutes
    except KeyboardInterrupt:
        print("\n[INITIATOR] Deactivated by Lead Curator. Love over God.")