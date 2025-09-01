"""
ascii_art.py
Holds ASCII art stages for the Snowman game.
"""

STAGES = [
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
    """,  # Stage 0: full snowman

    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : )
    """,  # Stage 1: legs intact, starting melt

    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
    """,  # Stage 2: legs gone

    """
      ___  
     /___\\ 
     (o o) 
     (   ) 
    """,  # Stage 3: belly melting

    """
      ___  
     /___\\ 
     (o o) 
    """,  # Stage 4: only head remains

    """
      ___  
     /___\\ 
    """,  # Stage 5: melted, game over
]
