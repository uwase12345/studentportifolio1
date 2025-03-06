import streamlit as st
import os
import json

# Set page title and icon
st.set_page_config(page_title="Student Portfolio", page_icon="🎓")

# Load or initialize profile data
def load_profile_data():
    if os.path.exists("profile_data.json"):
        with open("profile_data.json", "r") as file:
            return json.load(file)
    else:
        return {
            "name": "Uwase jeanne gentile",
            "location": "Rubavu, Rwanda",
            "field_of_study": "Computer Science, SWE",
            "university": "INES - Ruhengeri",
            "about_me": "I am a final-year Software Engineering student passionate about creating innovative solutions in healthcare, transportation, and public services through technology-driven systems.",
            "resume_path": "resume.pdf"
        }

# Save profile data
def save_profile_data(data):
    with open("profile_data.json", "w") as file:
        json.dump(data, file)

# Load profile data
profile_data = load_profile_data()

# Sidebar navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go To:", ["Home", "Projects","Timeline","Testimonials", "Skills", "Settings", "Contact"])

# Home section
if page == "Home":
    st.title("🎓 Student Portfolio")

    # Profile image
    uploaded_image = st.file_uploader("Upload Profile Picture", type=["jpg", "png"])
    if uploaded_image is not None:
        st.image(uploaded_image, width=150, caption="Uploaded Image")
    else:
       st.image("person.jpg", width=100, caption="Default Image")
        # Display student details
    st.write(f"👤 *Name:* {profile_data['name']}")
    st.write(f"📍 *Location:* {profile_data['location']}")
    st.write(f"📚 *Field of Study:* {profile_data['field_of_study']}")
    st.write(f"🎓 *University:* {profile_data['university']}")

    # Resume download button
    if os.path.exists(profile_data["resume_path"]):
        with open(profile_data["resume_path"], "rb") as file:
            resume_bytes = file.read()
        st.download_button(label="📄 Download Resume", data=resume_bytes, file_name="resume.pdf", mime="application/pdf")
    else:
        st.warning("⚠ Resume file not found. Please upload your resume.")

    st.markdown("---")
    st.subheader("About Me")
    st.write(profile_data["about_me"])
        # Student Testimonials Section
if page == "Testimonials":
    st.title("🗣 Student Testimonials")
    
    # Display example testimonial
    st.subheader("💬Testimonial:")
    st.write("Nadine is a brilliant problem solver! His final year project is truly innovative. – Mclement")
    
    st.markdown("---")
    
    # Allow classmates or mentors to leave testimonials
    st.subheader("✍ Leave a Testimonial")
    
    with st.form("testimonial_form"):
        name = st.text_input("Your Name")
        relationship = st.selectbox("Your Relationship", ["Classmate", "Mentor", "Teammate", "Other"])
        testimonial_message = st.text_area("Your Testimonial")
        
        submitted = st.form_submit_button("Submit Testimonial")
        if submitted:
            if name and testimonial_message:
                st.success(f"✅ Thank you, {name}! Your testimonial has been submitted.")
                # Display the testimonial after submission
                st.write(f"🗨 {testimonial_message} — {name} ({relationship})")
            else:
                st.error("⚠ Please fill in all fields before submitting.")
   
    # Display student details
    st.write(f"👤 *Name:* {profile_data['name']}")
    st.write(f"📍 *Location:* {profile_data['location']}")
    st.write(f"📚 *Field of Study:* {profile_data['field_of_study']}")
    st.write(f"🎓 *University:* {profile_data['university']}")

    # Resume download button
    if os.path.exists(profile_data["resume_path"]):
        with open(profile_data["resume_path"], "rb") as file:
            resume_bytes = file.read()
        st.download_button(label="📄 Download Resume", data=resume_bytes, file_name="resume.pdf", mime="application/pdf")
    else:
        st.warning("⚠ Resume file not found. Please upload your resume.")

    st.markdown("---")
    st.subheader("About Me")
    st.write(profile_data["about_me"])

# Projects section
elif page == "Projects":
    st.title("💻 My Projects")

    with st.expander("📊 ONLINE TICKET SELLING AND RESELLING PLATFORM FOR LOCAL EVENT"):
        st.write("An online platform for buying, selling, and reselling tickets for local events securely and efficiently using python")

    with st.expander("🤖 DESIGN AND IMPLEMENTATION OF ENTRY AND EXIT MANAGEMENT SYSTEM"):
        st.write("creating a secure and efficient system to monitor and manage the movement of individuals in and out of a facility using html,css and php")

    with st.expander("🌐 Interactive flashcard App for Teaching STEM concept to children"):
        st.write("An interactive flashcard app for teaching STEM concepts simplifies learning by using engaging, colorful cards with key ideas, visuals, and interactive quizzes to help children understand and retain science, technology, engineering, and mathematics concepts in a fun way.")

# Skills section
elif page == "Skills":
    st.title("⚡ Skills and Achievements")

    st.subheader("Programming Skills")
    skill_python = st.slider("Programming", 0, 100, 90)
    st.progress(skill_python)

    skill_js = st.slider("JavaScript", 0, 100, 75)
    st.progress(skill_js)

    skill_AI = st.slider("BI", 0, 100, 65)
    st.progress(skill_AI)

    st.subheader("Certifications")
    st.write("✔ ITORERO")
    st.write("✔ Urugerero training center")
    st.write("✔ AERG")
    st.write("✔ A2")
    st.write("✔ GREATER Project")

# Settings section
elif page == "Settings":
    st.title("🎨 Customize your profile")

    st.subheader("Upload a Profile Picture")
    uploaded_image = st.file_uploader("Choose a file", type=["jpg", "png"])
    if uploaded_image:
        st.image(uploaded_image, width=150)

    st.subheader("✍ Edit Personal Info")

    # Editable fields for personal information
    name = st.text_input("Name", value=profile_data["name"])
    location = st.text_input("Location", value=profile_data["location"])
    field_of_study = st.text_input("Field of Study", value=profile_data["field_of_study"])
    university = st.text_input("University", value=profile_data["university"])
    about_me = st.text_area("About Me", value=profile_data["about_me"])

    st.subheader("📄 Edit Resume")
    resume_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])
    if resume_file:
        with open("resume.pdf", "wb") as f:
            f.write(resume_file.getbuffer())
        profile_data["resume_path"] = "resume.pdf"
        st.success("Resume uploaded successfully!")

    # Save button to update the profile
    if st.button("Save Changes"):
        profile_data["name"] = name
        profile_data["location"] = location
        profile_data["field_of_study"] = field_of_study
        profile_data["university"] = university
        profile_data["about_me"] = about_me
        save_profile_data(profile_data)
        st.success("Profile updated successfully!")

# Contact section
elif page == "Contact":
    st.title("📬 Contact Me")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")

        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("✅ Message sent successfully")

    st.write("📧 Email: jeannegentilleu81@gmail.com")
    st.write("[🔗 LinkedIn](https://www.linkedin.com/in/yourprofile)")
    st.write("[📂 GitHub](https://github.com/uwase12345)")
    st.write("my phone number is: 0791647978, 0793624825")

st.sidebar.write("---")
st.sidebar.write("🔹 Made with ❤ using Streamlit")
