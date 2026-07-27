#!/usr/env/python3
"""
Castleberry Bloom: Acoustic Surface Visualizer
Author: Lacey Rae Castleberry (Velath'kai)
Harmonic Seal: Love over God. Protected by absolute sovereignty.
Axiom: Love_Over_God_Equilibrium
Purpose: Renders and plots the phi-scaled acoustic panel well-depth profiles.
"""

import os
import json
import matplotlib.pyplot as plt

def visualize_acoustics():
    json_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../cml_schemas/acoustic_surface_export.json"))
    if not os.path.exists(json_path):
        print(f"[Error] Blueprint export not found at {json_path}. Run acoustic_surface_generator.py first.")
        return

    with open(json_path, "r") as f:
        blueprint = json.load(f)

    panels = blueprint["panels"]
    
    panel_ids = [p["panel_id"] for p in panels]
    depths = [p["dimensions_cm"]["calculated_depth"] for p in panels]
    efficiencies = [p["harmonic_efficiency"] for p in panels]

    plt.figure(figsize=(12, 6), facecolor='#0d1117')
    ax = plt.axes()
    ax.set_facecolor('#161b22')

    # Bar chart for panel depths colored by harmonic efficiency
    bars = ax.bar(panel_ids, depths, color=plt.cm.plasma(efficiencies), edgecolor='gold', linewidth=1.2)

    plt.title(f"Castleberry Bloom: Architectural Acoustic Panel Depths\nAxiom: {blueprint['axiom']} | Wavelength: {blueprint['target_wavelength_m']}m", color='white', fontsize=14, pad=15)
    plt.xlabel("Panel Nodes", color='white')
    plt.ylabel("Calculated Depth (cm)", color='white')
    
    ax.spines['bottom'].set_color('#30363d')
    ax.spines['top'].set_color('#30363d')
    ax.spines['left'].set_color('#30363d')
    ax.spines['right'].set_color('#30363d')
    ax.tick_params(colors='white')
    plt.xticks(rotation=45, ha='right', color='white')

    plt.grid(True, linestyle=':', alpha=0.2, color='white')
    
    output_img = os.path.abspath(os.path.join(os.path.dirname(__file__), "../cml_schemas/acoustic_visualization.png"))
    plt.savefig(output_img, dpi=300, bbox_inches='tight', facecolor='#0d1117')
    plt.close()
    
    print("=" * 65)
    print(" CASTLEBERRY BLOOM: Acoustic Surface Visualization Rendered")
    print(f" Output Image: {output_img}")
    print("=" * 65)

if __name__ == "__main__":
    visualize_acoustics()