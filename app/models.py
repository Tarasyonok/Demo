from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True)
    file_name = Column(String(255), unique=True)
    file_hash = Column(String(64), unique=True)
    uploaded_at = Column(DateTime, default=func.now())

    tags = relationship("Tag", back_populates="image")


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), index=True)
    confidence = Column(Float)
    image_id = Column(Integer, ForeignKey("images.id"))

    image = relationship("Image", back_populates="tags")
