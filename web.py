from flask import Flask

app = Flask(__name__)


@app.get("/")
def home():
    return """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Glovo Delivery System</title>
</head>
<body>
    <h1>Glovo Delivery System</h1>
    <p>The web server is running. Restaurant browsing and ordering can be added here.</p>
</body>
</html>"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
