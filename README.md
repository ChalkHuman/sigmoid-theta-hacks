# Sigmoid-Theta-Hacks
## Step 1: Create a Virtual Environment (for Macs)
First make sure that you have virtualenv installed. Run this code in your terminal to install:

	pip install virtualenv

Lets say that the name of the virtual environment that you want to create is:
	
	sigmoid-hacks-env

Create the virtual environment by opening the folder where you want the virtual environment in the terminal. Execute the following code:
	
	python3 -m venv sigmoid-hacks-env

Now it is time to install packages. Update the terminal with this code to make sure you are working in the context of the virtual environment:
	
	source sigmoid-hacks-env/bin/activate

Make sure that the interpreter is updated to the virtual environment.

Make sure to update pip as well, using the command:
	
	pip install --upgrade pip

## Step 2: Install the Packages in the Virtual Environment
Run this command in the terminal in the virtual environment:
	
	pip install -r requirements.txt

## Step 3: Required System Component
Ensure ffmpeg is installed in your local system because PyDub uses ffmpeg to work

On Mac use 

    brew install ffmpeg


## Files in this repository
**audio.py** - file that search file from youtube and download the song file

**spectrogram.py** - file that contains Spectrum model for lyrics separation
