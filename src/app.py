"""
app.py

This is the entry point for the website.

Description:
------------
main.py initializes and starts the web server, setting up all necessary routes,
middleware, and configurations required for the website. 

Usage:
------
To start the website, simply run this file:
    $ python main.py

Author:
-------
Julian Fong

Date:
-----
05/31/24

"""
from website import create_app

def main():
    app = create_app()
    app.run(debug=True)

if __name__ == "__main__":
    main()