from flask import Flask

app = Flas(__name__)

@app.route('/')
def index():
	return 'Hello world'

if __name__ == "__main__":
	app.run()