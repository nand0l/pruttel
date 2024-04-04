import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

st.title("Main Page")
st.sidebar.success("Select a page above.")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

if "input_file_namet" not in st.session_state:
    st.session_state["input_file_name"] = ""
input_file_name = st.text_input('Enter the path to your input file:', '')

if input_file_name.startswith('"'):
    input_file_name = input_file_name[1:-1]

submit = st.button("Submit_path")
if submit:
    st.session_state["input_file_name"] = input_file_name
    st.write("You have entered: ", input_file_name)

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit_text")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)