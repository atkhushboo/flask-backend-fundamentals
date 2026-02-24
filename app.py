from flask import Flask

app=Flask(__name__)

@app.route("/")
def home ():
    return "Khushboo is runing Flask! "

@app.route("/sum")
def main():
    sum=2+3
    return f"Sum is {sum}"

@app.route("/info")
def info():
    return f"user details in user"

@app.route("/info/user")
def user():
    return f"name=Khushboo designation=SDE"


if __name__=="__main__":
    app.run(debug=True)