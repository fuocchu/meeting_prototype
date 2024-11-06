from flask import Flask, render_template, request
from parsing import parse_availability

app = Flask(__name__)


submissions = []

@app.route('/')
def index():
    return render_template('index.html', submissions=submissions)

@app.route('/submit', methods=['POST'])
def submit_availability():
    
    username = request.form['username']
    user_input = request.form['availability']
    
    
    availability = parse_availability(user_input)
    
    
    submissions.append({'username': username, 'availability': availability})

    return render_template('index.html', submissions=submissions)

@app.route('/suggest', methods=['POST'])
def suggest_meeting_time():
    
    common_times = find_common_times(submissions)
    return render_template('index.html', submissions=submissions, common_times=common_times)

def find_common_times(submissions):
    
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    common_times = {day: ["9 AM - 11 AM"] for day in days}

    
    for submission in submissions:
        user_availability = submission['availability']
        for day in days:
            if day in user_availability:
                common_times[day] = list(set(common_times[day]) & set(user_availability[day]))
            else:
                common_times[day] = []

    
    common_times = {day: times for day, times in common_times.items() if times}

    return common_times

if __name__ == "__main__":
    app.run(debug=True)
