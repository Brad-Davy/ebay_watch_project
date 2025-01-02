sudo docker run -e 'ACCEPT_EULA=Y' -e 'MSSQL_SA_PASSWORD=GreenHorses?!' -p 1433:1433 --name sqlserver -d mcr.microsoft.com/mssql/server:latest
