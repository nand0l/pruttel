import streamlit as st

st.title("Streamlit Cheatsheet")

# Display code then execute and show output
st.header("st.write")
st.write("""Write arguments to the app.

This is the Swiss Army knife of Streamlit commands: it does different things depending on what you throw at it. Unlike other Streamlit commands, write() has some unique properties:

- You can pass in multiple arguments, all of which will be written.
- Its behavior depends on the input types as follows.
- It returns None, so its "slot" in the App cannot be reused.")
         """)

st.subheader("st.write('string')")
st.code('st.write("Most objects")')
st.write("Most objects")  # df, err, func, keras!

st.subheader("st.write(list)")
st.code('st.write(["st", "is <", 3])')
st.write(["st", "is <", 3])  # see *

# Display code then execute and show output
st.subheader("st.text('string')")
st.code('''st.text("Fixed width text")''')
st.text("Fixed width text")

st.subheader("st.markdown('markdown_formatted_string')")
st.code('st.markdown("_Markdown_")')
st.markdown("_Markdown_")  # see *

st.code('''st.latex(r""" e^{i\\pi} + 1 = 0 """)''')
st.latex(r""" e^{i\pi} + 1 = 0 """)

st.code('''st.title("My title")''')
st.title("My title")

st.code('''st.header("My header")''')
st.header("My header")

st.code('''st.subheader("My sub")''')
st.subheader("My sub")

st.code('''st.code("for i in range(8): foo()")''')
st.code("for i in range(8): foo()")
