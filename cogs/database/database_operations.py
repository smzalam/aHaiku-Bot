from cogs.database import database
from sqlalchemy import select, and_, insert, delete, exc, update
from sqlalchemy.orm import Session
from cogs.database import models

class DatabaseOperations:
    def __init__(self):
        self.db = next(database.get_db())

    def select_server(self, guild_id, get_row):
        try:
            result = self.db.execute(select(models.ServerStats).where(models.ServerStats.server_id == guild_id))
            result = self.db_clean(result)
            if get_row == 'all' and result != []:
                return result[0]
            elif result != []:
                return result[0][get_row]
            else: 
                return None
        except exc.SQLAlchemyError as e:
            return str(e.orig)

    def insert_server(self, guild_id, guild_name, channelID=None, channelName=None):
        try:
            result = self.db.execute(insert(models.ServerStats).values(server_id = guild_id, server_name = guild_name, channel_id = channelID, channel_name = channelName, streak = 0))
            self.db.commit()
            return True
        except exc.SQLAlchemyError as e:
            return str(e.orig)

    def update_channel(self, guild_id, channelID, channelName):
        try:
             result = self.db.execute(update(models.ServerStats).where(models.ServerStats.server_id == guild_id).values(channel_id = channelID, channel_name=channelName))
             self.db.commit()
        except exc.SQLAlchemyError as e:
            return str(e.orig)

    def update_streak(self, guild_id, streak):
        try:
             result = self.db.execute(update(models.ServerStats).where(models.ServerStats.server_id == guild_id).values(streak = streak))
             self.db.commit()
        except exc.SQLAlchemyError as e:
            return str(e.orig)
        
    def select_rules(self):
        try:
            result = self.db.execute(select(models.Rules))
            result = self.db_clean(result)
            return result[0]
        except exc.SQLAlchemyError as e:
            return str(e.orig)

    def select_syllables(self, guild_id):
        try:
            result = self.db.execute(select(models.Syllables).where(models.Syllables.server_id == guild_id))
            result = self.db_clean(result)
            return result[0]
        except exc.SQLAlchemyError as e:
            return str(e.orig)

    def insert_syllables(self, guild_id, one, two, three):
        try:
            result = self.db.execute(insert(models.Syllables).values(server_id = guild_id, line_one = one, line_two = two, line_three = three))
            self.db.commit()
            return True
        except exc.SQLAlchemyError as e:
            return str(e.orig)

    def update_syllables(self, guild_id, one, two, three):
        try: 
            server_stats = self.db.execute(update(models.Syllables).where(models.Syllables.server_id == guild_id).values(line_one = one, line_two = two, line_three = thr))
            self.db.commit()
            return True
        except exc.SQLAlchemyError as e:
            return str(e.orig)
            
    def delete_server(self, guild_id):
        try:
            result = self.db.execute(delete(models.Syllables).where(models.Syllables.server_id == guild_id))
            result = self.db.execute(delete(models.ServerStats).where(models.ServerStats.server_id == guild_id))
            self.db.commit()
            return True
        except exc.SQLAlchemyError as e:
            return str(e.orig)

    def db_clean(self, response):
        result = []
        for row in response.scalars():
            row_dict = row.__dict__
            result.append(row_dict.pop('_sa_instance_state', None).dict)
        return result

