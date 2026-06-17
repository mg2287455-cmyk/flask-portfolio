from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Monu Gupta Portfolio</title>

<style>
body{
    margin:0;
    font-family:Arial,sans-serif;
    background:#f4f4f4;
}

header{
    background:#4CAF50;
    color:white;
    text-align:center;
    padding:30px;
}

nav{
    background:#333;
    padding:15px;
    text-align:center;
}

nav a{
    color:white;
    text-decoration:none;
    margin:15px;
    font-weight:bold;
}

nav a:hover{
    color:yellow;
}

.container{
    text-align:center;
    padding:40px;
}

.container a{
    text-decoration:none;
    color:blue;
    font-weight:bold;
}

footer{
    background:#333;
    color:white;
    text-align:center;
    padding:15px;
    margin-top:20px;
}
</style>
</head>

<body>

<header>
    <h1>Monu Gupta</h1>
    <p>B.Tech Electronics & Communication Engineering</p>
    <p>Python | Robotics | Web Development | Cybersecurity</p>
</header>

<nav>
    <a href="/">Home</a>
    <a href="/about">About</a>
    <a href="/skills">Skills</a>
    <a href="/projects">Projects</a>
    <a href="/contact">Contact</a>
</nav>

<div class="container">
    <h2>{{ message }}</h2>
    <p>{{ intro|safe }}</p>
</div>

<footer>
    <p>© 2026 Monu Gupta</p>
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        html,
        message="Welcome to My Portfolio",
        intro="""
        Hi, I am Monu Gupta from Ghazipur, Uttar Pradesh.
        I am a B.Tech Electronics & Communication Engineering student.
        I am interested in Python, Robotics, Web Development and Cybersecurity.
        """
    )

@app.route("/about")
def about():
    return render_template_string(
        html,
        message="About Me",
        intro="""
        I am pursuing B.Tech in Electronics & Communication Engineering.
        I enjoy building projects in Python, Robotics and Cybersecurity.
        I am continuously learning new technologies and practical skills.
        """
    )

@app.route("/skills")
def skills():
    return render_template_string(
        html,
        message="My Skills",
        intro="""
        Python<br>
        C Programming<br>
        HTML & CSS<br>
        Flask<br>
        Arduino<br>
        Robotics<br>
        Cybersecurity Fundamentals<br>
        Linux Basics<br>
        Networking Basics<br>
        Git & GitHub
        """
    )

@app.route("/projects")
def projects():
    return render_template_string(
        html,
        message="My Projects",
        intro="""
        Human Following Robot<br>
        Wireless Mobile Charging System<br>
        QR Code Generator using Python
        """
    )

@app.route("/contact")
def contact():
    return render_template_string(
        html,
        message="Contact Me",
        intro='''
        📧 Email:
        <a href="mailto:monuguptasittu@gmail.com">
        monuguptasittu@gmail.com</a>

        <br><br>

        💼 LinkedIn:
        <a href="https://www.linkedin.com/in/monu-gupta-ece" target="_blank">
        Visit My LinkedIn</a>

        <br><br>

        💻 GitHub:
        <a href="https://github.com/mg2287455-cmyk" target="_blank">
        Visit My GitHub</a>
        '''
    )

if __name__ == "__main__":
    app.run(debug=True)
