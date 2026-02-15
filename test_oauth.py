from flask import Flask, request, redirect, session, url_for, jsonify  # Core Flask tools: routing, redirects, session storage, JSON responses
import os  # Used to read environment variables (secure credentials)
import requests  # Used to make HTTP calls to GitHub API
from dotenv import load_dotenv  # Loads variables from .env file into environment

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)  # Create Flask application instance
app.secret_key = "dev_secret_for_testing_only"  # Required for session storage (used to store OAuth token)

# Read GitHub credentials securely from environment
CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")

# Centralized GitHub endpoints 
GITHUB_TOKEN_URL = "https://github.com/login/oauth/access_token"
GITHUB_USER_API = "https://api.github.com/user"


# ---------- Home Route ----------
@app.route("/")  # Root URL
def home():
    # If user already authenticated, skip login and go directly to dashboard
    if "access_token" in session:
        return redirect(url_for("dashboard"))

    # Build GitHub OAuth authorization URL
    github_auth_url = (
        f"https://github.com/login/oauth/authorize"
        f"?client_id={CLIENT_ID}"
    )

    # Display login link
    return f'<a href="{github_auth_url}">Login with GitHub</a>'


# ---------- OAuth Callback ----------
@app.route("/callback")  # GitHub redirects here after user approves
def callback():
    code = request.args.get("code")  # Extract temporary authorization code from URL

    if not code:
        return jsonify({"error": "Authorization code not received"}), 400  # Client error if missing

    # Exchange authorization code for access token
    token_response = requests.post(
        GITHUB_TOKEN_URL,
        headers={"Accept": "application/json"},  # Request JSON response instead of form-encoded
        data={
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "code": code
        }
    )

    # Validate successful token exchange
    if token_response.status_code != 200:
        return jsonify({
            "error": "Token exchange failed",
            "details": token_response.text
        }), 500  # Server error if GitHub call fails

    token_json = token_response.json()  # Parse response body
    access_token = token_json.get("access_token")  # Extract token

    if not access_token:
        return jsonify({
            "error": "Access token missing",
            "response": token_json
        }), 500  # Defensive validation

    # Store access token in session for authenticated requests
    session["access_token"] = access_token

    return redirect(url_for("dashboard"))  # Redirect to protected area


# ---------- Protected Dashboard ----------
@app.route("/dashboard")
def dashboard():
    access_token = session.get("access_token")  # Retrieve token from session

    # Prevent access if not authenticated
    if not access_token:
        return redirect(url_for("home"))

    # Call GitHub API using stored token
    user_response = requests.get(
        GITHUB_USER_API,
        headers={"Authorization": f"Bearer {access_token}"}
    )

    # Validate API call success
    if user_response.status_code != 200:
        return jsonify({
            "error": "Failed to fetch user data",
            "details": user_response.text
        }), 500

    user_data = user_response.json()  # Parse user JSON

    # Render minimal dashboard with user data
    return f"""
    <h2>QA Dashboard</h2>
    <p><strong>Username:</strong> {user_data.get("login")}</p>
    <p><strong>User ID:</strong> {user_data.get("id")}</p>
    <p><strong>Public Repos:</strong> {user_data.get("public_repos")}</p>
    <a href="/logout">Logout</a>
    """


# ---------- Logout ----------
@app.route("/logout")
def logout():
    session.clear()  # Clear session to remove token
    return redirect(url_for("home"))  # Return to login page


if __name__ == "__main__":
    app.run(port=8001, debug=True, use_reloader=False)  # Start development server
