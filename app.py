import kaizala

api = kaizala.API()
#print(api.add_subscribers_to_public_group(['+201129988266']))
print(api.send_message_to_public_group("message to SOME subscribers after updates" , ['+20115191227' , '+201129988266']))