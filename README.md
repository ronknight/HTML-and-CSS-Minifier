# HTML and CSS Minifier

This Python script minifies an HTML file with embedded CSS using the `htmlmin` and `csscompressor` libraries.

## Requirements

- Python 3.x
- htmlmin
- csscompressor

You can install the required libraries using pip:

```bash
pip install htmlmin csscompressor
```

## Usage

1. Save your HTML file with embedded CSS as `input.html`.
2. Run the script:

```python
python convert.py
```

This will create a new file output.html containing the minified HTML with the minified embedded CSS.

The minify_html_with_embedded_css function takes two arguments:

- input_file: The path to the input HTML file with embedded CSS.
- output_file: The path to the output file where the minified HTML with embedded minified CSS will be written.

The function performs the following steps:
- Read the input HTML file.
- Minify the HTML using htmlmin.minify.
- Extract the embedded CSS from the minified HTML.
- Minify the extracted CSS using csscompressor.compress.
- Replace the original CSS in the minified HTML with the minified CSS.
- Write the minified HTML with embedded minified CSS to the output file.

License
This project is licensed under the MIT License.