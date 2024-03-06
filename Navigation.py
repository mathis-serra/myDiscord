from homepage.Chat import ChatPage

class NavigationManager:
    def __init__(self, screen):
        self.screen = screen

    def switch_to_messages(self, email):
        from homepage.MessagesInterface import Messages
        message_page = Messages(self.screen, email)
        message_page.run()

    def switch_to_chat(self, current_user_email, other_user_id):
        chat_page = ChatPage(self.screen, current_user_email, other_user_id)
        chat_page.run()