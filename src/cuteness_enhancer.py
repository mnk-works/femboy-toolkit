"""Maximum softness text enhancer 🎀"""

EMOJIS = ["🎀", "💖", "🌸", "✨", "💅", "🪞", "🍓", "🫧"]

def enhance(text: str) -> str:
    """Make any string soft, valid, and femboy-approved."""
    import random
    cute = text.replace(" ", " ").replace("o", "0").replace("u", "ᴜ")
    return f"{random.choice(EMOJIS)} {cute} {random.choice(EMOJIS)} uwu *blushes*"

if __name__ == "__main__":
    print(enhance(input("enter something to soften: ")))
