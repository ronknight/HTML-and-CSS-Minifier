<h1 align="center"><a href="https://github.com/ronknight/HTML-and-CSS-Minifier">HTML and CSS Minifier</a></h1>
<h4 align="center">This Python script minifies an HTML file with embedded CSS using the htmlmin and csscompressor libraries.</h4>

<p align="center">
<a href="https://twitter.com/r0nknight"><img src="https://img.shields.io/twitter/follow/r0nknight?style=social"></a>
<a href="https://github.com/ronknight?tab=followers"><img src="https://img.shields.io/github/followers/ronknight?style=social"></a>
<a href="https://github.com/ronknight/HTML-and-CSS-Minifier/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
<a href="https://github.com/ronknight/HTML-and-CSS-Minifier/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
<a href="#"><img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"></a>
<a href="#"><img src="https://img.shields.io/badge/Made%20with%20%F0%9F%A4%8D%20by%20-%20Ronknight%20-%20red"></a>
</p>

<p align="center">
  <a href="#requirements">Requirements</a> •
  <a href="#usage">Usage</a>
</p>

---
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