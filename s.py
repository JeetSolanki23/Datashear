from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Specify the upload folder location
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Check if the 'file' key is in the request.files dictionary
    if 'file' not in request.files:
        return 'No file selected'
    
    file = request.files['file']
    
    # Check if the file has a filename
    if file.filename == '':
        return 'No file selected'

    # Save the file to the specified upload folder
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    
    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
