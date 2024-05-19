from config import db

todo_ref = db.collection('todos')

def show_todos() -> list:
    
    todos = [ ]
    try:
        for doc in todo_ref.stream():
            todo = doc.to_dict()
            todo['id'] = doc.id
            todos.append(todo)
        print(todos)
    except:
        print("Error fetching todos")
    
    return todos
    

def add_todo(task : str) -> str:
    """Add a Todo to the Firebase collection"""
    
    try:
        todo_ref.add({"task": task, "completed": False })
        return "Success"
    except:
        return "Error"
        
def complete_todo(id: str) -> str:
    """Update a Todo Item as Completed"""
    
    try:
        todo_ref.document(id).update({"completed": True})        
        return "Success"
    except Exception as e:
        print(e)
        return "Error"
        
        
def delete_todo(id: str) -> str:
    """Delete a todo from the list"""
    
    try:
        todo_ref = db.collection('todos').document(id)
        todo_ref.delete()
        return "Success"
    except:
        return "Error"
    