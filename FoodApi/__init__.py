from flask import Flask

# Always use relative import for custom module
from .main import app


if __name__ == "__main__":
    app.run(debug=True)
