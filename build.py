import os
import shutil

POSTS_DIR = "posts"
OUTPUT_DIR = "site"

# Clear previous build
if os.path.exists(OUTPUT_DIR):
    shutil.rmtree(OUTPUT_DIR)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Generate index page
index_content = "<html><head><title>Blog</title></head><body>"
index_content += "<h1>Katnip Blog</h1><ul>"

# Process each post
for folder in sorted(os.listdir(POSTS_DIR), reverse=True):  # Sort by newest first
    post_path = os.path.join(POSTS_DIR, folder, "post.md")
    assets_src = os.path.join(POSTS_DIR, folder, "assets")
    post_output_dir = os.path.join(OUTPUT_DIR, folder)

    if not os.path.exists(post_path):
        continue

    # Read the md content
    with open(post_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    # Wrap Markdown in <github-md> tags
    post_html = f"""
    <html>
    <head><title>{folder}</title></head>
    <body>
        <h1>{folder}</h1>
        <github-md>
        {markdown_content}
        </github-md>
        <br><a href="../index.html">Back to home</a>
    </body>
    <script src="https://cdn.jsdelivr.net/gh/MarketingPipeline/Markdown-Tag/markdown-tag.js"></script> 
    </html>
    """

    # Create post output directory
    os.makedirs(post_output_dir, exist_ok=True)

    # Write the post HTML file
    with open(os.path.join(post_output_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(post_html)

    # Copy assets folder if it exists
    assets_dest = os.path.join(post_output_dir, "assets")
    if os.path.exists(assets_src):
        shutil.copytree(assets_src, assets_dest, dirs_exist_ok=True)

    # Add post link to index
    index_content += f'<li><a href="{folder}/index.html">{folder}</a></li>'

index_content += "</ul></body></html>"

# Write index file
with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_content)

print("✅ Static site generated in 'site/' directory.")
