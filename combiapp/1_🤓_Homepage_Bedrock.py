import streamlit as st

st.set_page_config(
    page_title="Bedrock Courseware generator",
    page_icon="👋",
)

st.title("Main Page")
st.sidebar.success("Select a page above.")

if "input_file_name" not in st.session_state:
    st.session_state["input_file_name"] = ""
input_file_name = st.text_input('Enter the path to your input file:', '')

if input_file_name.startswith('"'):
    input_file_name = input_file_name[1:-1]

submit = st.button("Submit_path")
if submit:
    st.session_state["input_file_name"] = input_file_name
    st.write("You have entered: ", input_file_name)

