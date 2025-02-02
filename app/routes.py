import os
from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
from app import db
from app.models import Upload
from app.rss_generator import convert_to_rss

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            
            new_upload = Upload(filename=filename, file_type=filename.split('.')[-1])
            db.session.add(new_upload)
            db.session.commit()
            
            rss_feed = convert_to_rss(file_path)
            rss_filename = f"{filename}.xml"
            rss_path = os.path.join(UPLOAD_FOLDER, rss_filename)
            with open(rss_path, 'w', encoding='utf-8') as rss_file:
                rss_file.write(rss_feed)
            
            return send_file(rss_path, as_attachment=True)
    
    return render_template('upload.html')