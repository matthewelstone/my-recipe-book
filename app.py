import os
from flask import (
    Flask, flash, render_template,
 redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)



@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username").capitalize()))
                    return redirect(url_for("profile", username=session["user"]))

            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
            
        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username= mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect("login.html")


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "description": request.form.get("description"),
            "image": request.form.get("image"),
            "type_name": request.form.get("type_name"),
            "servings": request.form.get("servings"),
            "cuisine_name": request.form.get("cuisine_name"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "ingredients": request.form.getlist("ingredients"),
            "steps": request.form.getlist("steps"),
            "author": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))   
    cuisines = mongo.db.cuisines.find().sort("cuisine_name", 1)
    types = mongo.db.types.find().sort("type_name", 1)
    return render_template("add_recipe.html", cuisines=cuisines, types=types)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        recipes = mongo.db.recipes
        recipes.update_one({"_id": ObjectId(recipe_id)}, {"$set": {
            "recipe_name": request.form.get("recipe_name"),
            "description": request.form.get("description"),
            "image": request.form.get("image"),
            "type_name": request.form.get("type_name"),
            "servings": request.form.get("servings"),
            "cuisine_name": request.form.get("cuisine_name"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "ingredients": request.form.getlist("ingredients"),
            "steps": request.form.getlist("steps"),
            "author": session["user"]}},
            upsert=True)

        flash("Recipe Successfully Updated")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    cuisines = mongo.db.cuisines.find().sort("cuisine_name", 1)
    types = mongo.db.types.find().sort("type_name", 1)
    return render_template("edit_recipe.html", recipe=recipe, cuisines=cuisines, types=types)


@app.route("/recipe_page.html/<recipe_id>", methods=["GET", "POST"])
def recipe_page(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    cuisines = mongo.db.cuisines.find().sort("cuisine_name", 1)
    types = mongo.db.types.find().sort("type_name", 1)
    return render_template("recipe_page.html", recipe=recipe, cuisines=cuisines, types=types)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))

@app.route("/get_cuisines")
def get_cuisines():
    cuisines = list(mongo.db.cuisines.find().sort("cuisine_name", 1))
    return render_template("cuisines.html", cuisines=cuisines)


@app.route("/add_cuisine", methods=["GET", "POST"])
def add_cuisine():
    if request.method == "POST":
        cuisine = {
            "cuisine_name": request.form.get("cuisine_name")
        }
        mongo.db.cuisines.insert_one(cuisine)
        flash("New Cuisine Added")
        return redirect(url_for("get_cuisines"))
    return render_template("add_cuisine.html")


@app.route("/edit_cuisine/<cuisine_id>", methods=["GET", "POST"])
def edit_cuisine(cuisine_id):
    if request.method == "POST":
        cuisines = mongo.db.cuisines
        cuisines.update_one({"_id": ObjectId(cuisine_id)}, {"$set": {
            "cuisine_name": request.form.get("cuisine_name")}},
            upsert=True)

        flash("Cuisine Successfully Updated")
        return redirect(url_for("get_cuisines"))

    cuisine = mongo.db.cuisines.find_one({"_id": ObjectId(cuisine_id)})
    return render_template("edit_cuisine.html", cuisine=cuisine)


@app.route("/delete_cuisine/<cuisine_id>")
def delete_cuisine(cuisine_id):
    mongo.db.cuisines.delete_one({"_id": ObjectId(cuisine_id)})
    flash ("Cuisine Sucessfully Deleted")
    return redirect(url_for("get_cuisines"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
