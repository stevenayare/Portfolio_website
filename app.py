from pathlib import Path
import streamlit as st
from PIL import Image

# Path setup
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Ved_latest.pdf"
profile_pic = current_dir / "assets" / "Ved.JPG"

# General settings
PAGE_TITLE = "Digital CV | Ved Ayare"
PAGE_ICON = "random"
NAME = "VED AYARE"
DESCRIPTION = """
Senior Year Student focused on Data Science, Finance and Risk Analysis at Mukesh Patel School of Technology Management and Engineering.
I'm keen on unraveling puzzles and crafting remedies. 
Open to venture into any avenue that promises learning prospects and forging connections with individuals across diverse domains. 
Dedicated to harnessing my talents to aid in the formulation and execution of pioneering data-powered solutions that propel business expansion and streamline decision-making processes. 
My core competencies and areas of study encompass Machine Learning, Statistics, Time-Series, and Finance.
"""
EMAIL = "VEDANT.AYARE99@nmims.in"

SOCIALS = {
    "LinkedIn": "http://www.linkedin.com/in/ved-ayare-b08a37214",
    "Github": "https://github.com/stevenayare"
}

PROJECTS = {
    "👨‍⚕️ Parkinson Detection": "https://github.com/stevenayare/Machine-Learning-and-Data-Science.git",
    "📈forecasting Covid19 mortality rates": "https://github.com/stevenayare/Time_Series-.git",
    "🪄Developed a Harry Potter Dashboard using Power-BI for accurate revenue calculation and blockbuster movie identification through ETL techniques.": "https://github.com/stevenayare/PowerBiDash.git",
    "👮 Crime Classification": "https://github.com/stevenayare/Crime_Classification.git"
}

# Streamlit settings
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.title("HEY THERE!!")

# Load CSS file
with open(css_file, "r") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# Load resume PDF
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# Load profile picture
profile_picture = Image.open(profile_pic)



# --- HERO ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_picture, width=200,)  # Use the image object here

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📁 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write("✉️", EMAIL)


# socials

st.write("#") # empty lines

cols = st.columns(len(SOCIALS))

for index,(platform, link) in enumerate(SOCIALS.items()):
    cols[index].write(f"[{platform}]({link})")
    
    
st.write("#") # empty lines

st.subheader("Skills")

st.write(f"""
         
 
Languages:

•	C++
•	Python
•   R



Frameworks and Libraries:

•	NumPy
•	Pandas
•	Matplotlib
•	scikit-learn
•   streamlit
•   Flask
•	TensorFlow
•	OpenCV
•	Dart



Tools:

•	MS PowerPoint
•	MS Excel
•	MS Word
•	MySQL
•   AWS 
•	Power-BI
•	Jira

 
Concepts and Techniques:

•	Time-Series Analysis
•	Machine Learning """) # empty lines    


## PROJECTS

st.write("#")
st.subheader("Projects")
for project,link in PROJECTS.items():
    st.write(f"[{project}]({link})")
    
    
    