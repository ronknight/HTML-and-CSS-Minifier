<p><a target="_blank" href="https://app.eraser.io/workspace/6XEqNIjQGB0cKieTPlYE" id="edit-in-eraser-github-link"><img alt="Edit in Eraser" src="https://firebasestorage.googleapis.com/v0/b/second-petal-295822.appspot.com/o/images%2Fgithub%2FOpen%20in%20Eraser.svg?alt=media&amp;token=968381c8-a7e7-472a-8ed6-4a6626da5501"></a></p>

<h1 align="center"><a href="https://github.com/ronknight/HTML-and-CSS-Minifier">﻿HTML and CSS Minifier</a></h1>
<h4 align="center">This Python script minifies an HTML file with embedded CSS using the htmlmin and csscompressor libraries.</h4>

<p align="center">
<a href="https://twitter.com/PinoyITSolution"><img src="https://img.shields.io/twitter/follow/PinoyITSolution?style=social"></a>
<a href="https://github.com/ronknight?tab=followers"><img src="https://img.shields.io/github/followers/ronknight?style=social"></a>
<a href="https://github.com/ronknight/ronknight/stargazers"><img src="https://img.shields.io/github/stars/BEPb/BEPb.svg?logo=github"></a>
<a href="https://github.com/ronknight/ronknight/network/members"><img src="https://img.shields.io/github/forks/BEPb/BEPb.svg?color=blue&logo=github"></a>
  <a href="https://youtube.com/@PinoyITSolution"><img src="https://img.shields.io/youtube/channel/subscribers/UCeoETAlg3skyMcQPqr97omg"></a>
<a href="https://github.com/ronknight/HTML-and-CSS-Minifier/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
<a href="https://github.com/ronknight/HTML-and-CSS-Minifier/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
<a href="#"><img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"></a>
<a href="https://github.com/ronknight"><img src="https://img.shields.io/badge/Made%20with%20%F0%9F%A4%8D%20by%20-%20Ronknight%20-%20red"></a>
</p>

<p align="center">
  <a href="#requirements">Requirements</a> •
  <a href="#usage">Usage</a> •
  <a href="#diagrams">Diagrams</a> •
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
1. Save your HTML file with embedded CSS as `input.html` .
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


<!-- eraser-additional-content -->
## Diagrams
<!-- eraser-additional-files -->
<a href="/README-Minify HTML with Embedded CSS-1.eraserdiagram" data-element-id="WJp3Fc-bPd5nyRcn8tyTc"><img src="/.eraser/6XEqNIjQGB0cKieTPlYE___3Jivg2tjMecMlrHwbIVIBR8f7U03___---diagram----c55cb5e0dabdc3f5829434801d44c35f-Minify-HTML-with-Embedded-CSS.png" alt="" data-element-id="WJp3Fc-bPd5nyRcn8tyTc" /></a>
<!-- end-eraser-additional-files -->
<!-- end-eraser-additional-content -->
<!--- Eraser file: https://app.eraser.io/workspace/6XEqNIjQGB0cKieTPlYE --->
