from sqlalchemy import Date, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config.db import Base

class Photo(Base):
    __tablename__ = 'photos'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    url: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=False)
    owner: Mapped["User"] = relationship("User", back_populates="photos")
    photo_tags: Mapped[list["Photo_tag"]] = relationship("Photo_tag", back_populates="photo")
    comments: Mapped[list["Comment"]] = relationship("Comment", back_populates="photo")

class Photo_tag(Base):
    __tablename__ = 'photo_tag'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    photo_id: Mapped[int] = mapped_column(Integer, ForeignKey('photos.id'), nullable=False)
    tag_id: Mapped[int] = mapped_column(Integer, ForeignKey('tags.id'), nullable=False)
    photo: Mapped["Photo"] = relationship("Photo", back_populates="photo_tags")
    tag: Mapped["Tag"] = relationship("Tag", back_populates="photo_tags")

class Tag(Base):
    __tablename__ = 'tags'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    photo_tags: Mapped[list["Photo_tag"]] = relationship("Photo_tag", back_populates="tag")

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String)
    photos: Mapped[list["Photo"]] = relationship("Photo", back_populates="owner")

class Comment(Base):
    __tablename__ = 'comments'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    comment_text: Mapped[str] = mapped_column(String)
    photo_id: Mapped[int] = mapped_column(Integer, ForeignKey("photos.id"), nullable=True)
    photo: Mapped["Photo"] = relationship("Photo", back_populates="comments")
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="comments")