from pyngrok import ngrok

# Define the local server port
FLASK_PORT = 5000

# Start ngrok and get the public URL
public_url = ngrok.connect(FLASK_PORT).public_url

print(f"Public URL: {public_url}")
print("Your Flask app is now accessible remotely!")

# Keep ngrok running
input("Press Enter to exit...")
