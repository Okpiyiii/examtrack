import streamlit as st
import requests

# Constants
BACKEND_URL = "http://localhost:8000/predict"

st.set_page_config(page_title="Exam Anxiety Detector", page_icon="🧠", layout="centered")

st.title("🧠 AI-Based Exam Anxiety Detector")
st.markdown("""
This is a mental-wellness support system designed to identify and categorize exam-related anxiety.
*Disclaimer: This system is designed as a supportive tool and is not diagnostic.*
""")

st.write("---")

st.subheader("How are you feeling about your upcoming exams?")
user_input = st.text_area("Enter your pre-exam thoughts, reflections, or feelings here:", height=150)

if st.button("Analyze Anxiety Level", type="primary"):
    if user_input.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        with st.spinner("Analyzing your text..."):
            try:
                # Uncomment the following lines when the backend is fully integrated
                # response = requests.post(BACKEND_URL, json={"text": user_input})
                # if response.status_code == 200:
                #     result = response.json()
                #     anxiety_level = result.get("anxiety_level", "Unknown")
                # else:
                #     st.error("Error from backend server.")
                #     anxiety_level = "Error"
                
                # Mock response for now
                anxiety_level = "Moderate" 

                st.write("### Analysis Complete")
                
                if anxiety_level == "Low":
                    st.success("✅ **Anxiety Level: LOW**")
                    st.balloons()
                    st.info("💡 **Tip:** You seem to be in a good state of mind! Keep up your current study routine and make sure to get enough rest.")
                elif anxiety_level == "Moderate":
                    st.warning("⚠️ **Anxiety Level: MODERATE**")
                    st.info(
                        "💡 **Tip:** It's normal to feel some pressure. Try these quick tips:\n"
                        "- Take a 5-minute break and stretch.\n"
                        "- Practice deep breathing (inhale for 4s, hold for 4s, exhale for 6s).\n"
                        "- Review your materials systematically without cramming."
                    )
                elif anxiety_level == "High":
                    st.error("🚨 **Anxiety Level: HIGH**")
                    st.info(
                        "💡 **Tip:** Your text indicates significant stress.\n"
                        "- **Stop studying for a moment.** Step away from your desk.\n"
                        "- **Talk to someone:** Reach out to a friend, family member, or counselor.\n"
                        "- **Relaxation technique:** Listen to calming music or try targeted muscle relaxation."
                    )
                else:
                    st.error("Could not determine anxiety level.")

            except Exception as e:
                st.error(f"Connection error: {e}")
                st.info("Make sure the FastAPI backend is running on http://localhost:8000")
