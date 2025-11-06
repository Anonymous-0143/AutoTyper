# Auto Typer

A simple and convenient desktop utility built with Python and Tkinter to automate typing of predefined text snippets. This tool is designed to stay on top of other windows, allowing you to quickly paste text into any application using buttons or global hotkeys.


## Features

- **Always-on-Top:** The window stays visible over other applications for easy access.
- **Tabbed Interface:** Manage up to 10 different text snippets in separate tabs.
- **Multiple Pasting Modes:**
  - **Normal Paste:** Types the text exactly as it appears in the text box.
  - **Single Line:** Removes all newline characters to type the text as a single line.
  - **Line by Line:** Removes tab characters, useful for pasting code snippets without unwanted indentation.
- **Global Hotkeys:** Trigger typing actions from any application.
  - `Ctrl+6`: Normal Paste (with a 1-second delay).
  - `Ctrl+7`: Single Line Paste (with a 1-second delay).
  - `Ctrl+8`: Line by Line Paste (with a 1-second delay).
- **Clickable Buttons:** Manually trigger typing actions with a 4-second delay to give you time to switch to your target window.
- **Modern UI:** Features a clean, dark theme (`equilux`) for comfortable use.
- **Direct GitHub Link:** Includes a clickable label to visit the author's GitHub profile.

## How to Use

1.  Run the `auto_typer.exe` executable.
2.  Type or paste the text you want to automate into any of the 10 available tabs.
3.  Click on the application window where you want the text to be typed.
4.  Choose one of the following methods to start typing:
    - **Buttons:** Click one of the three buttons at the bottom ("Paste", "Single Line", "Line by Line"). You will have 4 seconds to focus the target window before typing begins.
    - **Hotkeys:** Use the corresponding hotkey combination (`Ctrl+6`, `Ctrl+7`, or `Ctrl+8`). You will have 1 second to focus the target window.

## Dependencies

This project relies on the following Python libraries:

- `pynput`: For controlling and monitoring input devices.
- `keyboard`: For global hotkey management.
- `ttkthemes`: To provide modern themes for the Tkinter UI.
- `Pillow`: For handling images used on the buttons.

## Building from Source

If you want to build the executable from the source code, follow these steps:

1.  **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/autotyper-master.git
    cd autotyper-master
    ```

2.  **Install dependencies:**
    It's recommended to use a virtual environment.

    ```sh
    pip install pynput keyboard ttkthemes Pillow pyinstaller
    ```

3.  **Run PyInstaller:**
    Navigate to the project's root directory in your terminal and run the following command to create a single executable file.

    ```sh
    pyinstaller --noconsole --onefile --windowed --icon=res/app_icon.ico --add-data "res;res" auto_typer.py
    ```

    - `--noconsole` or `--windowed`: Prevents the command prompt from appearing.
    - `--onefile`: Packages everything into a single `.exe` file.
    - `--icon`: Sets the application icon.
    - `--add-data "res;res"`: Bundles the `res` folder containing images and icons into the executable.

4.  **Find the Executable:**
    The final `auto_typer.exe` file will be located in the `dist` folder.

## Credits

This application was created by **Arin Choubey**.

Feel free to visit my GitHub Profile.

