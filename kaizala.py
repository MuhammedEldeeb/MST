import requests
import json

PUBLIC_GROUP_ID = "711f8509-50fb-4f28-bb43-e6688726d28a@2"
PRIVATE_GROUP_ID = "67ecf920-669b-400a-b77e-cd0258c25372@2"

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
        + create as a sub-group of the main group organization
        + add memeber(s) to a specific group
        + send message(s) to a spacific group  
    ]
    """

    def create_group(self , group_name , memebers_list , group_type = "Group" 
            , welcome_message = "Welcome to the group created via sadeem company" 
            , short_desc = "Short description" , long_desc = "Long description"
        ):
        
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

    def add_members_to_group(self , members_list , group_id = PUBLIC_GROUP_ID):
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

    def send_message_to_group(self , message , group_id = PRIVATE_GROUP_ID):
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

    """
    dealing with public groups
    [
        + create a public group as a sub-group of the main group organization
        + add memeber(s) to a specific group
        + add subscriber(s) to a specific group
        + send message(s) to a spacific group  
    ]
    """

    def create_public_group(self , name , members_list , welcome_msg = "Welcome to public group created via sadeem" , group_type = "ConnectGroup" ):
        url = URL + "groups"
        
        payload = {
            'name': name, 
            'welcomeMessage': welcome_msg, 
            'members':members_list, 
            'groupType': group_type
        }
        data = json.dumps(payload)

        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + self.__access_token,
            'cache-control': "no-cache",
        }
        
        response = requests.post(url, data=data, headers=headers)
        
        return response.json()

    def add_subscribers_to_public_group(self , subscribers_list , group_id = PUBLIC_GROUP_ID):
        pass