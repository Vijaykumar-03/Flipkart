from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        fullname = request.form.get("fullname")
        email = request.form.get("email")
        mobile = request.form.get("mobile")

        print("Name:", fullname)
        print("Email:", email)
        print("Mobile:", mobile)

        # Do NOT print passwords in production logs

        return f"Welcome {fullname}! Registration Successful."

    return render_template("register.html")


@app.route("/health", methods=["GET"])
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
