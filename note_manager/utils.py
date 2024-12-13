from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(100), nullable=False)
    note = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Note {self.titre} - {self.note}>'
