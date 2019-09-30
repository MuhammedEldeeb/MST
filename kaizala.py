import requests
import json

MIAN_GROUP_ID = "dba9fe96-598e-459d-b83a-6a85acf30acc@2"
PUBLIC_GROUP_ID = "711f8509-50fb-4f28-bb43-e6688726d28a@2"
PRIVATE_GROUP_ID = "67ecf920-669b-400a-b77e-cd0258c25372@2"
DEMO1_GROUP_ID = "c23fcf41-cd55-4f93-8013-11e178c633c3@2"
DEMO_PUBLIC_ID = "c5150d39-0df4-476c-ba7d-162fc6f60ca7@2"
ME_ID = "4e3e5ba6-07d4-411e-9cf4-8ac138a3b04b@2"


APPLICATION_ID = "e0f70fe7-b5c1-4d0c-8833-f6ec6c31c75e@2"
APPLICATION_SECRET = "3XIVOO04LW"
REFRESH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cm46bWljcm9zb2Z0OmNyZWRlbnRpYWxzIjoie1wicGhvbmVOdW1iZXJcIjpcIisyMDEwOTI4MDY3NjlcIixcImNJZFwiOlwiXCIsXCJ0ZXN0U2VuZGVyXCI6XCJmYWxzZVwiLFwiYXBwTmFtZVwiOlwiY29tLm1pY3Jvc29mdC5tb2JpbGUua2FpemFsYWFwaVwiLFwiYXBwbGljYXRpb25JZFwiOlwiZTBmNzBmZTctYjVjMS00ZDBjLTg4MzMtZjZlYzZjMzFjNzVlQDJcIixcInBlcm1pc3Npb25zXCI6XCI4LjRcIixcImFwcGxpY2F0aW9uVHlwZVwiOi0xLFwidG9rZW5WYWxpZEZyb21cIjoxNTY4NzMwNjgyNDkwLFwiZGF0YVwiOlwie1xcXCJHcm91cElkXFxcIjpcXFwiZGJhOWZlOTYtNTk4ZS00NTlkLWI4M2EtNmE4NWFjZjMwYWNjQDJcXFwiLFxcXCJBcHBOYW1lXFxcIjpcXFwibW9oYW1lZFxcXCIsXFxcIlVzZXJUZW5hbnRJZHNcXFwiOlxcXCJbXFxcXFxcXCIzMWM1OGQwOC01NDljLTQ2ZWYtYjExZS00MzliZmQ3MjZiMDhAMlxcXFxcXFwiXVxcXCJ9XCJ9IiwidWlkIjoiTW9iaWxlQXBwc1NlcnZpY2U6MjU0MmI5MzUtZDcxOS00ZjFhLWEzMzAtNzJhYTJjYjFmOWY1QDIiLCJ2ZXIiOiIyIiwibmJmIjoxNTY4NzMwNjgyLCJleHAiOjE2MDAyNjY2ODIsImlhdCI6MTU2ODczMDY4MiwiaXNzIjoidXJuOm1pY3Jvc29mdDp3aW5kb3dzLWF6dXJlOnp1bW8iLCJhdWQiOiJ1cm46bWljcm9zb2Z0OndpbmRvd3MtYXp1cmU6enVtbyJ9.dR5x4AFiixM67H_3-J3az5xHHzDKoxWe9v7J0QRCLV4"
URL = "https://kms2.kaiza.la/v1/"


