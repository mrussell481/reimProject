class Manager:

    def __init__(self, man_id: int, man_name: str, man_user: str, man_pass: str):
        self.man_id = man_id
        self.man_name = man_name
        self.man_user = man_user
        self.man_pass = man_pass

    def as_json_dict(self):
        return{
            "managerId": self.man_id,
            "managerName": self.man_name,
            "userName": self.man_user,
            "password": self.man_pass
        }
