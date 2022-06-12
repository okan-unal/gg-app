from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'whisper'
app.config['MYSQL_DATABASE_DB'] = 'gg_app'
app.config['MYSQL_DATABASE_HOST'] = 'app-db-service.db.svc.cluster.local'  ## 'app-db-service.db.svc.cluster.local' FQDN FOR K8S
mysql.init_app(app)
