from flask import Flask,render_template
from StickyNotesModel import AddNotes,ViewNotes

app = Flask(__name__)

app.add_url_rule('/addNotes', view_func=AddNotes.as_view('add_notes'),
    methods=['POST'])
app.add_url_rule('/viewNotes', view_func=ViewNotes.as_view('view_notes'),
    methods=['GET'])

@app.route('/')
def index():
    print "inside index"
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug='true')
