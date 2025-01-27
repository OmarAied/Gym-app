from website import create_app

app = create_app()

if __name__ == '__main__': #Only execute if ran and not imported
    app.run(debug=True) #Runs flask application