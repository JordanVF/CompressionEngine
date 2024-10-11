# Compression/Decompression Engine

A graphical user interface (GUI) application built with Python's Tkinter that allows users to compress and decompress files using a custom compression algorithm.

## Description

This application provides a simple GUI for compressing and decompressing files. It uses functions from a custom `compressmodule` module for compression and decompression logic. The user can select a file to compress or input file paths for decompression via the provided entry fields.


## Installation 
1. Clone this repository: 
```bash 
git clone https://github.com/JordanVF/CompressionEngine.git
```
2. Navigate to the project directory: 
```bash
cd CompressionEngine
```
3. Install the required dependencies, tKinter and compressmodule:
```bash
pip install tk
```
4. Ensure the compressmodule.py file containing the compress() and decompress() functions is present in the project directory.

## Usage
### Compression
1. Run the application:
```bash
python compDecompEngine.py
```
2. Use the Compress button to select a file to compress. The compressed file will be saved as Compression/compOut1.txt (you can modify this path in the code if needed).

### Decompression
1. Enter the input file path in the "Input File" field.
2. Enter the desired output file path in the "Output File" field.
3. Click the Decompress button.

## How it works

### Compression
- The open_file() function opens a file dialog to select a file.
- The selected file is passed to the compression() function, which uses the compress() function from compressmodule to perform the compression.
### Decompression
- The input and output file paths are fetched from the entry fields.
- The decompression() function uses the decompress() function from compressmodule to perform the decompression.
## License

This project is licensed under the MIT License. See the LICENSE file for more details.

