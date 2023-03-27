import streamlit as st
import functions as func


todos = func.get_list()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    func.put_list(todos)


st.title("My Todo Application")
st.subheader("This is my web-based 'ToDo' Application.")
st.write("This application's purpose is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        func.put_list(todos)
        del st.session_state[todo]
#        st.text_input[new_todo]=""
        st.experimental_rerun()

st.text_input(label="todo_to_add", value="", placeholder="Add a new Todo...",
              label_visibility="hidden", on_change=add_todo, key='new_todo')

# st.session_state