from flask import Flask

app = Flask(__name__)

@app.route("/")
def base_route():
    return "Highway to Hell"

@app.route("/hello/<float:number>", methods=["POST"])
def hello(number):
    if number <= 10:
        return f"hello {number}", 200 # status code
    if number >= 11:
        return f"hello {number}", 206 # partial content -> 206 status code



if __name__ == "__main__":
    app.run(host = "127.0.0.2", port = 5000, debug= True)

