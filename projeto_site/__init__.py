import pymysql

# Aqui estamos fingindo que a versão é a 2.2.6 para o Django aceitar
pymysql.version_info = (2, 2, 6, "final", 0)

pymysql.install_as_MySQLdb()