import getpass
from main import create_app

app = create_app()

# Get the username of the computer
username = getpass.getuser()


if username == "colindavis":
    if __name__ == '__main__':
        app.run(host="127.0.0.1",port=5000, debug=True)
else:
    if __name__ == "__main__":
        app.run(host="192.168.1.55", port=8008, debug=True)
