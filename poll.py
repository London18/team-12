from flask import Flask, render_template
import os
app = Flask(__name__)
 
poll_data1 = {
   'question' : 'I couldn’t seem to experience any positive feeling at all',
   'fields'   : ['0', '1', '2', '3']
}

poll_data2 = {
   'question' : 'I couldn’t seem to experience any negative feeling at all',
   'fields'   : ['0', '1', '2', '3']
}


count=-1
 
@app.route('/')
def root():
    return render_template('poll.html', data=getquestion(count))

#@app.route('/poll')
#def poll():
    #vote = request.args.get('field')
    #return vote 


def getquestion(count):
    count+=1
    if count%2==0:
        return poll_data1
    return poll_data2

    
if __name__ == "__main__":
    app.run(debug=True)