class API():
    def __init__(self):

        #self.__access_token = self.__get_access_token()
        self.__access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cm46bWljcm9zb2Z0OmNyZWRlbnRpYWxzIjoie1wicGhvbmVOdW1iZXJcIjpcIisyMDEwOTI4MDY3NjlcIixcImNJZFwiOlwiXCIsXCJ0ZXN0U2VuZGVyXCI6XCJmYWxzZVwiLFwiYXBwTmFtZVwiOlwiY29tLm1pY3Jvc29mdC5tb2JpbGUua2FpemFsYWFwaVwiLFwiYXBwbGljYXRpb25JZFwiOlwiZTBmNzBmZTctYjVjMS00ZDBjLTg4MzMtZjZlYzZjMzFjNzVlQDJcIixcInBlcm1pc3Npb25zXCI6XCIyLjMwOjMuMzA6NC4xMDo2LjIyOjUuNDo5LjI6MTUuMzA6MTQuMzA6MTkuMzA6MjQuMzBcIixcImFwcGxpY2F0aW9uVHlwZVwiOjMsXCJkYXRhXCI6XCJ7XFxcIkdyb3VwSWRcXFwiOlxcXCJkYmE5ZmU5Ni01OThlLTQ1OWQtYjgzYS02YTg1YWNmMzBhY2NAMlxcXCIsXFxcIkFwcE5hbWVcXFwiOlxcXCJtb2hhbWVkXFxcIixcXFwiVXNlclRlbmFudElkc1xcXCI6XFxcIltcXFxcXFxcIjMxYzU4ZDA4LTU0OWMtNDZlZi1iMTFlLTQzOWJmZDcyNmIwOEAyXFxcXFxcXCIsXFxcXFxcXCI3YTYzZWQ3OC1mNzZlLTQ0YmEtOTdlMS00ZjI4NGE4ODJjMmZcXFxcXFxcIl1cXFwifVwifSIsInVpZCI6Ik1vYmlsZUFwcHNTZXJ2aWNlOjI1NDJiOTM1LWQ3MTktNGYxYS1hMzMwLTcyYWEyY2IxZjlmNUAyIiwidmVyIjoiMiIsIm5iZiI6MTU2OTc4ODQ5MywiZXhwIjoxNTY5ODc0ODkzLCJpYXQiOjE1Njk3ODg0OTMsImlzcyI6InVybjptaWNyb3NvZnQ6d2luZG93cy1henVyZTp6dW1vIiwiYXVkIjoidXJuOm1pY3Jvc29mdDp3aW5kb3dzLWF6dXJlOnp1bW8ifQ.CCs1iAHdBS0SQyWc7Dz60OhHeMPAkWouqxmvl2jXbXc"


    def __get_access_token(self):
        
        url = URL + "accessToken"
        data = ""

        headers = {
            'applicpayloadationId': APPLICATION_ID,
            'applicationSecret': APPLICATION_SECRET,
            'refreshToken': REFRESH_TOKEN,
            'cache-control': "no-cache"
        }

        response = requests.get(url, data=data, headers=headers)
        return response.json().get('accessToken')

    """
    dealing with private groups
    [
        + send message(s) to a specific group
        + send message(s) to all sub-groups of a specific group
    ]
    """

    def send_message_to_private_group(self , message , group_id = PRIVATE_GROUP_ID):
        """
        you can use this method to send new message(s) to both public and private groups
        """
        url = URL + "groups/" + group_id + "/messages"
        
        payload = {
            'message': message
        }
        data = json.dumps(payload)

        headers = {
            'accessToken': self.__access_token,
            'Content-Type': "application/json",
            'cache-control': "no-cache",
        }
        
        response = requests.post( url, data=data, headers=headers)
        
        return response.json()

    def send_message_to_private_sub_groups(self , message , parent_group_id = PRIVATE_GROUP_ID):
        sub_groups = self.get_sub_groups(parent_group_id).get('subGroups')
        for group in sub_groups:
            group_type = group.get('groupType')
            if group_type == 'Group':
                group_id = group.get('groupId')
                self.send_message_to_private_group(message , group_id)


    """
    dealing with public groups
    [
        + add subscriber(s) to a specific group  
        + remove subscriber(s) from a specific group
    ]
    """

    def add_subscribers_to_public_group(self , subscribers_list , group_id = DEMO_PUBLIC_ID ):

        url = URL + "groups/" + group_id +"/subscribers/add"

        payload = {
            'subscribers': subscribers_list
        }
        data = json.dumps(payload)

        headers = {
            'accessToken': self.__access_token,
            'Content-Type': "application/json",
            'cache-control': "no-cache",
        }

        response = requests.put(url, data=data, headers=headers)

        return response.json()

    def remove_subscribers_from_public_group(self , subscribers_list , group_id = DEMO_PUBLIC_ID ):

        url = URL + "groups/" + group_id + "/subscribers/remove"

        payload = {
            'subscribers':subscribers_list
        }
        data = json.dumps(payload)

        headers = {
            'accessToken': self.__access_token,
            'Content-Type': "application/json",
            'cache-control': "no-cache",
        }

        response = requests.put(url, data=data, headers=headers)

        return response.json()

    def send_message_to_public_group(self , message , subscribers_list
        ,group_id = DEMO_PUBLIC_ID
        ,send_to_all_subscribers = False
        ):

        """ be sure to all members of subscribers_list are alredy subscribers """
        self.add_subscribers_to_public_group(subscribers_list , group_id)

        """ now you can send message to all members in the subscribers_list """
        url = URL + "groups/" + group_id + "/messages"

        payload = {
            'Message': message,
            'subscribers': subscribers_list, 
            'sendToAllSubscribers': send_to_all_subscribers
        }
        data = json.dumps(payload)

        headers = {
            'accessToken': self.__access_token,
            'Content-Type': "application/json",
            'cache-control': "no-cache",
        }

        response = requests.post( url, data=data, headers=headers)

        return response.json()


    """
    dealing with both public and private groups
    [
        + create a group (public/private) by default is private ,
            you can make it public py passing "group_type" parameter with the value "ConnectGroup"
        + add memeber(s) to a specific group
        + remove member(s) from a spacific group
        + get all members of a specific group 
        + get all sub-groups from a specific group 
    ]
    """

    def create_group(self , group_name , memebers_list , group_type = "Group" 
            , welcome_message = "Welcome to the group created via sadeem company" 
            , short_desc = "Short description" , long_desc = "Long description"
        ):

        """
        create both public and private groups 
        by default it create a private group
        but you can create a public group by passing "group_type" parameter with the value "ConnectGroup"
        """

        url = URL + "groups"

        payload = {
            'name': group_name,
            'welcomeMessage': welcome_message,
            'members': memebers_list,
            'groupType':group_type, 
            'ShortDescriptionString': short_desc, 
            'LongDescriptionString': long_desc
        }
        data = json.dumps(payload)
        headers = {
            'accessToken': self.__access_token,
            'Content-Type': "application/json"
        }
        
        response = requests.post(url , data=data, headers=headers)

        return response.json()

    def add_members_to_group(self , members_list , group_id = PRIVATE_GROUP_ID):
        """
        you can use this method to add new member(s) to both public and private groups
        """
        
        url = URL + "groups/" + group_id +"/members"
        
        payload = {
            'members': members_list
        }
        data = json.dumps(payload)

        headers = {
            'accessToken': self.__access_token,
            'Content-Type': "application/json",
            'cache-control': "no-cache",
            }
        
        response = requests.put( url, data=data , headers=headers)
        
        return response.json()

    def remove_members_from_group(self , member_id = ME_ID , group_id = PRIVATE_GROUP_ID):
                
        url = URL + "groups/" + group_id + "/members/" + member_id

        payload = ""
        headers = {
            'accessToken': self.__access_token,
            'cache-control': "no-cache",
        }

        response = requests.delete( url, data=payload, headers=headers)

        return response.json()

    def get_members_of_group(self , group_id = PRIVATE_GROUP_ID):

        url = URL + "groups/" + group_id + "/members"

        payload = ""
        headers = {
            'accessToken': self.__access_token,
            'cache-control': "no-cache",
        }

        response = requests.get(url, data=payload, headers=headers)

        return response.json()

    def get_sub_groups(self , parent_group_id = PRIVATE_GROUP_ID):

        url = URL + "groups/" + parent_group_id +"/subGroups"

        payload = ""
        headers = {
            'accessToken': self.__access_token,
            'cache-control': "no-cache",
        }

        response = requests.get(url, data=payload, headers=headers)

        return response.json()

    def create_sub_group(self , subgroup_name, members_list
        ,parent_group_id = PRIVATE_GROUP_ID
        ,welcome_msg = "Welcome to sub group created via sadeem"
        ,group_type = "Group" , short_desc = "Short description" 
        ,long_desc = "Long description"
        ):

        """
        create both public and private sub-groups 
        by default it create a private sub-group
        but you can create a public sub-group by passing "group_type" parameter with the value "ConnectGroup"
        """

        result = self.create_group(subgroup_name , members_list , group_type , welcome_msg , long_desc , short_desc)
        subgroup_id = result.get('groupId')
        subgroups_list = [subgroup_id]

        url = URL + "groups/" + parent_group_id + "/subGroups"

        payload = {
            'subGroups':subgroups_list
        }
        data = json.dumps(payload)

        headers = {
            'accessToken': self.__access_token ,
            'Content-Type': "application/json",
            'cache-control': "no-cache",
        }

        response = requests.put( url, data=data, headers=headers)

        return response.json()
    
    