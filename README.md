### iniciar o servidor
chmod +x ctreeEdge
./ctreeEdge&

pip install -r requirements.txt
pip freeze > requirements.txt

curl -u admin:ADMIN http://localhost:8081/ctree/api/v1/table/ctreeSQL -v

curl -u admin:ADMIN -d @table.json http://localhost:8081/ctree/api/v1/table/ctreeSQL/metrics -v

test insert:

curl -u admin:ADMIN -d @insert.json http://localhost:8081/ctree/api/v1/record/ctreeSQL/metrics -v


test SELECT:

curl -u admin:ADMIN http://localhost:8081/ctree/api/v1/record/ctreeSQL/metrics/1 -v

query find:

curl -u admin:ADMIN -d @find.json http://localhost:8081/ctree/api/v1/query/ctreeSQL/metrics/c_index?top=100
