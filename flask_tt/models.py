from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return 'Role(%r)' % self.role_name

    def keys(self):
        return ('id', 'role_name')

    def __getitem__(self, item):
        return getattr(self, item)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(64), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return 'User(%r)' % self.user_name

    def keys(self):
        return ('id', 'user_name', 'role_id')

    def __getitem__(self, item):
        return getattr(self, item)
