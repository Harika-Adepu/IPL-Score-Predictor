# IPL-Score-Predictor
Live App: https://ipl-score-predictor-pro.streamlit.app/

IPL Score Predictor Pro is an end-to-end Machine Learning pipeline designed to predict the final innings score of an IPL match in real-time. 
By leveraging historical ball-by-ball data and current match dynamics, the system provides highly stable predictions to help fans and analysts understand game momentum.

🚀 What it Does
Real-Time Prediction: Processes live match inputs—including current score, wickets, overs, and teams—to forecast the final total.  
Dynamic Feature Engineering: Utilizes advanced features like wicket-loss momentum and run-rate volatility to capture the shifting pressure of the mid-innings.  
Fast Execution: Built with a FastAPI backend and caching strategies to deliver predictions in under 200ms.  
User-Friendly Interface: Offers an interactive web dashboard developed using Streamlit for seamless user interaction.  

🛠️ Technical Highlights
Model: Random Forest Regression trained on 200k+ historical records.  
Accuracy: Achieved a 93% accuracy rate with a Mean Absolute Error (MAE) of less than 15 runs.  
Stack: Python (Pandas, NumPy, Scikit-learn), FastAPI, Streamlit.  

💡 Benefits of this Project
Strategic Insights: Helps analysts and enthusiasts quantify how a sudden fall of wickets or a high-scoring over impacts the projected total.  
Data-Driven Decision Making: Provides a statistical baseline for comparing current team performance against historical trends.  
Scalable Architecture: Demonstrates how to transition a local ML script into a production-ready web application using MLOps best practices.  
High Performance: Optimized for efficiency, ensuring that users receive instant updates without lag during fast-paced matches.  
