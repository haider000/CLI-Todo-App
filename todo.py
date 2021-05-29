import argparse
import sys
from datetime import date


def read_todo_file():
    try:
        with open('todo.txt') as fobj:
            text = fobj.read().splitlines()
            no_of_tasks = len(text)
        
        if(no_of_tasks<=0):
            print("There are no pending todos!")
        else:
            for i in range(no_of_tasks-1, -1, -1):
                sys.stdout.buffer.write("[{}] {}\n".format(i+1,text[i]).encode('utf8'))
    except FileNotFoundError:
        print("There are no pending todos!")
        
   
    
def write_todo_file(todo_item):
    with open('todo.txt', 'a') as fobj:
        fobj.write(todo_item + "\n")
        print('''Added todo: "{}"'''.format(todo_item))


def delete_from_todo(task_no):
    with open('todo.txt', 'r+') as fobj:
        text = fobj.readlines()   
        no_of_todo_tasks = len(text)
      
        
        if(task_no > no_of_todo_tasks or task_no<=0):
            print("Error: todo #{} does not exist. Nothing deleted.".format(task_no))
        
        else:
            fobj.truncate(0)
            fobj.seek(0)
            text.pop(task_no -1)
            
            for line in text:
                fobj.write(line)     
            
            print("Deleted todo #{}".format(task_no))
    
   
        
            
 
def done_todo(task_no):
    with open('todo.txt', 'r+') as fobj:
        text = fobj.readlines()   
        no_of_todo_tasks = len(text)
        
        
        
        if(task_no > no_of_todo_tasks or task_no<=0):
            print("Error: todo #{} does not exist.".format(task_no))
        
        else:
            fobj.truncate(0)
            fobj.seek(0)
            done_todo = text.pop(task_no -1) # removing task from todo file
            
            
            
            write_done_file(done_todo)  # writing task to the done file
            
            for line in text:
                fobj.write(line)     
            
            print("Marked todo #{} as done.".format(task_no))
            
        
        
    

def write_done_file(name):
    with open('done.txt', 'a') as fobj:
        fobj.write("x {0} {1}".format( date.today(), name))
        

def report_of_tasks():
    completed_tasks = 0
    pending_tasks = 0
    with open('done.txt') as fobj1:
        text1 = fobj1.readlines() 
        completed_tasks = len(text1)
        
    with open('todo.txt') as fobj2:
        text2 = fobj2.readlines()
        pending_tasks = len(text2)
        
    print("{} Pending : {} Completed : {}".format(date.today(), pending_tasks,completed_tasks))

               
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument('first', type=str, nargs="?", default="")
    parser.add_argument('second', type=str, nargs="?", default="")
    
    args = parser.parse_args()
    
    if(args.first == "add"):
        if(args.second == ""):
            print("Error: Missing todo string. Nothing added!")
        else:
            write_todo_file( args.second )
    
    elif(args.first == "ls"):
        read_todo_file()
        
    elif(args.first == "del"):
        if(args.second == ""):
            print( "Error: Missing NUMBER for deleting todo.")
        
        else:
            delete_from_todo( int(args.second) )
    
    elif(args.first == "done"):
        if(args.second == ""):
            print("Error: Missing NUMBER for marking todo as done.")
        
        else:
            done_todo( int(args.second) )
    
    elif(args.first == "help" or args.first == ""):
       sys.stdout.buffer.write('''Usage :-\n'''.encode('utf8'))
       sys.stdout.buffer.write('''$ ./todo add "todo item"  # Add a new todo\n'''.encode('utf8'))
       sys.stdout.buffer.write('''$ ./todo ls               # Show remaining todos\n'''.encode('utf8'))
       sys.stdout.buffer.write('''$ ./todo del NUMBER       # Delete a todo\n'''.encode('utf8'))
       sys.stdout.buffer.write('''$ ./todo done NUMBER      # Complete a todo\n'''.encode('utf8'))
       sys.stdout.buffer.write('''$ ./todo help             # Show usage\n'''.encode('utf8'))
       sys.stdout.buffer.write('''$ ./todo report           # Statistics\n'''.encode('utf8'))
    elif(args.first == "report"):
       report_of_tasks()
    
   