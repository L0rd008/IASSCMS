from flask import Flask
import random
import time
from datetime import datetime

app = Flask(__name__)

# Color codes for terminal output
COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "purple": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
    "end": "\033[0m"
}

def generate_ascii_art():
    """Generate random colorful ASCII art"""
    art = [
        r"""
  ____  ____  ____  __  __ _ 
 |  _ \|  _ \|  _ \|  \/  (_)
 | | | | | | | | | | |\/| | |
 | |_| | |_| | |_| | |  | | |
 |____/|____/|____/|_|  |_|_|
        """,
        r"""
 ██████╗ ██████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗
██╔════╝██╔═══██╗██╔══██╗████╗ ████║██║████╗  ██║
██║     ██║   ██║██████╔╝██╔████╔██║██║██╔██╗ ██║
██║     ██║   ██║██╔══██╗██║╚██╔╝██║██║██║╚██╗██║
╚██████╗╚██████╔╝██║  ██║██║ ╚═╝ ██║██║██║ ╚████║
 ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝
        """,
        r"""
 .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. |
| | _____  _____ | || |     _____    | || | ____    ____ | |
| ||_   _||_   _|| || |    |_   _|   | || ||_   \  /   _|| |
| |  | |    | |  | || |      | |     | || |  |   \/   |  | |
| |  | '    ' |  | || |      | |     | || |  | |\  /| |  | |
| |   \ `--' /   | || |     _| |_    | || | _| |_\/_| |_ | |
| |    `.__.'    | || |    |_____|   | || ||_____||_____|| |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------' 
        """
    ]
    color = random.choice(list(COLORS.values()))
    return f"{color}{random.choice(art)}{COLORS['end']}"

def get_funny_quote():
    """Return a random developer quote"""
    quotes = [
        "Code never lies, comments sometimes do.",
        "It works on my machine!",
        "DDRMin: Making the world more colorful, one HTTP request at a time",
        "There are 10 types of people: those who understand binary and those who don't.",
        "I'm not lazy, I'm just on energy-saving mode."
    ]
    return random.choice(quotes)

@app.route("/")
def hello():
    """Main endpoint with creative output"""
    # Generate dynamic content
    ascii_art = generate_ascii_art()
    quote = get_funny_quote()
    time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    visitor_num = random.randint(1000, 9999)
    
    # Build the response
    response = f"""
<html>
<head>
    <title>DDRMin Creative Server</title>
    <style>
        body {{
            background-color: #121212;
            color: #f0f0f0;
            font-family: 'Courier New', monospace;
            text-align: center;
            padding: 50px;
        }}
        .ascii-art {{
            white-space: pre;
            font-size: 0.8em;
            color: #{random.randint(100, 999)};
            margin: 20px 0;
        }}
        .quote {{
            font-style: italic;
            margin: 30px 0;
            color: #{random.randint(100, 999)};
        }}
        .info {{
            margin-top: 40px;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="ascii-art">{ascii_art}</div>
    <h1>Welcome to DDRMin Creative Server!</h1>
    <div class="quote">"{quote}"</div>
    <div class="info">
        <p>Server Time: {time_str}</p>
        <p>You are visitor #{visitor_num}</p>
    </div>
</body>
</html>
    """
    return response

if __name__ == "__main__":
    print(f"{COLORS['cyan']}Starting DDRMin creative server...{COLORS['end']}")
    print(f"{COLORS['yellow']}Visit http://localhost:80 in your browser!{COLORS['end']}")
    app.run(host='0.0.0.0', port=80)