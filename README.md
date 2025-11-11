# ALTO to TEI

This repository contains a Python script to convert ALTO XML files into TEI XML format. The conversion process extracts text content from ALTO files.
TEI elements such as `<teiHeader>`, `<text>`, `<body>`, and `<p>` are created to structure the output TEI document.

* TextBlocks in ALTO files are mapped to TEI divisions (`<div>`), with their content preserved.
* TextLine elements are represented using `<lb/>` tags to indicate line breaks.


## Requirements

- Python 3.7 or higher
- lxml library
- Install dependencies using `pip install -r requirements.txt` 
- Jupyter Notebook (for running the provided notebook)



## Example

An example ALTO file is provided in the `data/sample` directory. You can use this file to test the conversion process.


## Usage

1. Clone the repository:
   ```bash
    git clone https://github.com/ludovicmoncla/alto-to-tei.git
    cd alto-to-tei
    ```
2. Option 1: Run the Jupyter Notebook:
    ```bash
    jupyter notebook alto2tei.ipynb
    ```
3. Option 2: Use the script directly (update paths as needed):

    ```bash
    python alto2tei.py
    ```

## Code Snippet

```python
from alto2tei import alto_to_tei, display_tei, save_tei
alto_path = "data/sample/X0000041.xml"
tei_path = "outputs/X0000041.xml"
tei = alto_to_tei(alto_path)
display_tei(tei)
save_tei(tei, tei_path)
``` 