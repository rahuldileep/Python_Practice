"""Assume we'll focus on the following workflows:
Text conversations only
Users
Add a user
Remove a user
Update a user
Add to a user's friends list
Add friend request
Approve friend request
Reject friend request
Remove from a user's friends list
Create a group chat
Invite friends to a group chat
Post a message to a group chat
Private 1-1 chat
Invite a friend to a private chat
Post a meesage to a private chat
No need to worry about scaling initially
"""

from abc import ABCMeta
from enum import Enum

class User():

	def __init__(self, user_id, name, passhash):
		self.user_id = user_id
		self.name = name
		self.passhash = passhash

	def messageuser(self,friend_id, message):
		pass

	def messagegroup(self, group_id, message):
		pass

	def sendfriendrequest(self, friend_id):
		pass

	def receivefriendrequest(self,friend_id):
		pass

	def rejectfriendrequest(self,friend_id):
		pass

	def approvefriendrequest(self, friend_id):
		pass



class UserService():
	def adduser(self,user_id):
		pass
	def removeuser(self,user_id):
		pass


class Chat(metaclass=ABCMeta):
	def __init__(self, chat_id):
		self.chat_id = chat_id
		self.users = []
		self.messages = []

class GroupChat(Chat):
	def addusers(self,user_id):
		pass
	def removeuser(self,user_id):
		pass

class PrivateChat(Chat):
	def __init__(self,user1,user2):
		super(PrivateChat,self).__init__()
		self.users.extend([user1,user2])


class Message():
	def __init__(self,m_id, message, timestamp):
		self.message_id = m_id
		self.message = message
		self.timestamp = timestamp

class AddRequest():
	def __init__(self,from_user,to_user,request_status, timestamp):
		self.from_user = from_user
		self.to_user = to_user
		self.request_status = request_status
		self.timestamp = timestamp

class RequestStatus(Enum):
	UNREAD = 0
	READ = 1
	ACCEPTED = 2
	REJECTED = 3