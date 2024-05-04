from flask import Flask

app = Flask(__name__)

app.config.from_object("config.DevelopmentConfig")

'''if app.config["NVE"] == "development":
    app.config.from_object("config.DevelopmentConfig")
elif app.config["NVE"] == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.ProductionConfig")'''

from app import views
