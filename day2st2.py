import streamlit as st
st.header("anurag university student management system Varshitha Kadiyam")
st.title("welcome to anurag university")
st.subheader("manage student records easily")
st.markdown("-------------------")
st.text("this application allows you to perform crud operations on student records using mysql database")
st.write("hello srinika")
st.write("123")
st.write(1,3,5,6,7)
st.write("name: srinika","age: 34","course: python")
st.markdown("### features of the application")
st.markdown("**bold text**")
st.markdown("*italic text*")
st.markdown("<h3 style='color:red'>done Students</h3>",unsafe_allow_html=True)
st.caption("this is a caption for the student management system")
st.code("""
    def add(a,b):
        return a+b
        """,language='python')
st.latex(r'''
         a^2+b^2=c^2
            ''')
st.divider()
if st.button("click me"):
    st.write("button clicked")
    st.success("operation successful")
    st.snow()
else:
    st.write("button not clicked yet")
    st.error("operation failed")
name=st.text_input("enter your name")
st.write(f"hello,{name}!")
if name=="":
    st.warning("name cannot be empty")
elif not name.isalpha():
    st.error("invalid input")
else:
    st.success(f"hello,{name}!")
    feedback=st.text_area("enter feedback")
    st.write(feedback)
    if st.checkbox("i agee to the trems and condiytion"):
        st.write("thanks for aggreeing")
gender=st.radio("Select your gender:",("Male","feamle","other"))
st.write(f"you selected:{gender}")
country=st.selectbox("select your country",("india","usa","uk","canada"))
st.write(f"you selected:{country}")
skills=st.multiselect("Select skills",["python","java","c","streamlit"])
st.write(f"Skills:",skills)
age=st.slider("select your age",0,100,25)
st.write(f"age:(age)")
uploaded_file=st.file_uploader("choose a file")
if uploaded_file is not None:
     st.success("file uploaded successfullly")
     st.write(f"filename:{uploaded_file.name}")
st.divider()
with st.form("my_form"):
    name=st.text_input("Name")
    age=st.number_input("age",0,100)
    submit=st.form_submit_button("submit")
if submit:
    st.write(name,age)
with st.form("login"):
    user=st.text_input("username")
    password=st.text_input("password",type="password")
    longin=st.form_submit_button("login")
if longin:
    st.success("logged in successfully")
st.divider()
col1,col2,col3=st.columns(3)
with col1:
    st.header("colmun 1")
    st.write("this is column 1")
with col2:    
    st.header("colmun 2")
    st.write("this is column 2")
with col3:
    st.header("colmun 3")
    st.write("this is column 3")
st.divider()
container=st.container()
container.write("inside container")
container.button("click")
data={
    'name':['srinika','varshitha','anurag'],
    'age':[24,22,23],
    'course':['python','java','c++']
}
st.table(data)
st.divider()
st.sidebar.title("Menu")
option = st.sidebar.selectbox(
"Choose page",
["Home", "About", "Contact"]
)
st.sidebar.write(f"You selected: {option}")
 