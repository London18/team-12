from flask import Flask, render_template, request
import os

current_user = None

app = Flask(__name__)

Q={'1' : {
   'question' : 'I couldn’t seem to experience any positive feeling at all',
   'fields'   : ['Strongly disagree', 'Disagree', 'Agree', 'Strongly agree', 'skip']
},

'2' : {
   'question' : 'I found it difficult to work up the initiative to do things',
   'fields'   : ['Strongly disagree', 'Disagree', 'Agree', 'Strongly agree', 'skip']
},

'3' : {
   'question' : 'I couldn’t seem to experience any neutral feeling at all',
   'fields'   : ['Strongly disagree', 'Disagree', 'Agree', 'Strongly agree', 'skip']
},

'4' : {
   'question' : 'I found it hard to wind down',
   'fields'   : ['Strongly disagree', 'Disagree', 'Agree', 'Strongly agree', 'skip']
},

'5' : {
   'question' : 'I was aware of dryness of my mouth',
   'fields'   : ['Strongly disagree', 'Disagree', 'Agree', 'Strongly agree', 'skip']
}
}

@app.route('/login')
def root1():
    #return render_template('poll.html', data=getquestion(count))
    return render_template('login.html')

@app.route('/question', methods = ['GET', 'POST'])
def loginsuccess():
    global current_user
    current_user = request.form.get('username')
    with open('saveresponse.csv','a+') as f:
        f.write('\n'+ current_user)
    return render_template('question.html', data = Q['1'])
 
count=1

@app.route('/poll')
def poll():
    global count
    vote = request.args.get('field')
    with open('saveresponse.csv','a+') as f:
        f.write(','+vote)
    count+=1
    if count>=6:
        count = 1
        return render_template('thankyou.html', data={'user':current_user})
    
    return render_template('question.html', data=Q[str(count)])
    


if __name__ == "__main__":
    app.run(debug=True)
    
