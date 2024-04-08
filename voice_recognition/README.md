<!-- ABOUT THE PROJECT -->
## About The Project

This is a reference for voice recognition with whisper API based on [here](https://pypi.org/project/openai-whisper/).
Whisper AI model supports tiny/base/small/medium/large models.


<!-- GETTING STARTED -->
## Getting Started

Instructions on setting up your project locally.

### Prerequisites

  ```sh
  sudo apt update
  sudo apt install ffmpeg
  sudo apt install python3-pyaudio
  ```

### Python virtual env

  ```sh
  python3 -m venv venv_whisper
  source venv_whisper/bin/activate
  pip install -U pip
  ```

### Installation

  ```sh
  pip install -r requirements.txt
  ```

<!-- USAGE EXAMPLES -->
## Usage

Run the python code for voice recognition with whisper
  ```sh
  python3 test_whisper.py or python3 test_whisper_en.py
  ```

Run the python code for mic recording as a file
  ```sh
  python3 mic_rec.py
  ```

Run the python code for mic input and voice recognition
  ```sh
  python3 mic_whisper.py or python3 mic_google.py
  ```
