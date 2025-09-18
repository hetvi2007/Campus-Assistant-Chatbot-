import streamlit as st
from database import get_all_faqs, add_faq

st.set_page_config(page_title="Campus Assistant Chatbot", page_icon="🎓")

st.title("🎓 Campus Assistant Chatbot")

# Sidebar for navigation
menu = ["Chatbot", "Admin"]
choice = st.sidebar.selectbox("Navigate", menu)

# ---------------- Chatbot Page ----------------
if choice == "Chatbot":
    st.subheader("💬 Ask me anything about college, exams, or syllabus!")

    faqs = get_all_faqs()
    query = st.text_input("Type your question:")

    if query:
        query_lower = query.lower()
        response = "❌ Sorry, I don't have an answer for that. Please contact admin."

        for q, a in faqs:
            if q in query_lower:
                response = a
                break

        st.success(response)

# ---------------- Admin Page ----------------
elif choice == "Admin":
    st.subheader("⚙️ Admin Panel - Add New FAQ")

    new_q = st.text_input("Enter Question (keyword):")
    new_a = st.text_area("Enter Answer:")

    if st.button("Add FAQ"):
        if new_q and new_a:
            add_faq(new_q.lower(), new_a)
            st.success(f"✅ FAQ Added: '{new_q}'")
        else:
            st.error("⚠️ Please enter both question and answer.")
