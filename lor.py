import streamlit as st
import google.generativeai as genai

# Function to generate a letter of recommendation
def generate_recommendation(name, job_title, relationship, strengths, reason_for_fit):
    """
    Generate a letter of recommendation based on the provided inputs.

    Args:
        name (str): Name of the person being recommended.
        job_title (str): Job title of the person being recommended.
        relationship (str): Relationship with the person being recommended.
        strengths (str): Strengths, skills, and achievements of the person.
        reason_for_fit (str): Why they are a good fit for the job.

    Returns:
        str: A generated letter of recommendation.
    """
    prompt = f"""
    Write a professional and compelling letter of recommendation for the following individual:

    - Name: {name}
    - Job Title: {job_title}
    - Relationship: {relationship}
    - Strengths, Skills, and Achievements: {strengths}
    - Why They Are a Good Fit: {reason_for_fit}

    The letter should be formal, well-structured, and emphasize their qualifications and suitability for the role they are applying for. Conclude with a positive and strong endorsement.
    """
    try:
        model = genai.GenerativeModel('gemini-1.5-pro-latest')
        response = model.generate_content([prompt])
        return response.text
    except Exception as e:
        return f"Error generating letter: {e}"

# Main Streamlit app
def main():
    # Configure the Gemini API key
    genai.configure(api_key="AIzaSyB46sAin3C4rTXYCmXkmfQho4fzNUMH6Rw")

    st.title("Letter of Recommendation Generator")
    st.subheader("Generate professional letters of recommendation with ease.")

    # Input fields for the user
    name = st.text_input("Enter the Name of the Person You Want to Recommend:")
    job_title = st.text_input("Enter Their Job Title:")
    relationship = st.text_input("What is Your Relationship with the Person?")
    strengths = st.text_area("Describe Their Strengths, Skills, and Achievements:")
    reason_for_fit = st.text_area("Why Are They a Good Fit for the Job?")

    # Button to generate the letter
    if st.button("Generate Letter"):
        if not (name and job_title and relationship and strengths and reason_for_fit):
            st.warning("Please fill out all the fields!")
        else:
            st.info("Generating your letter of recommendation...")
            letter = generate_recommendation(name, job_title, relationship, strengths, reason_for_fit)
            
            if letter.startswith("Error"):
                st.error(letter)
            else:
                st.success("Here's the letter of recommendation:")
                st.write(letter)

# Run the app
if __name__ == "__main__":
    main()
