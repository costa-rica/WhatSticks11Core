from .base import Base, session_scope
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, \
    Date, Boolean
from itsdangerous.url_safe import URLSafeTimedSerializer#new 2023
from datetime import datetime
from flask_login import UserMixin
from .config import config
import os
from flask import current_app


def default_username(context):
    return context.get_current_parameters()['email'].split('@')[0]


class Users(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    email = Column(String(255), unique = True, nullable = False)
    password = Column(Text, nullable = False)
    username = Column(Text, default=default_username)
    lat = Column(Float(precision=4, decimal_return_scale=None))
    lon = Column(Float(precision=4, decimal_return_scale=None))
    timezone = Column(Text)
    location_permission = Column(Boolean, default=False)
    location_reoccuring_permission = Column(Boolean, default=False)
    admin_users_permission = Column(Boolean, default=False)
    share = Column(Text)
    notes = Column(Text)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)
    oura_token_id = relationship("OuraToken", backref="oura_token_id", lazy=True)
    oura_sleep = relationship('OuraSleepDescriptions', backref='oura_sleep', lazy=True)
    loc_day = relationship('UserLocationDay', backref='user_loc_day', lazy=True)

    def get_reset_token(self):
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        return serializer.dumps({'user_id': self.id})

    @staticmethod
    def verify_reset_token(token):
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        try:
            payload = serializer.loads(token, max_age=1000)
            user_id = payload.get("user_id")
        except:
            return None
        with session_scope() as session:
            return session.query(Users).get(user_id)

    def __repr__(self):
        return f'Users(id: {self.id}, email: {self.email}, share: {self.share},' \
        f'location_reoccuring_permission: {self.location_reoccuring_permission})'


# class UserNotes(Base):
#     __tablename__ = 'user_notes'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     datetime_of_note=Column(DateTime)
#     note_title = Column(Text) #walking, running, empty is ok for something like mood
#     note_details = Column(Text)
#     source_name=Column(Text)
#     time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

#     def __repr__(self):
#         return f"UserNotes({self.id},datetime_of_note:{self.datetime_of_note}," \
#         f"note_title: {self.note_title}, note_details: {self.note_details}," \
#         f"time_stamp_utc: {self.time_stamp_utc})"

