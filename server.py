from flask import Flask, render_template, request, redirect, session
from database import register_new_user, check_login
from weather import get_weather, get_snow, detect_ski_type, detect_clothes_type
import map
import config

server = Flask("app")
server.secret_key = config.flask_secret_key


@server.route("/")
def main_page():
    return render_template("main.html")


@server.route("/home")
def home_page():
    try:
        email = session["email"]
        return render_template("homepage.html")
    except Exception:
        return redirect("/")


@server.route("/resort", methods=["POST"])
def resort():
    try:
        email = session["email"]
        resort_name = request.form.get("resort_name")
        weather = get_weather(resort_name)
        snow = get_snow(resort_name)

        if weather.get("error"):
            return weather["error"]["message"]

        try:
            avg_snow_depth = (int(snow["topSnowDepth"].removesuffix("in")) + int(
                snow["botSnowDepth"].removesuffix("in"))) / 2

            ski_type = detect_ski_type(avg_snow_depth)
        except Exception:
            ski_type = "No Info"


        try:
            temp = weather["current"]["temp_c"]
            clothes_type = detect_clothes_type(temp)
        except Exception:
            clothes_type = "No Info"


        try:
            map_info = map.get_map_info(resort_name)
            area_id = map_info[0]["properties"]["id"]
            website = map_info[0]["properties"]["websites"]
            if len(website) == 0:
                website = None
            else:
                website = website[0]
        except Exception:
            area_id = None


        return render_template("resort.html",
                               weather=weather,
                               snow=snow,
                               ski_type=ski_type,
                               clothes_type=clothes_type,
                               area_id=area_id,
                               website=website
                            )
    except Exception as e:
        print(e)
        return "Error! Try again later!"


@server.route("/login", methods=["post"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    if "reg" in request.form:
        try:
            register_new_user(email=email, password=password)
            session["email"] = email
            return redirect("/home")
        except Exception:
            return "Error! Try again!"
    elif "login" in request.form:
        if check_login(email=email, password=password):
            session["email"] = email
            return redirect("/home")
        else:
            return "Error! Try again!"


server.run(
    host=config.HOST,
    port=config.PORT
)
