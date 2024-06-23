from bs4 import BeautifulSoup
import re

def extract_text_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Function to extract text from tags
    def extract_text(tag):
        return tag.get_text(separator="\n").strip()
    
    # Extract title
    title = soup.title.string if soup.title else "无标题"

    # Extract all headings
    headings = []
    for i in range(1, 7):
        for header in soup.find_all(f'h{i}'):
            headings.append(f"{'#' * i} {extract_text(header)}")

    # Extract all paragraphs
    paragraphs = [extract_text(p) for p in soup.find_all('p')]

    # Extract all links
    links = [f"[{extract_text(a)}]({a['href']})" for a in soup.find_all('a', href=True)]

    # Extract all images
    images = [f"![{img.get('alt', '图片')}]({img['src']})" for img in soup.find_all('img', src=True)]

    # Combine extracted text
    combined_text = "\n\n".join(headings + paragraphs + links + images)
    
    # Clean up extra whitespace
    combined_text = re.sub(r'\n{3,}', '\n\n', combined_text)
    
    return f"# {title}\n\n{combined_text}".strip()

def write_to_markdown_file(text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

# Example HTML content
html_content = """

"""

# Extract text from the example HTML
extracted_text = extract_text_from_html(html_content)

# Write the extracted text to a Markdown file
output_filename = 'output.md'
write_to_markdown_file(extracted_text, output_filename)

print(f"Extracted text has been written to {output_filename}")
