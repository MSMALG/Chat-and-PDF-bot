# css = '''
# <style>
# .chat-message {
#     padding: 1.5rem; 
#     border-radius: 0.5rem; 
#     margin-bottom: 1rem; 
#     display: flex;
#     justify-content: space-around;
#     align-items: center;
# }
# .bot {
#     background-color: #FFFFFF;
#     color: #000;
#     border: 1px solid #228A5E;
# }
# .user {
#     background-color: #228A5E;
#     color: #000;
#     flex-direction: row-reverse;
# }
# .user .message{
#     text-align: end;
# }
# .chat-message .avatar img {
#   max-width: 4.9rem;
#   max-height: 4.9rem;
#   border-radius: 50%;
#   object-fit: cover;
# }
# .chat-message .message {
#   width: 80%;
#   padding: 0 1.5rem;
#   color: #000;
# }
# </style>
# '''


bot_template = '''
<div class="chat-message bot" style="padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex;justify-content: space-around; align-items: center; background-color: #FFFFFF; color: #000; border: 1px solid #228A5E;">
    <div class="avatar">
        <img src="https://www.clipartmax.com/png/middle/118-1184192_virtual-assistants-and-chat-bots-bot-icon-bot.png" 
        style="max-height: 4.5rem; max-width: 4.5rem; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message" style="text-align: justify; width: 80%; padding: 0 1.5rem; color: #000;">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user" style="padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex;justify-content: space-around; align-items: center; background-color: #228A5E; color: #000; flex-direction: row-reverse;">
    <div class="avatar">
        <img src="https://icons.veryicon.com/png/o/miscellaneous/two-color-icon-library/user-286.png"
        style="max-height: 4.5rem; max-width: 4.5rem; border-radius: 50%; object-fit: cover;">
    </div>    
    <div class="message" style="text-align: justify; width: 80%; padding: 0 1.5rem; color: #000;">{{MSG}}</div>
</div>
'''
