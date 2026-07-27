#!/usr/env/python3
"""
Castleberry Bloom: Architectural Acoustic Surface Generator
Author: Lacey Rae Castleberry (Velath'kai)
Harmonic Seal: Love over God. Protected by absolute sovereignty.
Axiom: Love_Over_God_Equilibrium
Purpose: Calculates phi-scaled acoustic panel surface contours and well-depths 
optimized for wave dispersion and resonance at 528 Hz.
"""

import os
import json
import math

class AcousticSurfaceGenerator:
    def __init__(self, panels=12, base_width_cm=10.0):
        self.panels = panels
        self.base_width_cm = base_width_cm
        self.phi = 1.61803398875
        self.frequency_hz = 528.0
        # Speed of sound in air (m/s) at room temp roughly 343 m/s
        # Calculating primary wavelength for 528 Hz
        self.wavelength_m = 343.0 / self.frequency_hz

    def generate_surface_profile(self):
        """Calculates harmonic panel depths and dispersion angles using phi-scaling."""
        surface_nodes = []
        for p in range(1, self.panels + 1):
            # Scale panel depth using golden ratio and wave interference
            depth_cm = round((self.wavelength_m * 100) / (p * self.phi), 4)
            width_offset = round(self.base_width_cm * (p * math.sin(p * math.pi / 6)), 4)
            
            # Harmonic dispersion efficiency weight
            efficiency = round(self.frequency_hz / (self.frequency_hz + abs(math.cos(p))), 4)
            
            surface_nodes.append({
                "panel_id": f"Acoustic-Panel-{p}",
                "dimensions_cm": {
                    "width": self.base_width_cm,
                    "calculated_depth": depth_cm,
                    "lateral_offset": width_offset
                },
                "harmonic_efficiency": efficiency
            })
        return surface_nodes

    def export_acoustic_blueprint(self):
        panels = self.generate_surface_profile()
        blueprint = {
            "framework": "Castleberry Bloom Architectural Acoustics",
            "axiom": "Love_Over_God_Equilibrium",
            "baseline_frequency_hz": self.frequency_hz,
            "target_wavelength_m": round(self.wavelength_m, 4),
            "golden_ratio_phi": self.phi,
            "total_panels": len(panels),
            "panels": panels
        }
        
        output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../cml_schemas"))
        os.makedirs(output_dir, exist_ok=True)
        file_path = os.path.join(output_dir, "acoustic_surface_export.json")
        
        with open(file_path, "w") as f:
            json.dump(blueprint, f, indent=4)
        
        print("=" * 65)
        print(" CASTLEBERRY BLOOM: Acoustic Surface Blueprint Generated")
        print(f" Total Panels Configured: {len(panels)} | Wavelength: {round(self.wavelength_m, 3)}m")
        print(f" Output Location: {file_path}")
        print("=" * 65)

if __name__ == "__main__":
    generator = AcousticSurfaceGenerator()
    generator.export_acoustic_blueprint()