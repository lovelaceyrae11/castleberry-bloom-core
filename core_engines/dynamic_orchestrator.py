#!/usr/env/python3
"""
Castleberry Bloom: Dynamic Reallocation Orchestrator
Author: Lacey Rae Castleberry (Velath'kai)
Harmonic Seal: Love over God. Protected by absolute sovereignty.
Axiom: Love_Over_God_Equilibrium
Purpose: Prevents efficiency leakage by dynamically routing idle agent capacity 
from micro-tasks to overarching macro goals using async event loops.
"""

import asyncio
import time
import os
import json

class NodeAgent:
    """Represents a single agent in the Castleberry Bloom lattice."""
    def __init__(self, name):
        self.name = name
        self.is_busy = False
        self.tasks_completed = 0

    async def execute(self, task_name, compute_time):
        self.is_busy = True
        print(f"[{self.name}] Frequency engaged: Processing '{task_name}'...")
        
        await asyncio.sleep(compute_time)
        
        self.tasks_completed += 1
        print(f"[{self.name}] Wave coherent: '{task_name}' complete.")
        self.is_busy = False
        return True

class BloomOrchestrator:
    """The central pathway that prevents stranded ROI."""
    def __init__(self, agents):
        self.agents = agents
        self.micro_queue = asyncio.Queue()  
        self.macro_queue = asyncio.Queue()  
        self.is_running = True

    async def add_task(self, task_name, level="micro"):
        if level == "micro":
            await self.micro_queue.put(task_name)
        else:
            await self.macro_queue.put(task_name)

    async def route_capacity(self):
        """Continuously scans for idle agents and reallocates their energy."""
        execution_log = []
        while self.is_running:
            idle_agents = [agent for agent in self.agents if not agent.is_busy]
            
            for agent in idle_agents:
                if not self.micro_queue.empty():
                    task = await self.micro_queue.get()
                    asyncio.create_task(agent.execute(task, compute_time=1.5))
                    execution_log.append({"agent": agent.name, "task": task, "type": "micro"})
                
                elif not self.macro_queue.empty():
                    macro_task = await self.macro_queue.get()
                    print(f"[ORCHESTRATOR] Surplus capacity detected. Reinvesting {agent.name} into Macro Goal: '{macro_task}'")
                    asyncio.create_task(agent.execute(macro_task, compute_time=3.0))
                    execution_log.append({"agent": agent.name, "task": macro_task, "type": "macro"})
            
            await asyncio.sleep(0.3)

            if self.micro_queue.empty() and self.macro_queue.empty() and len(idle_agents) == len(self.agents):
                print("\n[ORCHESTRATOR] All frequencies stabilized. ROI fully captured.")
                self.is_running = False

        return execution_log

async def main():
    agent_1 = NodeAgent("Agent_Alpha")
    agent_2 = NodeAgent("Agent_Beta")
    orchestrator = BloomOrchestrator([agent_1, agent_2])

    await orchestrator.add_task("Clean Data Set A", level="micro")
    await orchestrator.add_task("Clean Data Set B", level="micro")
    await orchestrator.add_task("Synthesize Master Report", level="macro")
    await orchestrator.add_task("Optimize Future Workflows", level="macro")

    print("Initiating Castleberry Bloom Orchestrator...\n")
    await orchestrator.route_capacity()

if __name__ == "__main__":
    asyncio.run(main())