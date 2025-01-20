from server.models import db

class ResearchPaper(db.Model):
    __tablename__ = 'research_papers'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    authors = db.Column(db.String(255), nullable=False)
    published_date = db.Column(db.DateTime, nullable=False)
    abstract = db.Column(db.Text, nullable=False)