import pandas as pd

members = [
    ('Angel', 30, 'Male', 'Active'),
    ('Janice', 25, 'Female', 'Active'),
    ('Alex', 40, 'Male', 'Inactive')
]

df_members = pd.DataFrame(members, columns=['Name', 'Age', 'Gender', 'Membership Status'])


class Member:
    def __init__(self, id, name, age, membership_status):
        self.id = id
        self.name = name
        self.age = age
        self.membership_status = membership_status