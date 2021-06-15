class Member:

    def __init__(self, mem_id: int, mem_name: str, mem_user: str, mem_pass: str):
        self.mem_id = mem_id
        self.mem_name = mem_name
        self.mem_user = mem_user
        self.mem_pass = mem_pass

    def as_json_dict(self):
        return{
            "memberId": self.mem_id,
            "memberName": self.mem_name,
            "userName": self.mem_user,
            "password": self.mem_pass
        }
