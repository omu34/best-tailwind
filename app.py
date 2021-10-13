from flask import Flask,render_template
 
app=Flask(__name__)

@app.route('/')
def home_page(): 
    return "<h1>mines</h1>"
# render_template('base.html')

if __name__ == '__main__':
    app.run(port=3400,debug=True)