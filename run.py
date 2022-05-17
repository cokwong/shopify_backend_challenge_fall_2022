def main():
    """
    Runs app with backend and frontend

    :return: None
    """

    # Create API
    from api import create_app
    app = create_app()

    # Create frontend
    from frontend import create_webapp
    create_webapp(app)

    app.run(host="0.0.0.0")


if __name__ == "__main__":
    main()
