from flask import Flask, render_template, request
import os
app = Flask(__name__)

#@app.route('/login')
#def root():
    #return render_template('poll.html', data=getquestion(count))
#    return render_template('login.html', data = getquestion(count))

#@app.route('/question')
#def loginsuccess():
    #username = request.args.get(pass)
    #return username 
 
Q={'1' : {
   'question' : 'I couldn’t seem to experience any positive feeling at all',
   'fields'   : ['0', '1', '2', '3']
},

'2' : {
   'question' : 'I found it difficult to work up the initiative to do things',
   'fields'   : ['0', '1', '2', '3']
},

'3' : {
   'question' : 'I couldn’t seem to experience any neutral feeling at all',
   'fields'   : ['0', '1', '2', '3']
},

'4' : {
   'question' : 'I found it hard to wind down',
   'fields'   : ['0', '1', '2', '3']
},

'5' : {
   'question' : 'I was aware of dryness of my mouth',
   'fields'   : ['0', '1', '2', '3']
}
}

count=1

@app.route('/')
def root():
    username = request.args.get('password')
    with open('saveresponse.csv','a+') as f:
        f.write(username + '\n')
    #return render_template('poll.html', data=getquestion(count))
    return render_template('poll.html', data = Q['1'])

@app.route('/poll')
def poll():
    global count
    vote = request.args.get('field')
    with open('saveresponse.csv','a+') as f:
        f.write(vote + '\n')
    count+=1
    return render_template('poll.html', data=Q[str(count)])

if __name__ == "__main__":
    app.run(debug=True)