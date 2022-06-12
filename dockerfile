##PULL BASE IMAGE
FROM ubuntu:20.04
## CHECK UPDATES
RUN apt-get update
## INSTALL NGINX AND CURL PACKAGE
RUN apt-get install -y curl && apt-get install nginx -y
## WE NSTALL THE NECESSARY PACKAGES SO THAT WE CAN PULL THE CERTIFICATE
RUN apt-get -y install openssh-client && apt-get install sshpass -y && apt-get install rsync -y
## DEFINE WORKING DIRECTORY
WORKDIR /
## CREATE FOLDER
RUN mkdir certs
## WE PULL FROM CURRENT FOLDER OF KUBERNETES ADMINISTRATOR CERTIFICATES
RUN sshpass -p "hb2022" rsync -rvz -e 'ssh -o StrictHostKeyChecking=no -p 22' --progress  root@172.31.85.37:/etc/kubernetes/pki/*.crt /certs/
## WE LEARN THE EXPIRY DATES OF THE CERTIFICATES AND WRITE THEM TO THE LOG FILE.
RUN find /certs/ -type f -name "*.crt" -print|egrep -v 'apiserver-etcd-client.crt$'|xargs -L 1 -t  -i bash -c 'openssl x509  -noout -subject -dates  -in  {}' 1> /var/log/cert-checker.log
## EXPOSE PORTS.
RUN cp /var/log/cert-checker.log /var/www/html/index.nginx-debian.html
EXPOSE 80
EXPOSE 443
## DEFINE DEFAULT COMMAND.
#CMD service nginx start
CMD ["nginx", "-g", "daemon off;"]
