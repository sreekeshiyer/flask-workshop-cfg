from flask import Blueprint, request, jsonify, redirect, render_template
from utils import add_todo, show_todos, complete_todo, delete_todo

todo = Blueprint("todo", __name__)


@todo.route("/", methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        
        if add_todo(request.form['task']) =='Success':
            return redirect("/")
            
        return "There was an issue adding your task"
    
    else:
        return render_template("index.html", todos = show_todos())
            
            
@todo.route("/complete/<id>")
def complete(id : str ):
    
    if complete_todo(id) == 'Success': 
        return redirect("/")
    return "There was an issue updating your todo"
        
    
            
@todo.route("/delete/<id>")
def delete(id: str):
    
    if delete_todo(id): 
        return redirect("/")
    return "There was an issue deleting your todo"
        