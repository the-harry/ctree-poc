### iniciar o servidor
chmod +x ctreeEdge
./ctreeEdge


curl -u admin:ADMIN http://192.168.43.161:8081/ctree/api/v1/table/ctreeSQL -v

curl -u admin:ADMIN -d @table.json http://192.168.43.161:8081/ctree/api/v1/table/ctreeSQL/metrics -v

test insert:

curl -u admin:ADMIN -d @insert.json http://192.168.43.161:8081/ctree/api/v1/record/ctreeSQL/metrics -v


test SELECT:

curl -u admin:ADMIN http://192.168.43.161:8081/ctree/api/v1/record/ctreeSQL/metrics/1 -v
