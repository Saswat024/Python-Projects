# Python Projects

A collection of Python projects ranging from beginner to intermediate level. This repository serves as a learning resource and a playground for Python programming.

## Projects

### 1. Basic Calculator

A simple command-line calculator that performs basic arithmetic operations.

- **Features**:
  - Addition, subtraction, multiplication, and division
  - Clear screen functionality
  - User-friendly interface with menu-driven operations

### 2. Number Guessing Game

A fun number-guessing game where the player tries to guess a randomly generated number within a specified range.

- **Features**:
  - Customizable number range
  - Limited attempts
  - Hints (too high/too low)
  - Score tracking based on remaining attempts

### 3. Word Guessing Game

A word guessing game where players try to guess a hidden word with a limited number of attempts.

- **Features**:
  - Large dictionary of words
  - Visual feedback for correct/incorrect guesses
  - Attempts counter
  - Case-insensitive input

### 4. Real-Time Chat Application

A web-based real-time chat application built with FastAPI and WebSockets.

- **Features**:
  - Multiple chat rooms
  - Real-time messaging
  - Username customization
  - Responsive web interface

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
   pip install fastapi uvicorn websockets
   ```

## Usage

### Running the Projects

Each project is self-contained in its own directory. Navigate to the project directory and run the corresponding Python file:

```bash
# For example, to run the calculator:
cd "Basic Calculator"
python Calculator.py

# For the chat application:
cd "Real-Time Chat Application"
python server.py
# Then open http://localhost:8000 in your web browser
```

## Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Create a new branch for your feature (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Acknowledgments

- Thanks to all the open-source projects and tutorials that inspired these projects.
- Special thanks to the Python community for their amazing tools and libraries.
