# -*- coding:utf-8 -*-
 #programme qui prends les données du csv, les sanitize et les envoie a la base de donnée si tout est correct (+gestion messages d'erreur)

import common

DAOracle = common.internal.BalanceDAODTO.DAOBalanceOracle.DAOBalanceOracle()
DAOcsv = common.internal.BalanceDAODTO.DAOBalanceCsv.DAOBalanceCsv()


DTO = DAOcsv.read("test.csv")
sanitizer = common.internal.BalanceDAODTO.SanitizerBalance.SanitizerBalance(DTO, True, False)
booleen = sanitizer.sanitizeDto()
if(booleen):
    try:
        DAOracle.update(DTO)
        print("update succesful")
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print("Erreur de commande")
        print(error.code)
        print(error.message)
        print(error.context)

else:
    print ("La base de donnee Oracle ne sera pas updater tant que les valeurs ne sont pas bonnes")
