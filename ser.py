from flask import Flask , render_template
from alfred import alfred

app=Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')


@app.route('/alfred')

def activate():
    return alfred()




if __name__=="__main__":
    app.run(debug = True)
