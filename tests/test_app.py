from src.app import StliteApp


def test_app_initialization():
    app = StliteApp()
    assert app.title == "My Stlite Application"
