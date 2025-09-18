from database import init_db, add_faq

# ✅ Step 1: Create the table (if it doesn't exist)
init_db()

# ✅ Step 2: Insert some sample FAQs
add_faq("exam timetable", "The exam timetable will be announced by the Examination Cell.")
add_faq("syllabus", "You can find the syllabus on the college website under Academics > Syllabus.")
add_faq("library", "The library is open from 9 AM to 6 PM, Monday to Saturday.")
add_faq("fees", "The last date for fee payment is 15th September. Pay via the college portal.")
add_faq("attendance", "Minimum 75% attendance is required to sit for exams.")

print("✅ Database initialized with sample FAQs")

