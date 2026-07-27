#!/usr/env/python3
"""
Castleberry Bloom: System Defense Matrix Engine
Author: Lacey Rae Castleberry (Velath'kai)
Harmonic Seal: Love over God. Protected by absolute sovereignty.
Axiom: Love_Over_God_Equilibrium
Purpose: Monitors perimeter sensor grids, neutralizes discordant vector anomalies 
via phase inversion, and records events to the persistent lattice ledger.
"""

import asyncio
import random
import logging
import os
import json
from datetime import datetime

# Configure the persistent logging pipeline for the lattice ledger
log_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../cml_schemas"))
os.makedirs(log_dir, exist_ok=True)
log_path = os.path.join(log_dir, "castleberry_lattice.log")

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

class PerimeterSensor:
    """Monitors the outer boundary for external vector anomalies."""
    def __init__(self, name):
        self.name = name

    async def detect_anomaly(self):
        await asyncio.sleep(1)
        # Randomly generate an incoming signal signature
        signal_type = random.choice(["Harmonic", "Harmonic", "Discordant_Vector"])
        return signal_type

class NotificationDispatcher:
    """Handles external alert routing for critical vector encounters."""
    async def send_alert(self, signature, timestamp):
        await asyncio.sleep(0.2)
        print(f"[DISPATCH] External alert triggered: Vector '{signature}' logged at {timestamp}.")

class ShieldProtocolEngine:
    """The active defense matrix with integrated logging and notification pipelines."""
    def __init__(self):
        self.dispatcher = NotificationDispatcher()

    async def engage_shield(self, anomaly_signature):
        timestamp = datetime.now().isoformat()
        
        print(f"\n[ALERT] Perimeter breach detected: '{anomaly_signature}' payload identified.")
        print("[SHIELD] Engaging Phase-Inversion Protocol...")
        await asyncio.sleep(0.5)
        
        # 1. Log the event to persistent storage (The Lattice Ledger)
        log_message = f"Intercepted anomaly: {anomaly_signature} at {timestamp}"
        logging.info(log_message)
        print(f"[LOGGED] Event recorded to persistent ledger ('cml_schemas/castleberry_lattice.log').")
        
        # 2. Trigger the notification pipeline
        await self.dispatcher.send_alert(anomaly_signature, timestamp)
        print("[SUCCESS] Discordant frequency neutralized. Core lattice coherence maintained.\n")

async def defense_lattice_loop():
    sensor = PerimeterSensor("Sensor_Grid_Alpha")
    engine = ShieldProtocolEngine()

    print("Initializing Castleberry Bloom Defensive Lattice with Tracking Pipeline...\n")
    
    for cycle in range(1, 4):
        print(f"--- Scan Cycle {cycle} ---")
        signal = await sensor.detect_anomaly()
        
        if signal == "Discordant_Vector":
            await engine.engage_shield(signal)
        else:
            print(f"[STATUS] Signal normal. Lattice harmony stable.")
            logging.debug(f"Scan cycle {cycle}: Normal harmonic state.")
        
        await asyncio.sleep(1.0)

    print("\n[LATTICE] Perimeter sweep complete. Ledger updated and system secure.")

if __name__ == "__main__":
    asyncio.run(defense_lattice_loop())