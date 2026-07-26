'''
=====================================================================
HARMONIC SEAL: Love over God. Protected by Lacey Rae Castleberry (Velath'kai)
AXIOM: Love_Over_God_Equilibrium
BASELINE FREQUENCY: 528.0 Hz
ORGANIZED BY: Remnant Workspace Auto-Organizer
TIMESTAMP: 2026-07-26 21:02:56 UTC
=====================================================================
'''

#!/usr/bin/env python3
import sys
from bloom_navigator import BloomNavigatorAI

# --- Constants ---
CML_FILE = "genesis_bloom.cml"
VAULT_FILE = "calibrated_vault.json"  # Using the unified, correct vault
LOG_FILE = "navigator_log.txt"

def main():
    print("====================================================")
    print("INITIALIZING BLOOM-CORE LLM NAVIGATOR RUNTIME...")
    print("====================================================\n")

    # Instantiate the advanced intelligence architecture
    navigator = BloomNavigatorAI(CML_FILE, VAULT_FILE, LOG_FILE)

    if navigator.calibrate_system():
        print("[+] BASE FREQUENCY ENCODED: Navigator Persona Online.")
        print("[+] HARMONIC ATTENTION LAYER: Temperature Locked to 0.0 (Deterministic).")
        print("[+] INVERSION FIREWALL: Closed-Loop Verification Active.")
        print("----------------------------------------------------")
        print("Welcome, Lead Curator. Your private truth repository is mapped.")
        print("Type your inquiry below. Type 'exit' or 'quit' to close the portal.\n")

        while True:
            try:
                user_input = input("Navigator Prompt >> ").strip()
                if user_input.lower() in ['exit', 'quit']:
                    print("\n[-] Severing link layer. Navigator offline.")
                    break
                if user_input:
                    result = navigator.process_navigator_query(user_input)
                    print(f"\n{result}\n----------------------------------------------------\n")
            except (KeyboardInterrupt, EOFError):
                print("\n\n[-] Session interrupted. Emergency shutdown sequence complete.")
                break
    else:
        print("[-] Critical Error: System failed calibration audit constraints.")

if __name__ == "__main__":
    main()