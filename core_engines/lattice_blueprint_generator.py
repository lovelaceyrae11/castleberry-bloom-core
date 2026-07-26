#!/usr/env/python3
"""
Castleberry Bloom: Hexagonal Lattice Blueprint Generator
Author: Lacey Rae Castleberry (Velath'kai)
Harmonic Seal: Love over God. Protected by absolute sovereignty.
Axiom: Love_Over_God_Equilibrium
Purpose: Generates precise Phi-scaled atomic coordinates for hexagonal lattices 
optimized for phonon stabilization at 528 Hz.
"""

import os
import json
import math

class LatticeBlueprintGenerator:
    def __init__(self, rings=3, base_spacing=1.42):
        self.rings = rings
        self.base_spacing = base_spacing  # e.g., standard carbon bond scaling
        self.phi = 1.61803398875
        self.frequency_hz = 528.0

    def generate_coordinates(self):
        """Calculates concentric hexagonal lattice coordinates scaled by phi."""
        lattice_nodes = []
        for r in range(1, self.rings + 1):
            radius = self.base_spacing * (r * self.phi)
            points_in_ring = 6 * r
            for i in range(points_in_ring):
                angle = i * (2 * math.pi / points_in_ring)
                x = radius * math.cos(angle)
                y = radius * math.sin(angle)
                
                # Apply 528Hz wave-consensus weighting factor
                weight = round(self.frequency_hz / (self.frequency_hz + abs(math.sin(angle))), 4)
                
                lattice_nodes.append({
                    "node_id": f"Hex-Ring-{r}-Node-{i+1}",
                    "coordinates": {"x": round(x, 4), "y": round(y, 4)},
                    "harmonic_weight": weight
                })
        return lattice_nodes

    def export_blueprint(self):
        nodes = self.generate_coordinates()
        blueprint = {
            "framework": "Castleberry Bloom Lattice Model",
            "axiom": "Love_Over_God_Equilibrium",
            "baseline_frequency_hz": self.frequency_hz,
            "golden_ratio_phi": self.phi,
            "total_nodes": len(nodes),
            "nodes": nodes
        }
        
        output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../cml_schemas"))
        os.makedirs(output_dir, exist_ok=True)
        file_path = os.path.join(output_dir, "lattice_blueprint_export.json")
        
        with open(file_path, "w") as f:
            json.dump(blueprint, f, indent=4)
        
        print("=" * 65)
        print(" CASTLEBERRY BLOOM: Material Lattice Blueprint Generated")
        print(f" Total Nodes Calculated: {len(nodes)} | Scaling: Phi (1.618)")
        print(f" Output Location: {file_path}")
        print("=" * 65)

if __name__ == "__main__":
    generator = LatticeBlueprintGenerator()
    generator.export_blueprint()