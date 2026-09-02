import streamlit as st
import google.generativeai as genai
from PIL import Image

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="🫀Cardio Decoder ",
    page_icon="🫀🔍",
    layout="wide"
)

st.title("🫀🔍Cardio Decoder")
st.write("Upload a image and get insights using Gemini 3.6 Flash.")

# -----------------------------
# Gemini API Configuration
# -----------------------------
GOOGLE_API_KEY = "AQ.Ab8RN6I8YPTlSiDIOySHIW5bbr3C355CjoSh3HIy296LJWuorg"

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-3.6-flash")

# -----------------------------
# Image Upload
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload a Image",
    type=["jpg", "jpeg", "png"]
)

# -----------------------------
# Analyze Button
# -----------------------------
if uploaded_file is not None:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:
        st.image(image, caption="Uploaded Image", use_container_width=True)

    with col2:

        if st.button("Analyze Image"):

            with st.spinner("Analyzing image..."):

                prompt = """
                You are an AI science tutor specializing in interpreting educational diagrams.

                Analyze the uploaded science diagram carefully.

                The diagram may represent biology, chemistry, physics, environmental science, or another scientific topic.

                Perform the following tasks:

                1. Identify the scientific topic.
                2. Identify the concept represented.
                3. Identify every clearly visible label.
                4. Explain each label.
                5. Explain the relationship between the labeled components.
                6. Describe the process represented by the diagram step by step.
                7. Explain the concept in beginner-friendly language.
                8. Identify important scientific terminology.
                9. Create an examination-oriented summary.
                10. Generate 5 viva questions and answers.
                11. Generate 5 MCQs with answers.

                If a label is unclear, mark it as [unclear].
                Never invent missing labels.

                OUTPUT FORMAT:

                ## 🔬 Scientific Topic
                ...

                ## 🧩 Diagram Explanation
                ...

                ## 🏷️ Labels

                | Label | Explanation |
                |---|---|
                | | |

                ## 🔄 Process
                1. ...
                2. ...
                3. ...

                ## 📖 Important Terms
                | Term | Meaning |
                |---|---|

                ## 🎯 Examination Summary
                ...

                ## 🗣️ Viva Questions

                ### Q1
                **Answer:** ...

                Repeat for five questions.

                ## 🧠 MCQs

                ### Q1
                A. ...
                B. ...
                C. ...
                D. ...

                **Answer:** ...

                Repeat for five questions.
                """

                response = model.generate_content(
                    [prompt, image]
                )

                st.subheader("Analysis Result")
                st.write(response.text)
