# Digital Clock Application 🕐

A sleek and modern digital clock built with PyQt5, featuring a futuristic cyan display on a dark slate background.

## Features ✨

- Real-time digital clock display
- Custom digital font support (Digital-7)
- Modern dark theme with cyan accents
- Updates every second
- Clean and minimal interface
- Fallback font (Helvetica) if custom font is unavailable

## Screenshot

The clock displays time in 12-hour format with AM/PM indicator:
- **Format:** `hh:mm:ss AM/PM`
- **Colors:** Cyan text (#00E5FF) on dark slate background (#0F172A)
- **Font:** Digital-7 (or Helvetica as fallback)

## Requirements 📋

- Python 3.x
- PyQt5

## Installation 🚀

### 1. Install Python
Make sure you have Python 3.x installed on your system.

### 2. Install PyQt5
```bash
pip install PyQt5
```

### 3. Download the Font (Optional)
- Download the **Digital-7** font from:
  - [1001 Fonts](https://www.1001fonts.com/digital-7-font.html)
  - [DaFont](https://www.dafont.com/digital-7.html)
- Place the `digital-7.ttf` file in the same directory as the Python script
- Rename it to `digital-font` (or update the code to match your font filename)

## Project Structure 📁

```
digital-clock/
├── digital_clock.py    # Main application file
├── digital-font        # Digital-7 font file (optional)
└── README.md          # This file
```

## Usage 💻

1. Clone or download this repository
2. Navigate to the project directory
3. Run the application:

```bash
python digital_clock.py
```

The clock window will appear and automatically start displaying the current time.

## Customization 🎨

### Change Colors

In the `initUI()` method, modify the stylesheets:

```python
# Change text color
self.time_label.setStyleSheet("color: #YOUR_COLOR;")

# Change background color
self.setStyleSheet("background-color: #YOUR_COLOR;")
```

### Change Font Size

```python
my_font = QFont(font_family, 40)  # Change 40 to your desired size
```

### Change Window Size

```python
self.setGeometry(500, 400, 300, 150)  # x, y, width, height
```

### Change Time Format

In the `update_time()` method:

```python
# 24-hour format
current_time = QTime.currentTime().toString("HH:mm:ss")

# 12-hour format with AM/PM (current)
current_time = QTime.currentTime().toString("hh:mm:ss AP")

# Without seconds
current_time = QTime.currentTime().toString("hh:mm AP")
```

## Color Palette 🎨

- **Text Color:** `#00E5FF` (Cyan)
- **Background:** `#0F172A` (Dark Slate)
- **Border:** `#00E5FF` (Cyan) - if you want to add borders

## Troubleshooting 🔧

### Font Not Loading
If the Digital-7 font doesn't load:
1. Check that the font file is in the same directory as the script
2. Verify the filename matches exactly (case-sensitive)
3. The app will automatically fall back to Helvetica font

### Import Errors
If you get `ModuleNotFoundError: No module named 'PyQt5'`:
```bash
pip install PyQt5
```

### Window Not Appearing
- Check if another window is covering it
- Try changing the `setGeometry()` values to move the window position

## Code Structure 🏗️

- **`DigitalClock` class**: Main widget that inherits from QWidget
- **`__init__()`**: Initializes the clock components
- **`initUI()`**: Sets up the user interface, styling, and font
- **`update_time()`**: Updates the displayed time every second

## Features Explained 📖

### QTimer
Updates the clock display every 1000ms (1 second):
```python
self.timer.start(1000)
```

### Custom Font Loading
Loads the Digital-7 font with error handling:
```python
font_id = QFontDatabase.addApplicationFont("digital-font")
if font_id == -1:
    my_font = QFont("Helvetica", 40)  # Fallback
```

### Time Formatting
Uses Qt's QTime to get and format current time:
```python
QTime.currentTime().toString("hh:mm:ss ap")
```

## License 📄

This project is free to use and modify for personal or educational purposes.

## Contributing 🤝

Feel free to fork this project and submit pull requests for any improvements!

## Author ✍️

Created as a PyQt5 learning project.

## Acknowledgments 🙏

- Digital-7 font by Style-7
- PyQt5 framework by Riverbank Computing

---

**Enjoy your digital clock! ⏰**