from flask import Flask, request, jsonify, render_template
import logging
from services.manager_service import ManagerService
from services.member_service import MemberService
from exceptions.user_not_found import UserNotFound

app: Flask = Flask(__name__)
logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(message)s')


# member_dao = MemberDaoImpl()
# manager_dao = ManagerDaoImpl()
# manager_service = ManagerServiceImpl(manager_dao)
# member_service = MemberServiceImpl(member_dao)


# The landing page is just here to help build context leading up to the other functions of this site.
# Returns an HTML with no other logic.
@app.route("/", methods=["GET"])
def home_page():
    return render_template("GatorFanPage.html")


# A single page serves as a login, reimbursement viewer and manager, as well as a stats page.
# With no information being carried between webpages, there is no need to use session storage or cookies for this site.
# All data (including the login) is cleared when the page is refreshed, allowing you to quickly switch users to
# demo both members and managers.
# The initial routing to this 'God page' only returns an HTML.
@app.route("/bugCatch", methods=["GET"])
def main_page():
    return render_template("pokeviewer.html")


# Log-in request that looks for a user in both the member and manager tables,
# and then returns a list of requests depending on whether the user is an member or manager.
# The front-end will use the info to verify the login and determine which page to show.
# Should return a list with the user object and whether they're a member or manager.
@app.route("/bugCatch/login", methods=["GET"])
def login():
    body = request.json
    user_name = body["userName"]
    password = body["password"]
    try:
        ManagerService.login(user_name, password)
    except UserNotFound:
        try:
            MemberService.login(user_name, password)
        except UserNotFound:
            return "Incorrect username or password", 404


# Returns a specific reimbursement that managers can approve or deny.
# The front-end will change views and populate a form with the info given from this function.
@app.route("/bugCatch/manager/<man_id>/reim/<reim_id>", methods=["GET"])
def retrieve_man_request():
    pass


# Returns a specific reimbursement for members to view.
# Does not include approve/deny buttons on the front-end, nor will there be a comment box.
@app.route("/bugCatch/member/<mem_id>/reim/<reim_id>", methods=["GET"])
def retrieve_mem_request():
    pass


# Takes in information from a reimbursement request,
# returns either a success or failure message.
@app.route("/bugCatch/member/<mem_id>/create", methods=["POST"])
def create_request():
    pass


# Updates a request's status to "approved" or "denied", and may also have a comment.
# Returns a success or failure message.
@app.route("/bugCatch/manager/<man_id>/reim/<reim_id>/judge", methods=["PATCH"])
def judge_request():
    pass


# Returns a list of numbers that represent various statistics about the requests
# made in the database.
@app.route("/bugCatch/manager/<man_id>/stats", methods=["GET"])
def stats():
    pass


if __name__ == '__main__':
    app.run()
