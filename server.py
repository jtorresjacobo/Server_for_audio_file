import audiospeed
import convert_wav_with_features
import mysql_python
from flask import Flask
from flask import Response, jsonify, request, redirect, url_for
from pydub import AudioSegment

#persistent storage in dictionary
import shelve
#import main
#printing ip of host
import socket
import cut
#file uploading
import os
from werkzeug.utils import secure_filename

#serving files that were uploaded
from flask import send_from_directory

#mac-specific relative path to the script's location
UPLOAD_FOLDER = './audio'
ALLOWED_EXTENSIONS = set(['wav', 'ogg', 'mp3'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#configuration
def folder():
    if request.method == 'POST':
        file = request.files['file']
        name=file.filename.split(".")
        UPLOAD_FOLDER = './audio/'+name[0]
        app = Flask(__name__)
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    print 'upload file'

    try:
        ### .audio
        os.stat(app.config['UPLOAD_FOLDER'])

    except:        
        os.mkdir(app.config['UPLOAD_FOLDER'])
    if request.method == 'POST':
        file = request.files['file']
        print 'filename: ' + file.filename

        if file and allowed_file(file.filename):
            print 'allowing file'

            filename = secure_filename(file.filename)

            name=filename.split(".")    

            #main route       

            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

            #convert to format wav with features 
            #"name " is the name of audio file 
            name=convert_wav_with_features.audio(os.path.join(app.config["UPLOAD_FOLDER"]),filename)

            #modify audio speed to 0.5
            audiospeed.input_pathaudio(os.path.join(app.config["UPLOAD_FOLDER"]),name)

            #separating audio every 30 seconds
            cut.separate_audio(os.path.join(app.config["UPLOAD_FOLDER"]),name)

            #entering audio file to database
            mysql_python.input(os.path.join(app.config["UPLOAD_FOLDER"])+"/"+name)

            return redirect(url_for('uploaded_file',filename=filename))

    return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form action="" method=post enctype=multipart/form-data>
        <p><input type=file name=file>
        <input type=submit value=Upload>
        </form>
        '''


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    print(app.config['UPLOAD_FOLDER'],
                               "_1")
    return '''
        <!doctype html>
        <title>Ingreso satisfactorio</title>
        <h1>Ingreso satisfactorio</h1>
        '''    

#    return send_from_directory(app.config['UPLOAD_FOLDER'],
#    						   "_1")

if __name__ == '__main__':

    print(socket.gethostbyname(socket.gethostname()))
    app.run(host='0.0.0.0')
