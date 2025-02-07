# Timer Application

## Description

A simple GTK-based countdown timer with a Start/Stop toggle button and a Reset button. The timer runs in a separate thread to ensure the UI remains responsive.

## Features

- **Start/Stop Timer:** Toggle button to start and stop the countdown.
- **Reset Timer:** Reset button to restore the timer to the initial duration.
- **Thread Management:** Uses a separate daemon thread for the countdown.
- **Live Time Update:** Timer updates dynamically in the UI without freezing.
- **Customizable Duration:** Modify `self.duration` in `timer.py` to set a different countdown time.

## Prerequisites

Ensure the following dependencies are installed:

- **Python 3**
- **GTK 3 and PyGObject**

To install GTK and PyGObject on Fedora, run:

```sh
sudo dnf install gtk3 python3-gobject
```

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/timer.git
   ```
2. **Navigate into the project directory:**
   ```sh
   cd timer
   ```
3. **Run the timer application:**
   ```sh
   python3 timer.py
   ```

## Creating an Executable

Note: The current repo already has executable present. To create in your device, copy the timer.py file to next folder or delete the executable files.
To create an executable file using `pyinstaller`, follow these steps:

1. Install `pyinstaller`:
   ```sh
   pip install pyinstaller
   ```
2. Generate the executable:
   ```sh
   pyinstaller --onefile --windowed timer.py
   ```
3. The executable will be found in the `dist/` folder.

## Usage

- Click **Start** to begin the countdown.
- Click **Stop** to pause the countdown.
- Click **Reset** to restore the timer to the initial duration.

## Contributing

1. Fork the repository
2. Create a new branch:
   ```sh
   git checkout -b feature-branch
   ```
3. Make changes and commit:
   ```sh
   git commit -m "Add new feature"
   ```
4. Push to GitHub and create a Pull Request:
   ```sh
   git push origin feature-branch
   ```
5. Your pull request will be reviewed before approval. Feedback may be provided, and changes might be requested before merging.

## To-Do

- Add timer for break period.
- Implement the program in OS system tray.
