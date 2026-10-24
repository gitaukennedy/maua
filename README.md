# 🌸 3D Botanical Lily Animation

A procedural 3D animation of an Oriental lily bouquet, rendered in Python as a vertical 9:16 video. The animation is 1080 × 1920 pixels, 30 frames per second, and 13 seconds long.

## Features

- Procedurally modeled petals, stems, leaves, stamens, and pistils
- Animated construction and flower reveal
- MP4 output encoded with FFmpeg
- Optional preview keyframes

## Requirements

- Windows with Python installed and available as `python`
- NumPy and OpenCV for Python
- FFmpeg for MP4 encoding

## Setup in Git Bash

From the project directory, create and activate a virtual environment, then install the Python packages:

```bash
python --version
python -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
python -m pip install numpy opencv-python
```

Install FFmpeg from Git Bash using Winget if it is not installed already:

```bash
winget install --id Gyan.FFmpeg --source winget --accept-source-agreements --accept-package-agreements
```

Winget installs FFmpeg under the user's local WinGet package directory. The script searches that directory automatically, so a restarted shell or a manually edited `PATH` is not required. To override the detected executable, set `FFMPEG_PATH` to its full Windows path before running the script.

## Run

Render the complete animation:

```bash
python generate_lily_animation.py
```

The video is written to `lily_3d_botanical_animation.mp4` in the project directory. Rendering all 390 frames may take several minutes.

Render four preview images instead:

```bash
python generate_lily_animation.py --preview
```

Preview PNG files are written to the project directory.

## Dependencies

Python packages:

```text
numpy
opencv-python
```

FFmpeg is a separate system executable and is not installed by `pip`.
