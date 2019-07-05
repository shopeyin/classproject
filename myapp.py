from p_package import app


if __name__ == "__main__":
    
    #print(app.config['TITLE'])
    app.run(debug=True,port=8000)