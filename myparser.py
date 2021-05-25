import os
from pathlib import Path



def string(a):
    return f'''<div class="gallery-item">
            <a href = "{{{{ url_for('static', filename='images/{a}') }}}}">
			<img class="gallery-image" src="{{{{ url_for('static', filename='images/{a}') }}}}">
            </a>
        </div>'''

def parse(link_list):
    result = ""
    for x in link_list:
        result += string(x)
    return result

def pictures():
    paths = sorted(Path("static/images").iterdir(), key=os.path.getmtime)
    a = []
    for x in paths:
        a.append(os.path.basename(x))
    
    return a

