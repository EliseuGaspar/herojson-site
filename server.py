from src.app import app

if __name__ == '__main__':
	app.run(
		port=2000,
		host='0.0.0.0',
		debug=True
	)