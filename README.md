# Get Ansible inventory from Database CMDB
This commande produceansible  __hosts__ file in the actual directory


## Install command line
```
python setup.py install
```

## Usage
```
usage: ainv [-h] -u USER -p PASSWORD 
ainv: error: the following arguments are required: -u/--user, -p/--password
```
## Run
```
ainv -u dbuser -p $PASS 
```


## POC with SQLLite
```
sqlite3 inv.db
create table inventory(env varchar(3), service varchar(30), app varchar(30), host varchar(40));
INSERT INTO inventory ( env, service, app, host) values ('DEV','GOLD', 'MOLIS', 'lvn00839d');
INSERT INTO inventory ( env, service, app, host) values ('VAL','GOLD', 'MOLIS', 'mls3-dev');
INSERT INTO inventory ( env, service, app, host) values ('PROD','GOLD', NULL, 'mls4-prd');
INSERT INTO inventory ( env, service, app, host) values ('DEV','BRONZE', 'SLIMS', 'lvn00065d');
INSERT INTO inventory ( env, service, app, host) values ('DEV','BRONZE', 'SLIMS', 'lvn00232d');
INSERT INTO inventory ( env, service, app, host) values ('DEV','BRONZE', 'SLIMS', 'lvn00324d');
INSERT INTO inventory ( env, service, app, host) values ('PROD','BRONZE', 'SLIMS', 'lvn00325d');
```

this is an example output of based on **sqlite** table hostsDEV
```
GOLD:
  children:
    MOLIS:
      hosts:
        lvn00839d:
BRONZE:
  children:
    SLIMS:
      hosts:
        lvn00065d:
        lvn00232d:
        lvn00324d:
```

## Oracle Dialect
```
engine = create_engine("oracle+cx_oracle://scott:tiger@hostname:port/?service_name=myservice&encoding=UTF-8&nencoding=UTF-8")
```
