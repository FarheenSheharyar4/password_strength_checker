import streamlit as st
import re   #regex  is m numercapital r small hotah
st.set_page_config(page_title="Password Strengtg Checker By Farheen Sheharyar", page_icon="🔒",layout="centered")
#custom css
st.markdown("""
<style>
     .main {text-align: center;}
     .stTextInput {width: 60%; !important; margin: auto; }
     .stButton button {width: 50%; backgrond-color blue; color: white; font-size:18px;}
     .stButton button:hover {background-color: red;}
     </style>
     """,unsafe_allow_html=True) 

#page title and description

st.title("🔐Password Strength Generator") 
st.write("Enter your password below to check its security level. 🔍") 
password=st.text_input("Enter Your Password" ,type="password")

#function to check password strength
 
def check_password_strength(password):
     score = 0
     feedback = []
     if len(password) >= 8:
         score += 1 #increased by 1
     else:
         feedback.append("❌password should be **at least 8 character long**.")
         
     if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
          score += 1
     else:
         feedback.append(" ❌password should include **both uppercase(A-Z) and lowercase(a-z)**.")
     if re.search(r"\d",password):
         score += 1
     else:
         feedback.append("❌password should include **at least one number (0-9)**.")    
     #special characters
     if re.search(r"[!@#$%^&*]",password):
        score += 1
     else:
           feedback.append("❌ include **at least one special character (!@#$%^&*)**.")
    
    #display password strength result
     
     if score == 4:
        st.success("✅ **Strong Password** Your password is secure.")
     elif score == 3:
         st.info("⚠️ **Moderate Password** - Consider improving security by adding more feature") 
     else: 
         st.error("❌ **Week Password** - Follow the suggesti below to strength it.")  
    
     #feedback
     
     if feedback: 
       with st.expander("🔍**improve Your Password** "):        # expander multiple elements ko check krta h r hme details btata h 
        for tip in feedback:
             st.write(tip)  
     pasword = st.text_input("Enter Your Password:",type="pasword",help="Ensure your password is strong 🔐")
    #Button working
     if st.button("Check Strength"):
         if password:
             check_password_strength(password)
         else:
             st.warning("⚠️ Please enter a password first!")#show warning if password empty
