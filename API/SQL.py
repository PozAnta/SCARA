import sqlite3


class Data:
    def __init__(self):
        self.conn = sqlite3.connect('C:\\Python\\Scara\\DB\\DB.db')
        self.cur = self.conn.cursor()
        self.table = 'Tests'
        self.column_name = 'Name'

    def insert_data(self, value_insert, table, column_name):
        ad = "insert into " + table + "(" + column_name + ") VALUES('" + value_insert + "')"
        self.cur.execute(ad)
        self.conn.commit()

    def update_data(self, location_data, name_data, table, column_name):

        self.cur.execute("UPDATE " + table + " SET " + column_name + "='%s' WHERE id='%s'" % (name_data, location_data))
        self.conn.commit()

    def read_column_data(self):
        # print("===*** " + self.table + " -> " + self.column_name + " ***===")
        select_str = "select " + self.column_name + ", " + self.column_name + " from " + self.table
        self.cur.execute(select_str)
        result = []
        rows = self.cur.fetchall()
        for row in rows:
            result.append(row[0])
        return result

    def read_by_id(self, id_search):
        select_str = "select " + self.column_name + ", " + self.column_name + " from " + self.table + " WHERE Id=" +\
                     id_search
        self.cur.execute(select_str)
        rows = self.cur.fetchall()
        result = []
        for row in rows:
            result.append(row[0])
        return result


# column_name = 'Name'
# location_val = 6
# update_val = "BadDay"
# read_column_data(table, column_name)
# read_by_id(table, column_name, "0")
