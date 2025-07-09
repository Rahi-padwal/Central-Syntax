# Central-Syntax
This is a repository for HackOrbit 2025

A web-based platform for connecting, managing, and querying both local and cloud SQL databases, with AI-powered query assistance using the Groq API.  
### Features  
Connect to Local & Cloud Databases: Manage multiple MySQL (and MongoDB) databases from a single dashboard.  
Secure Authentication: User registration and login with encrypted cloud credentials.  
Dynamic Schema Visualization: View and explore database schemas in real time.  
AI-Powered Query Assistance: Use Groq API to convert natural language to SQL/MongoDB queries and vice versa.  
Safe Query Execution: Execute queries with robust error handling and feedback.  
Modern UI: Built with HTML, CSS, and JavaScript for a responsive experience.  

### Tech Stack  
-Backend: Python, Flask, PyMySQL, Flask-CORS, python-dotenv, pymongo  
-Frontend: HTML, CSS, JavaScript  
-Database: MySQL (local & cloud), MongoDB (optional)  
-AI Integration: Groq API (LLM for query conversion)  

### Setup Instructions  
1. Clone the Repository  
Apply to index.html  
Run  
2. Create and Activate a Virtual Environment  
Apply to index.html  
Run  
3. Install Dependencies  
Apply to index.html  
Run  
4. Set Up MySQL Database  
Install MySQL and create your databases (e.g., ai_sql_assistant, course_management).  
Update db_config.py and/or .env with your MySQL credentials:  
Apply to index.html  
Grant privileges to your MySQL user if needed.  
5. Set Up Groq API (for GenAI features)    
See SETUP_GROQ_API.md for full instructions.  
Quick steps:  
Get your API key from Groq Console  
Add to .env:  
Apply to index.html  
7. Configure Environment Variables   
Create a .env file in your project root:  
Apply to index.html  
8. Run the Application  
Apply to index.html   
Run  
The app will be available at http://localhost:5000/ (or as configured).  

### Usage  
-Register/Login: Access the portal via the login/register pages.  
-Add Databases: Use the dashboard to add local or cloud databases.  
-Query Workspace: Open the workspace to write and execute SQL queries.  
-AI Features: Use the AI assistant to convert natural language to SQL or explain queries (requires Groq API key).  
-Schema View: Visualize and explore your database schema.  

### Key Files and Directories  
-app.py — Flask app entry point  
-routes/ — API endpoints for authentication, database, chatbot, etc.  
-models/ — Database models and credential encryption  
-js/ — Frontend logic (dashboard, workspace, chatbot, etc.)  
-pages/ — HTML templates for all major pages  
-styles/ — CSS for UI/UX  
-utils/ — Encryption and prompt generation utilities  
-requirements.txt — All Python dependencies  

### Technologies Used  
-Python, Flask, PyMySQL, Flask-CORS, python-dotenv, pymongo  
-HTML, CSS, JavaScript  
-Groq API (LLM/GenAI)   
-MySQL, MongoDB  

### Troubleshooting  
-500 Internal Server Error:  
-Check your MySQL credentials in db_config.py and .env.  
-Ensure your MySQL server is running and accessible.  
-Check backend logs for detailed error messages.  

### Groq API Errors:  
-Ensure your API key is correct and set in .env.  
-Check for rate limits or missing key errors.
