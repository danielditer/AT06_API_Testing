# The class will instantiate SMS_store objects, similar to an inbox or outbox on a cellphone
class SMS_Store:
    has_been_viewed = False
    inboxList = []
    indexList = []

    # Makes new SMS tuple, inserts it after other messages
    # in the store. When creating this message, its # has_been_viewed status is set False.
    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        self.add = (from_number, time_arrived, text_of_SMS, self.has_been_viewed)
        self.inboxList.append(self.add)
        return self.inboxList

    # Returns the number of sms messages in my_inbox
    def message_count(self):
        return len(self.inboxList)

    # Returns list of indexes of all not-yet-viewed SMS messages
    def get_unread_indexes(self):
        for i in range(0, len(self.inboxList)):
            if self.inboxList[i][3] == False:
                self.indexList.append(i)
        return self.indexList

    # Return (from_number, time_arrived, text_of_sms) for message[i]
    # Also change its state to "has been viewed".
    # If there is no message at position i, return None
    def get_message(self, i):
        for j in self.inboxList:
            if self.inboxList[i] == j:
                j = list(j)
                j[3] = True
                self.inboxList[i] = tuple(j)
                print(j)
                if j[3] == True:
                    return "Message Viewed" + "\nFrom:" + str(j[0]) + "\n Time:" + str(j[1]) + "\n Text: \t" + str(j[2])
            elif i > len(self.inboxList) or i < 0:
                return None

    # Delete the message at index i
    def delete(self, i):
        del self.inboxList[i]

    # Delete all messages from inbox
    def clear(self):
        del self.inboxList[::]


my_inbox = SMS_Store()
my_inbox.add_new_arrival("65324310", "14:00", "hey, what's up?")
my_inbox.add_new_arrival("71234567", "23:19", "how are you")
my_inbox.add_new_arrival("79876543", "08:05", "bye, see you later")
print(my_inbox.get_message(0))
print(my_inbox.get_message(1))
print(my_inbox.get_unread_indexes())
print(my_inbox.message_count())
my_inbox.delete(1)
print(my_inbox.message_count())
my_inbox.clear()
print(my_inbox.message_count())