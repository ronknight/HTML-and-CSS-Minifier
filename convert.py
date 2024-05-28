import htmlmin
from csscompressor import compress

def minify_html_with_embedded_css(input_file, output_file):
    # Read input HTML file
    with open(input_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Minify HTML
    minified_html = htmlmin.minify(html_content, remove_empty_space=True)

    # Minify embedded CSS
    minified_css = compress(minified_html)

    # Replace original CSS with minified CSS in the minified HTML
    minified_html_with_minified_css = minified_html.replace(minified_css, compress(minified_css))

    # Write minified HTML with embedded minified CSS to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(minified_html_with_minified_css)

# Usage example
input_file = 'input.html'
output_file = 'output.html'
minify_html_with_embedded_css(input_file, output_file)
