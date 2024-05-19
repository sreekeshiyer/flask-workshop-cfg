import os
import json

from flask import Flask, render_template, url_for, request, redirect
from firebase_admin import credentials, firestore, initialize_app

app = Flask(__name__)
cred = credentials.Certificate('credentials.json')
default_app = initialize_app(cred)

db = firestore.client()

todo_ref = db.collection('todos')

@app.route("/", methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        
        try:
            todo_ref.add({"task": request.form['task'], "completed": False })
            
            return redirect("/")
            
        except: 
            return "There was an issue adding your task"
    
    else:
        
        try:
            todos = [ ]
            
            for doc in todo_ref.stream():
                
                todo = doc.to_dict()
                todo['id'] = doc.id
                todos.append(todo)
            print(todos)
            
            return render_template("index.html", todos = todos)
            
        except:
            
            return "There was an issue loading your todos"
            
            
@app.route("/complete/<id>")
def complete(id : str ):
    
    try: 
        todo_ref.document(id).update({"completed": True})
        
    except:
        return "There was an issue updating your todo"
        
    
            
@app.route("/delete/<id>")
def delete(id: str):
    
    try: 
        todo_ref = db.collection('todos').document(id)
        todo_ref.delete()
    except:
        return "There was an issue deleting your todo"
        
        
if __name__ == '__main__':
    
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)