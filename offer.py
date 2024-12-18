import streamlit as st
import google.generativeai as genai

# Function to generate the offer letter
def generate_offer_letter(candidate_name, position_title, responsibilities, compensation, benefits):
    """
    Generate a formal offer letter based on the provided inputs.

    Args:
        candidate_name (str): Name of the candidate.
        position_title (str): Position title offered to the candidate.
        responsibilities (str): Responsibilities for the position.
        compensation (str): Compensation package offered.
        benefits (str): Benefits offered to the candidate.

    Returns:
        str: A generated offer letter.
    """
    prompt = f"""
    Write a formal and professional offer letter for the following candidate:

    - Candidate Name: {candidate_name}
    - Position Title: {position_title}
    - Responsibilities: {responsibilities}
    - Compensation Package: {compensation}
    - Benefits: {benefits}

    The letter should be polite, clear, and professional. It should outline the position, responsibilities, compensation, and benefits in a positive tone while maintaining a formal structure. The offer should conclude with an invitation to accept the offer and join the company.
    The letter should be formal, polite, and professional. It should outline the following:

    1. A warm introduction to the candidate.
    2. A clear statement of the position title and compensation package.
    3. A description of the candidate's responsibilities and expectations.
    4. A list of the benefits offered.
    5. Proposed start date and response deadline.
    6. Instructions on how to respond, including signing and returning the letter.
    7. A polite conclusion, expressing excitement for the candidate to join the team.

    Be sure to include the company header, formal tone, and include placeholders where necessary.
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

    st.title("Offer Letter Generator")
    st.subheader("Generate professional offer letters quickly and easily.")

    # Input fields for the user
    candidate_name = st.text_input("Enter the Candidate's Name:")
    position_title = st.text_input("Enter the Position Title:")
    responsibilities = st.text_area("Enter the Responsibilities:")
    compensation = st.text_area("Enter the Compensation Package:")
    benefits = st.text_area("Enter the Benefits:")

    # Button to generate the offer letter
    if st.button("Generate Offer Letter"):
        if not (candidate_name and position_title and responsibilities and compensation and benefits):
            st.warning("Please fill out all the fields!")
        else:
            st.info("Generating your offer letter...")
            offer_letter = generate_offer_letter(candidate_name, position_title, responsibilities, compensation, benefits)
            
            if offer_letter.startswith("Error"):
                st.error(offer_letter)
            else:
                st.success("Here's the offer letter:")
                st.write(offer_letter)

# Run the app
if __name__ == "__main__":
    main()
