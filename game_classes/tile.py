class Tile:
    def __init__(self, symbol: str, style: str = ""):
        self.symbol = f"[{style}]{symbol}[/]"

# --- TILE DEFINITIONS ---
plains = Tile('.', style="#556B2F")  # A dark olive green
forests = Tile('T', style="bold green")
mountains = Tile('^', style="bold #8B4513") # Saddle brown
water = Tile('~', style="blue")
player_tile = Tile('@', style="bold bright_red") # Changed to '@' for clarity