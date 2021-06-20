from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import logging
from services.manager_service_impl import ManagerServiceImpl
from services.member_service_impl import MemberServiceImpl
from daos.manager_dao_impl import ManagerDaoImpl
from daos.member_dao_impl import MemberDaoImpl
from entities.member import Member
from entities.manager import Manager
from entities.reimbursement import Reimbursement
from exceptions.user_not_found import UserNotFound


app: Flask = Flask(__name__)
CORS(app)
logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(message)s')


member_dao = MemberDaoImpl()
manager_dao = ManagerDaoImpl()
manager_service = ManagerServiceImpl(manager_dao)
member_service = MemberServiceImpl(member_dao)


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
@app.route("/bugCatch/login", methods=["POST"])
def login():
    body = request.json
    user_name = body["userName"]
    password = body["password"]
    try:
        manager = manager_service.login(user_name, password)
        return jsonify(manager.as_json_dict()), 200
    except Exception:
        try:
            member = member_service.login(user_name, password)
            return jsonify(member.as_json_dict()), 200
        except Exception:
            return "Incorrect username or password", 404


# A second call made by the login button if the user is a manager. Returns all requests.
@app.route("/bugCatch/requests", methods=["GET"])
def requests():
    request_list = manager_service.view_all_requests()
    json_list = [l.as_json_dict() for l in request_list]
    return jsonify(json_list), 200


# A second call if the user is a member. Returns only requests belonging to them.
@app.route("/bugCatch/requests/<mem_id>", methods=["GET"])
def requests_by_user(mem_id: int):
        request_list = member_service.view_member_requests(mem_id)
        json_list = [l.as_json_dict() for l in request_list]
        if json_list:
            return jsonify(json_list), 200
        else:
            return "Member could not be found.", 404


# Returns a specific reimbursement.
# Managers should also see buttons to approve/deny new requests, but that is handled on the front end.
#@app.route("/bugCatch/member/<mem_id>/reim/<reim_id>", methods=["GET"])
#def retrieve_request(mem_id: int, reim_id: int):
#    reimbursement = member_service.view_request(mem_id, reim_id)
#    return jsonify(reimbursement.as_json_dict()), 200


# Takes in information from a reimbursement request,
# returns either a success or failure message.
# Front end logic should check each element to ensure everything is filled out.
# Optional: refresh the list of requests to include the new one.
@app.route("/bugCatch/member/<mem_id>/create", methods=["POST"])
def create_request(mem_id: int):
    try:
        body = request.json
        new_request = Reimbursement(body["reimbursementID"],
                                    body["reimbursementName"],
                                    body["sender"],
                                    body["reason"],
                                    body["amount"],
                                    body["date"],
                                    body["approved"],
                                    body["comment"],
                                    body["memberId"])
        new_request.fk_mem_id = mem_id
        member_service.create_request(new_request)
        return "Request created successfully.", 201
    except:
        return "Unable to create request.", 422


# Updates a request's status to "approved" or "denied", and may also have a comment.
# Returns a success or failure message.
@app.route("/bugCatch/member/<mem_id>/reim/<reim_id>/judge", methods=["PATCH"])
def judge_request(mem_id: int, reim_id: int):
    body = request.json
    verdict = body["verdict"]
    comment = body["comment"]
    try:
        manager_service.judge_request(mem_id, reim_id, verdict, comment)
        return "Success.", 200
    except:
        return "Failure.", 422


# Returns a list of numbers that represent various statistics about the requests
# made in the database.
@app.route("/bugCatch/stats", methods=["GET"])
def stats():
    #stats_list = []
    stats_list = manager_service.statistics()
    return jsonify(stats_list), 200


if __name__ == '__main__':
    app.run()
