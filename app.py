import streamlit as st
import pandas as pd
from fuzzywuzzy import fuzz
from database import init_db, get_all_faqs, add_faq

# Initialize database & table automatically
init_db()

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

        best_match = None
        best_score = 0

        for q, a in faqs:
            q_lower = q.lower()
            score = fuzz.partial_ratio(query_lower, q_lower)  # similarity score
            if score > best_score:
                best_score = score
                best_match = a

        # Accept only good matches
        if best_score >= 60:
            response = best_match

        st.success(response)

# ---------------- Admin Page ----------------
elif choice == "Admin":
    st.subheader("⚙️ Admin Panel - Manage FAQs")

    # Show all FAQs
    faqs = get_all_faqs()
    if faqs:
        df = pd.DataFrame(faqs, columns=["Question", "Answer"])
        st.write("📋 Current FAQs in Database:")
        st.dataframe(df)
    else:
        st.info("ℹ️ No FAQs found. Please add some below.")

    # Add new FAQ
    st.write("---")
    st.subheader("➕ Add a New FAQ")
    new_q = st.text_input("Enter Question (keyword):")
    new_a = st.text_area("Enter Answer:")

    if st.button("Add FAQ"):
        if new_q and new_a:
            add_faq(new_q.lower(), new_a)
            st.success(f"✅ FAQ Added: '{new_q}'")
        else:
            st.error("⚠️ Please enter both question and answer.")
