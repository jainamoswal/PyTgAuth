# By @j_projects

# import modules
from flask import Flask, redirect, request
from pytgauth import verify

# define app & token
app = Flask(__name__)
token = 'xxx' #From @botfather

# define main route.
@app.route('/')
def main():
    if verify(request.args.to_dict(), token):
        return redirect('https://t.me/j_projects')
    return 'Bad request.'

# run the app via __name__ style
if __name__ == '__main__':
    app.run(debug=False)
