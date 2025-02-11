from flask import current_app
from app import db

class Video(db.Model):
    video_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    release_date = db.Column(db.DateTime, nullable=True)
    total_inventory = db.Column(db.Integer)
    available_inventory = db.Column(db.Integer, default=0)
    
    def to_json(self):
        video = {
            "id": self.video_id,
            "title": self.title,
            "release_date": self.release_date,
            "total_inventory": self.total_inventory,
            "available_inventory": self.available_inventory
        }
        return video
      
    @classmethod  
    def from_json(cls, json_file):
        return cls(**json_file)