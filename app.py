import psutil

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
# / is the home path 
def index():

    cpu_percent = psutil.cpu_percent()
    mem_percent=psutil.virtual_memory().percent
    Message=None

    if cpu_percent >80 or mem_percent > 80:
        Message="HIGH CPU or Memory Utilization detected. Please scale up"
    return render_template("index.html",cpu_percent_from_index_html=cpu_percent,mem_percent_from_index_html=mem_percent,message=Message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


