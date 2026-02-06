# PYTHON-GUI Projects Collection

A collection of Python GUI applications built with Tkinter, featuring four distinct utility applications with modern and user-friendly interfaces.

## 📋 Table of Contents
- [Projects Overview](#projects-overview)
- [Installation](#installation)
- [Projects](#projects)
  - [Digital Clock](#1-digital-clock)
  - [Calculator](#2-calculator)
  - [Stop Watch](#3-stop-watch)
  - [Weather Application](#4-weather-application)
- [Requirements](#requirements)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Projects Overview

This repository contains four Python GUI applications:

1. **Digital Clock** - A real-time digital clock display
2. **Calculator** - A fully functional calculator with standard operations
3. **Stop Watch** - A precision stopwatch with start, stop, and reset functions
4. **Weather Application** - A weather information app with live data

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/SamiKhan43/PYTHON-GUI.git
cd PYTHON-GUI
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 📂 Projects

### 1. Digital Clock

A simple yet elegant digital clock that displays the current time in real-time.

**Features:**
- Real-time clock display
- Clean and minimal interface
- 12/24 hour format support
- Date display

**How to Run:**
```bash
cd digital-clock
python digital_clock.py
```

---

### 2. Calculator

A fully functional calculator application with a graphical user interface.

**Features:**
- Basic arithmetic operations (Addition, Subtraction, Multiplication, Division)
- Clear and delete functions
- Decimal point support
- Keyboard input support
- Error handling

**How to Run:**
```bash
cd calculator
python calculator.py
```

**Supported Operations:**
- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division
- Percentage calculations
- Square root and advanced operations

---

### 3. Stop Watch

A precise stopwatch application with millisecond accuracy.

**Features:**
- Start/Stop functionality
- Reset button
- Lap time recording
- Millisecond precision
- Clean and intuitive UI

**How to Run:**
```bash
cd stop-watch
python stopwatch.py
```

**Controls:**
- **Start**: Begin timing
- **Stop**: Pause the timer
- **Reset**: Clear the timer
- **Lap**: Record lap times

---

### 4. Weather Application

A weather application that fetches and displays current weather information for any city.

**Features:**
- Real-time weather data
- Temperature display (Celsius/Fahrenheit)
- Weather conditions and descriptions
- Humidity and wind speed information
- City search functionality
- Weather icons

**How to Run:**
```bash
cd weather-application
python weather_app.py
```

**API Requirements:**
- Requires an API key from [OpenWeatherMap](https://openweathermap.org/api)
- Add your API key in the configuration file or as an environment variable

**Setup:**
1. Sign up for a free API key at OpenWeatherMap
2. Add your API key to the application:
```python
API_KEY = "your_api_key_here"
```

---

## 📦 Requirements

All required Python packages are listed in `requirements.txt`:

```
tkinter (usually comes with Python)
requests (for weather application)
python-dateutil
pillow (for image handling)
```

Install all dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

Each project is self-contained in its respective folder. Navigate to the desired project folder and run the main Python file.

**General Structure:**
```
PYTHON-GUI/
├── digital-clock/
│   ├── digital_clock.py
│   └── README.md
├── calculator/
│   ├── calculator.py
│   └── README.md
├── stop-watch/
│   ├── stopwatch.py
│   └── README.md
├── weather-application/
│   ├── weather_app.py
│   ├── config.py
│   └── README.md
├── .gitignore
├── requirements.txt
└── README.md
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## 📝 Development

### Running Tests
```bash
python -m pytest tests/
```

### Code Style
This project follows PEP 8 style guidelines. Please ensure your code is formatted accordingly.

## 🐛 Known Issues

- Weather app requires internet connection
- API rate limits may apply for weather data

## 🔮 Future Enhancements

- [ ] Add dark mode theme
- [ ] Add more calculator functions (scientific mode)
- [ ] Export stopwatch lap times to CSV
- [ ] Add weather forecasts (5-day, 7-day)
- [ ] Add unit tests for all applications
- [ ] Create executable files for each application

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Sami Khan**
- GitHub: [@SamiKhan43](https://github.com/SamiKhan43)

## 🙏 Acknowledgments

- Python Tkinter documentation
- OpenWeatherMap API
- Python community for inspiration and support

## 📞 Contact

For questions or suggestions, please open an issue on GitHub or contact the repository owner.

---

⭐ **If you found this project helpful, please give it a star!** ⭐