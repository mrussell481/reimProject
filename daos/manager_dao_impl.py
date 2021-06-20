from typing import List
from daos.manager_dao import ManagerDao
from entities.manager import Manager
from entities.reimbursement import Reimbursement
from utils.connection_util import connection


class ManagerDaoImpl(ManagerDao):

    def login(self, user_name: str, password: str) -> Manager:
        cursor = connection.cursor()
        sql = """select * from manager where man_user = '{}' and man_pass = '{}';""".format(user_name, password)
        cursor.execute(sql)
        record = cursor.fetchone()
        user = Manager(*record)
        return user

    def view_all_requests(self) -> List[Reimbursement]:
        cursor = connection.cursor()
        sql = """select * from reimbursement order by rb_id desc;"""
        cursor.execute(sql)
        records = cursor.fetchall()
        request_list = []
        for x in records:
            request_list.append(Reimbursement(*x))
        return request_list

    def judge_request(self, member_id: int, request_id: int, verdict: bool, comment: str) -> str:
        cursor = connection.cursor()
        sql = """update reimbursement set approved = {} where mem_id = {} and rb_id = {};""".format(verdict,
                                                                                                      member_id,
                                                                                                      request_id)
        cursor.execute(sql)
        if len(comment) > 0:
            sql = """update reimbursement set man_comment = '{}' where mem_id = {} and rb_id = {}""".format(comment,
                                                                                                        member_id,
                                                                                                        request_id)
            cursor.execute(sql)
        connection.commit()
        return "Successfully updated approval status."

    def statistics(self) -> list:

        # The values in stats_list are as follows:
        # 1. Member who made the most off of reimbursements
        # 2. How much that member made
        # 3. Member who made the most requests
        # 4. Number of requests they made
        # 5. Total number of requests
        # 6. Total amount of money made by members
        # 7. Approval Rate
        # 8. Average number of Requests per member
        # 9. Number of approved requests (used for the pie chart)
        stats_list = []

        # Step 1 and 2
        cursor = connection.cursor()
        sql = """select sender, sum(amount) from reimbursement group by sender;"""
        cursor.execute(sql)
        records = cursor.fetchall()
        richest_member_list = []
        for record in records:
            richest_member_list.append(record)
        richest_member_name = ""
        richest_member_amount = 0
        for record in richest_member_list:
            if record[1] > richest_member_amount:
                richest_member_amount = record[1]
                richest_member_name = record[0]
        stats_list.append(richest_member_name)
        stats_list.append(richest_member_amount)

        # Step 3 and 4
        sql = """SELECT sender, count(*)
                    FROM reimbursement
                    GROUP BY sender
                    order by count desc;"""
        cursor.execute(sql)
        requesting_member_record = cursor.fetchone()
        requesting_member = []
        for record in requesting_member_record:
            requesting_member.append(record)
        stats_list.append(requesting_member[0])
        stats_list.append(requesting_member[1])

        # Step 5
        sql = """select count(*) from reimbursement;"""
        cursor.execute(sql)
        request_count = cursor.fetchone()
        request_total = request_count[0]
        stats_list.append(request_count[0])

        # Step 6
        sql = """select sum(amount) from reimbursement;"""
        cursor.execute(sql)
        reim_amount = cursor.fetchone()
        stats_list.append(reim_amount[0])

        # Step 7
        sql = """select count(approved) from reimbursement where approved = true;"""
        cursor.execute(sql)
        accept_rate = cursor.fetchone()
        stats_list.append(round((accept_rate[0] / request_total)*100, 3))

        # Step 8
        sql = """select count(*) from site_member;"""
        cursor.execute(sql)
        member_count = cursor.fetchone()
        stats_list.append(round((request_total / member_count[0]), 3))

        # Step 9
        stats_list.append(accept_rate[0])

        return stats_list
