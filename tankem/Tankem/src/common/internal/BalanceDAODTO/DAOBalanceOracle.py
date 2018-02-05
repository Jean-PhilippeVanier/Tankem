# -*- coding: utf-8 -*-
from DAOBalance import DAOBalance
from DTOBalance import DTObalance
import cx_Oracle
from SingletonDBConnection import SingletonDBConnection

class DAOBalanceOracle(DAOBalance):

    def __init__(self):
        self.connection = SingletonDBConnection().getConnection()

    def read(self, table_name):
        table_name = table_name.upper()
        tmpDTO = DTObalance()
        curRead = self.connection.cursor()

        curRead = curRead.execute("SELECT column_name FROM user_tab_columns WHERE table_name = '%s'" % (table_name))
        keysList = curRead.fetchall()

        curRead.close()

        for key in keysList:
            curRead = self.connection.cursor()
            curRead.execute("SELECT %s FROM %s" % (key[0],table_name))
            value = curRead.fetchall()

            tmpDTO.setValue(key[0], value[0][0])

            curRead.close()

        tmpDTO.setValue("TABLE_NAME", table_name)

        return tmpDTO

    def update(self, DTO):
        tmpDict = DTO.getDictionary()
        tmpID = DTO.getValue("ID")
        table_name = DTO.getValue("TABLE_NAME")

        for key,value in tmpDict.items():
            if(key != "ID" and key != "TABLE_NAME"):
                curRead = self.connection.cursor()
                curRead.execute("UPDATE %s SET %s = %s WHERE id = %s" % (table_name,key,value,tmpID))
                curRead.close()
        self.connection.commit()

