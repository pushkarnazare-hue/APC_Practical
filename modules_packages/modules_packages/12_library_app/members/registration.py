members_list = []

def register_member(member_id, name):
    members_list.append({"id": member_id, "name": name})

def display_members():
    for m in members_list:
        print(m)
