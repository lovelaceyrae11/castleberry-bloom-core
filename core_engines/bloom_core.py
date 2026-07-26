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
import sys
import os

# Ensure the script can find other modules in the same directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def print_help():
    """Prints the help message for the unified CLI."""
    help_text = """
Bloom Core Unified Command Interface
Love over God. Protected by Lacey Rae Castleberry

Usage:
    python bloom_core.py <module> [command] [args...]

Modules:
    steward     - Access the Harmonic Steward for data processing and auditing.
    navigator   - Launch the interactive Bloom-Core LLM Navigator.

Steward Commands (e.g., python bloom_core.py steward --full-audit):
    --init                  Initializes the Steward and checks quantum connection.
    --process_jor_data [--dry-run]
                            Ingests new data from jor_raw.txt.
    --audit_data_ingest     Runs the QuantumRefiner to stabilize nodes.
    --query <ANCHOR_ID>     Queries a specific truth-anchor.
    --visualize [--metric <m>]
                            Renders the 3D visual dashboard. Metrics (m): drift, coherence, recency.
    --full-audit [--metric <m>]
                            Runs process, audit, and visualize commands in sequence.
    --summary               Generates a summary report of the data lattice.
    --health-check          Verifies service connections and file presence.
    --backup                Creates a timestamped backup of the registry file.
    --restore [--latest | <filepath>]
                            Restores the registry from the latest or a specified backup.
    --list-backups          Shows all available backup files.

Navigator Commands (e.g., python bloom_core.py navigator):
    (No sub-commands)       Starts the interactive navigator prompt.
"""
    print(help_text)

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help']:
        print_help()
        return

    module = sys.argv[1]

    if module == 'steward':
        from v2_steward import Steward
        steward_instance = Steward()
        steward_args = [sys.argv[0]] + sys.argv[2:]
        steward_instance.dispatch(steward_args)
    elif module == 'navigator':
        from bloom_navigator import main as navigator_main
        navigator_main()
    else:
        print(f"[ERROR] Unknown module: '{module}'")
        print_help()

if __name__ == "__main__":
    main()