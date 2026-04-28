import streamlit as st
import pandas as pd
import pickle
import time

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="IPL Predictor Pro", 
    page_icon="🏏", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. CACHED DATA LOADING
@st.cache_resource
def load_model():
    try:
        with open('ipl_score_model.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None

model = load_model()

# 3. DATA LISTS
venues = sorted(['Eden Gardens', 'Kimberley Oval', 'Sharjah Cricket Stadium', 'Wankhede Stadium', 
                 'Arun Jaitley Stadium', 'Holkar Cricket Stadium', 'Punjab Cricket Association Stadium',
                 'MA Chidambaram Stadium', 'Dubai International Cricket Stadium', 'M Chinnaswamy Stadium', 
                 'Narendra Modi Stadium', 'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium'])

teams = sorted(['Chennai Super Kings', 'Rajasthan Royals', 'Mumbai Indians', 'Delhi Capitals', 
                'Royal Challengers Bangalore', 'Sunrisers Hyderabad', 'Punjab Kings', 
                'Kolkata Knight Riders', 'Gujarat Titans', 'Lucknow Super Giants'])

# 4. SIDEBAR - MATCH SETUP
st.sidebar.header("🏆 Match Setup")
st.sidebar.info("Select the teams and the venue for the match.")

batting_team = st.sidebar.selectbox("Batting Team", teams)
bowling_team = st.sidebar.selectbox("Bowling Team", [t for t in teams if t != batting_team])
venue = st.sidebar.selectbox("Venue / Stadium", venues)

# 5. MAIN UI
st.title("🏏 IPL First-Innings Score Predictor")
st.markdown("---")

if model is None:
    st.error("🚨 **Model file not found!** Please ensure `ipl_score_model.pkl` is in the directory.")
else:
    # Use columns for a cleaner "Scorecard" look
    st.subheader("📊 Live Match Statistics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            current_score = st.number_input("Current Runs Scored", min_value=0, step=1, help="Total runs on the board")
            wickets = st.slider("Wickets Lost", 0, 9, 0)
            
    with col2:
        with st.container(border=True):
            overs = st.number_input("Overs Completed (> 5.0)", min_value=5.1, max_value=19.5, step=0.1, 
                                    help="Must be at least 5 overs completed")
            recent_runs = st.number_input("Runs in Last 5 Overs", min_value=0, step=1)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # 6. PREDICTION LOGIC
    if st.button("✨ Predict Final Score"):
        with st.spinner('Analyzing pitch conditions and historical trends...'):
            time.sleep(1) # Visual effect for the user
            
            # Construct DataFrame
            input_df = pd.DataFrame(
                [[venue, batting_team, bowling_team, current_score, wickets, overs, recent_runs]],
                columns=['venue', 'batting_team', 'bowling_team', 'current_score', 'wickets_lost', 'overs_completed', 'recent_overs_score']
            )
            
            try:
                prediction = int(model.predict(input_df)[0])
                
                # Output Section
                res_col1, res_col2 = st.columns([2, 1])
                
                with res_col1:
                    st.success(f"## 🎯 Predicted Total: {prediction}")
                    st.write(f"Based on current momentum, {batting_team} is projected to finish around this score.")
                
                with res_col2:
                    st.metric(label="Expected Range", value=f"{prediction-10}-{prediction+10}")
                
                st.balloons()
                
            except Exception as e:
                st.error(f"Error in calculation: {e}")

# 7. FOOTER
st.markdown("---")
st.caption("Developed for IPL Analytics Portfolio | Data source: Historical IPL Matches")
