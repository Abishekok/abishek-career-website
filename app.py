from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Chennai, India',
    'salary': 'Rs.1000000'
}, {
    'id': 3,
    'title': 'Python Developer',
    'location': 'Madurai, India',
    'salary': 'Rs.1000000'
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Bengaluru, India',
    'salary': 'Rs.1000000'
}]


@app.route("/")
def hellp_abishek():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
