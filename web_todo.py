import streamlit as st
import functions
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

todos = functions.get_todos()


def add_todo():
    local_todo = st.session_state["new_todo"] + '\n'
    todos.append(local_todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app.")
st.text("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input("New todo", label_visibility="hidden", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

