import streamlit as st

st.set_page_config(page_title="Campus Assistant Chatbot", page_icon="🎓")

st.title("🎓 Campus Assistant Chatbot")
st.write("Hello! I'm your Campus Assistant. Ask me anything about college, exams, or syllabus.")

# Simple FAQ knowledge base (dictionary)
faq = {
    "exam timetable": "The exam timetable will be announced by the Examination Cell.",
    "syllabus": "You can find the syllabus on the college website under Academics > Syllabus.",
    "library": "The library is open from 9 AM to 6 PM, Monday to Saturday.",
    "fees": "The last date for fee payment is 15th September. Pay via the college portal.",
    "attendance": "Minimum 75% attendance is required to sit for exams."
}

# User input
query = st.text_input("Type your question:")

if query:
    # Convert query to lowercase for matching
    query = query.lower()
    response = "Sorry, I don't have an answer for that. Please contact admin."
    
    for key in faq:
        if key in query:
            response = faq[key]
            break

    st.success(response)

