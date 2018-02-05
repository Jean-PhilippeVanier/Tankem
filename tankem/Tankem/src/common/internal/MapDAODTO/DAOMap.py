# -*- coding: utf-8 -*-
from DAO import DAO
from DTOTuile import DTOtuile
from DTOSpawn import DTOspawn
from DTOMap import DTOmap
from DTOListmap import DTOlistmap
import cx_Oracle


class DAOmaporacle():

    # Connection
    def __init__(self):
        self.connection = cx_Oracle.connect('e1384492', 'C',
                                            '10.57.4.60/DECINFO.edu')

        self.DTOlistmap = DTOlistmap()

    def read(self):
        # Get array maps
        curRead = self.connection.cursor()
        curRead = curRead.execute("SELECT * FROM %s " % ("EDITOR_NIVEAU"))
        arrayMapTmp = curRead.fetchall()
        curRead.close()

        # Append each map to DTOlistmap
        for map in arrayMapTmp:
            DTO_map_tmp = DTOmap(map[0],map[1],map[2],map[3],map[4],map[5],map[6],map[7])

            # Get tuiles of map
            curRead = self.connection.cursor()
            curRead.execute("SELECT * FROM EDITOR_TUILE WHERE id_niveau='%s'"
                            % (DTO_map_tmp.getId()))

            arrayTuilesTmp = curRead.fetchall()
            curRead.close()
            for tuile in arrayTuilesTmp:
                DTO_tuile_tmp = DTOtuile(tuile[0],tuile[1],tuile[2],tuile[3],tuile[4])
                DTO_map_tmp.appendTuile(DTO_tuile_tmp)

            # Get tuiles of map
            curRead = self.connection.cursor()
            curRead.execute("SELECT * FROM EDITOR_SPAWN WHERE id_niveau='%s'"
                            % (DTO_map_tmp.getId()))

            arraySpawnTmp = curRead.fetchall()
            curRead.close()
            for spawn in arraySpawnTmp:
                DTO_spawn_tmp = DTOspawn(spawn[0],spawn[1],spawn[2],spawn[3])
                DTO_map_tmp.appendTuile(DTO_spawn_tmp)

            # Ajouter map a la liste
            self.DTOlistmap.appendList(DTO_map_tmp)

        return self.DTOlistmap
