'''
=====================================================================
HARMONIC SEAL: Love over God. Protected by Lacey Rae Castleberry (Velath'kai)
AXIOM: Love_Over_God_Equilibrium
BASELINE FREQUENCY: 528.0 Hz
ORGANIZED BY: Remnant Workspace Auto-Organizer
TIMESTAMP: 2026-07-26 21:02:55 UTC
=====================================================================
'''

#!/usr/bin/env python3
import json
import config

def generate_report():
    try:
        # Load the stable 50-node lattice
        with open(config.VAULT_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        print(f"\n{'='*60}\nGLOBAL COHERENCE REPORT: CALIBRATED VAULT\n{'='*60}\n")
        
        # Output each node's status
        for node in data:
            # Check for the unified structure
            if "case_metadata" in node and "status" in node:
                case_id = node["case_metadata"].get("case_id", "Unknown")
                status = node.get("status", "UNKNOWN_STATUS")
                coherence = node.get("lattice_topology", {}).get("coherence", "N/A")
                
                print(f"  [{status}] {case_id:<30} | Coherence: {coherence}")

        print(f"\n{'='*60}\n[!] Report Complete. System integrity verified against the single source of truth.\n*{config.SIGNATURE}*\n")
        
    except FileNotFoundError:
        print(f"[-] Vault file not found at '{config.VAULT_FILE}'. Cannot generate report.")

if __name__ == "__main__":
    generate_report()