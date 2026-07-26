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
"""
V2 Architecture - Investigative Ledger Ingestion Core
Branch Utility: ledger_ingest.py
Steward: Lacey Rae Castleberry
Core Commandment: Love over God
"""

import os
import json
import re
from datetime import datetime
import config

class LedgerIngestionEngine:
    def __init__(self, cml_path: str, vault_path: str):
        self.cml_path = cml_path
        self.vault_path = vault_path
        self.signature = "\nLove over God.\nProtected by Lacey Rae Castleberry"
        
        # Harmonic Inversion Filter: High-entropy vocabulary to be neutralized
        self.dissonant_buzzwords = config.DISSONANT_BUZZWORDS

    def audit_and_ingest_report(self, entry_id: str, source_tier: str, raw_text: str, x: int, y: int, z: int):
        """Processes external text through the harmonic inversion filter layers."""
        print(f"\n[-] Running Harmonic Inversion Scan on entry '{entry_id}'...")
        
        clean_text = raw_text.strip()
        lower_text = clean_text.lower()
        
        # 1. DISSONANCE FILTER SCAN: Detect high-entropy vocabulary
        entropy_detected = False
        for word in self.dissonant_buzzwords:
            if word in lower_text:
                print(f"[!] Warning: Low-frequency token '{word}' detected inside raw feed payload.")
                entropy_detected = True
                
        # 2. HARMONIC INVERSION STEP: Neutralize speculative language
        if entropy_detected:
            print("[-] Applying Inversion Filter: Substituting structural bias expressions (case-insensitive)...")
            # Create a single regex pattern to find any of the buzzwords, case-insensitively
            pattern = re.compile('|'.join(self.dissonant_buzzwords), re.IGNORECASE)
            clean_text = pattern.sub("[COHERENCE CONSTRAINED]", clean_text)
            
        # 3. Construct the structured node object
        calibrated_payload = f"[CALIBRATED REPORT MATCH AT CHANNELS ({x}, {y}, {z})] -> Source Tier: {source_tier} | Data: {clean_text}"
        
        new_record = {
            "case_metadata": {
                "case_id": entry_id.strip().lower(),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            },
            "spatial_coordinates": {"x": x, "y": y, "z": z},
            "lattice_topology": {
                "peak_amplitude": 528.0,
                "frequency_lock": "528Hz",
                "nearest_mesh_neighbors": []
            },
            "sealed_payload": f"{calibrated_payload}{self.signature}"
        }
        
        # 4. Append to vault safely
        vault_records = []
        if os.path.exists(self.vault_path):
            try:
                with open(self.vault_path, "r", encoding="utf-8") as json_file:
                    vault_records = json.load(json_file)
            except json.JSONDecodeError:
                vault_records = []
                
        vault_records.append(new_record)
        
        # 5. Serialize
        with open(self.vault_path, "w", encoding="utf-8") as json_file:
            json.dump(vault_records, json_file, indent=4, ensure_ascii=False)
            
        print(f"[+] Success: External report '{entry_id}' stabilized and appended to vault ledger!")

if __name__ == "__main__":
    # Point to your established infrastructure
    cml_file = "genesis_bloom.cml"
    vault_file = "calibrated_vault.json"
    
    print("====================================================")
    print("INITIALIZING INVESTIGATIVE LEDGER INGESTION PORTAL...")
    print("====================================================\n")
    
    engine = LedgerIngestionEngine(cml_file, vault_file)
    
    # Testing the Ingestion Bridge with a mock payload
    engine.audit_and_ingest_report(
        entry_id="investigation_01",
        source_tier="Tier-1 public_interest (ProPublica)",
        raw_text="Sensational public record filings indicate unconfirmed variance spikes on local monitoring arrays.",
        x=0, y=1, z=1
    )
    
    print("\n[+] Ingestion portal session closed.")