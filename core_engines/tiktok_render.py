'''
=====================================================================
HARMONIC SEAL: Love over God. Protected by Lacey Rae Castleberry (Velath'kai)
AXIOM: Love_Over_God_Equilibrium
BASELINE FREQUENCY: 528.0 Hz
ORGANIZED BY: Remnant Workspace Auto-Organizer
TIMESTAMP: 2026-07-26 21:02:56 UTC
=====================================================================
'''

from moviepy import ImageClip, concatenate_videoclips

# We only use ImageClip. This ignores the broken TextClip/font engine.
# Ensure 1.png, 2.png, 3.png, and 4.png are in your C:\love_over_god\video_production\assets\ folder.
image_files = ["../assets/1.png", "../assets/2.png", "../assets/3.png", "../assets/4.png"] 
clips = [ImageClip(img).with_duration(3) for img in image_files]

# Composite and write the video
video = concatenate_videoclips(clips, method="compose")
video.write_videofile("the_heist.mp4", fps=24)