from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check-password', methods=['POST'])
def check_password():
    password = request.json['password']
    
    # Define password strength rules
    length_ok = len(password) >= 8
    uppercase_ok = any(c.isupper() for c in password)
    lowercase_ok = any(c.islower() for c in password)
    digit_ok = any(c.isdigit() for c in password)
    special_ok = any(c in '!@#$%^&*()-_=+[{]};:<>|./?\\' for c in password)
    
    # Calculate strength score
    strength = 0
    if length_ok:
        strength += 1
    if uppercase_ok and lowercase_ok:
        strength += 1
    if digit_ok:
        strength += 1
    if special_ok:
        strength += 1
    
    # Provide feedback messages based on strength score
    if strength <= 1:
        feedback = "Weak password"
    elif strength == 2:
        feedback = "Moderate password"
    elif strength == 3:
        feedback = "Good password"
    else:
        feedback = "Strong password"
    
    return jsonify({
        'strength': strength,
        'feedback': feedback
    })

if __name__ == '__main__':
    app.run(debug=True)
