# Python Projects

A collection of Python projects ranging from beginner to intermediate level. This repository serves as a learning resource and a playground for Python programming.

## Projects

### 1. Basic Calculator

A simple command-line calculator that performs basic arithmetic operations.

- **Features**:
  - Addition, subtraction, multiplication, and division
  - Input validation and error handling
  - Clear screen functionality for better user experience
  - User-friendly interface with menu-driven operations
  - Continuous operation with option to exit
  - Division by zero protection

### 2. Number Guessing Game

A fun number-guessing game where the player tries to guess a randomly generated number within a specified range.

- **Features**:
  - Customizable number range (user-defined lower and upper bounds)
  - Limited attempts (10 tries)
  - Interactive hints (too high/too low feedback)
  - Attempt counter with remaining tries display
  - Win/lose conditions with appropriate messages

### 3. Word Guessing Game

A word guessing game where players try to guess a hidden word letter by letter with a limited number of attempts.

- **Features**:
  - Large dictionary of 40+ educational words (science, technology, mathematics themes)
  - Visual feedback showing guessed letters and remaining blanks
  - Dynamic attempts counter (word length + 5 bonus attempts)
  - Case-insensitive input handling
  - Progressive word revelation as letters are guessed correctly
  - Personalized experience with username input

### 4. Real-Time Chat Application

A modern web-based real-time chat application built with FastAPI and WebSockets, featuring a responsive and intuitive user interface.

- **Features**:
  - **Real-time messaging** using WebSocket connections
  - **Multiple chat rooms** - users can join different rooms simultaneously
  - **Username customization** with personalized message display
  - **Modern responsive web interface** with gradient backgrounds and animations
  - **Message timestamps** showing when each message was sent
  - **User join/leave notifications** to track room activity
  - **Automatic message scrolling** to keep latest messages visible
  - **Elegant message bubbles** with different styling for user vs. other messages
  - **Keyboard shortcuts** (Enter key to send messages)
  - **Connection status handling** with error and disconnection feedback
  - **Cross-platform compatibility** - works on desktop and mobile browsers


## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/python-projects.git
   cd python-projects
   ```

2. For the Real-Time Chat Application, install the required dependencies:
   ```bash
   pip install fastapi uvicorn jinja2 python-multipart
   ```

## Usage

### Running the Projects

Each project is self-contained in its own directory. Navigate to the project directory and run the corresponding Python file:

```bash
# Basic Calculator
cd "Basic Calculator"
python Calculator.py

# Number Guessing Game
cd "Number Guessing Game"
python NumberGuess.py

# Word Guessing Game
cd "Word Guessing Game"
python WordGuess.py

# Real-Time Chat Application
cd "Real-Time Chat Application"
python chat.py
# Then open http://localhost:8000 in your web browser
# You'll be prompted to enter a username and room name
# Open multiple browser tabs/windows to test real-time chat functionality
```


## File Structure

```
python-projects/
├── Basic Calculator/
│   └── Calculator.py
├── Number Guessing Game/
│   └── NumberGuess.py
├── Word Guessing Game/
│   └── WordGuess.py
├── Real-Time Chat Application/
│   ├── chat.py                 # Main FastAPI server
│   ├── static/
│   │   ├── script.js          # Client-side JavaScript
│   │   └── styles.css         # CSS styling
│   └── templates/
│       └── index.html         # HTML template
└── README.md
```

## Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Create a new branch for your feature (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Learning Outcomes

These projects demonstrate various Python concepts:

- **Basic Calculator**: Input validation, exception handling, loops, functions
- **Number Guessing Game**: Random number generation, conditional statements, user input
- **Word Guessing Game**: String manipulation, list operations, game logic
- **Real-Time Chat Application**: Web development, WebSockets, asynchronous programming, HTML/CSS/JavaScript integration

## Acknowledgments

- Thanks to all the open-source projects and tutorials that inspired these projects
- Special thanks to the Python community for their amazing tools and libraries
- FastAPI and Uvicorn teams for excellent web framework and ASGI server
- The WebSocket protocol for enabling real-time communication
