## 🍎 HGR Vectorizer: Modern Images to Apple II Vectors

A Python command-line tool that bridges modern computer vision with 8-bit retro computing. 

**HGR Vectorizer** takes standard image files (like JPG or PNG), performs edge detection, and uses vector approximation to generate an **Applesoft BASIC** script full of `HPLOT` commands. The resulting script can be run natively on an Apple II (or an emulator) in High-Resolution Graphics (HGR) mode (280x192, monochrome).

---

## ✨ Features
- **Native Apple II Resolution:** Automatically downscales inputs to the classic 280x192 viewport.
- **Smart Vectorization:** Uses Canny Edge Detection and the Douglas-Peucker algorithm to convert dense pixel edges into memory-efficient, straight vector lines.
- **Adjustable Detail:** A simple command-line flag allows you to dial in the exact "blockiness" or detail level of the generated art.
- **Ready-to-Run Output:** Generates valid Applesoft BASIC code complete with line numbers and HGR setup commands.

## 🛠️ Installation

1. Make sure you have Python 3.x installed.
2. Clone or download this repository.
3. Install the required computer vision libraries via pip:


```bash
pip install opencv-python numpy

```

## 🚀 Usage

Run the script from your terminal, pointing it to your target image.

### Basic Usage

To generate the code and print it to your terminal:

```bash
python hgr_vectorizer.py photo.jpg

```

### Saving to a File (Recommended)

You'll likely want to save the output so you can load it onto an Apple II. Just pipe the output to a text file:

```bash
python hgr_vectorizer.py photo.jpg > art.bas

```

### Adjusting the Detail Level

Use the `-e` or `--epsilon` flag to change how aggressively the vectors are simplified.

* **Lower numbers** (e.g., `0.005`) = highly detailed, lots of short lines, uses more Apple II memory.
* **Higher numbers** (e.g., `0.05`) = very abstract, long geometric lines, uses less memory.

```bash
# Generate a highly abstract/geometric version of the image
python hgr_vectorizer.py photo.jpg -e 0.05 > abstract_art.bas

```

## 💾 How to Run on an Apple II

Once you have your `art.bas` file, you need to get it onto actual hardware or an emulator.

**Method 1: Paste into an Emulator (Quickest)**
Many emulators (like AppleWin for Windows) allow you to simply copy the text from `art.bas` and paste it directly into the emulator's window at the `]` prompt. Type `RUN` once it finishes pasting.

**Method 2: Disk Images (For Real Hardware)**

1. Use a tool like [CiderPress](https://a2ciderpress.com/) to open a blank `.dsk` image.
2. Import your `art.bas` text file as an Applesoft BASIC file.
3. Boot the `.dsk` on your real Apple II via a Floppy Emu or standard disk drive and run the file.

## 🧠 How it Works Under the Hood

1. **Grayscale & Resize:** The image is smashed down to 280x192 and stripped of color.
2. **Canny Edge Detection:** OpenCV finds the hard contrast lines in the image.
3. **Contour Mapping:** The edge pixels are grouped into continuous paths.
4. **Douglas-Peucker Algorithm:** `cv2.approxPolyDP()` analyzes the curvy pixel paths and removes vertices to create straight line approximations.
5. **Formatting:** The coordinate data is translated into `HPLOT X,Y TO X,Y` syntax, perfectly mapping OpenCV's `0,0` top-left origin to the Apple II's identical coordinate system.

## 📄 License

MIT License. Feel free to use, modify, and distribute for your own demoscene projects!
