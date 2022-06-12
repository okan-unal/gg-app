Steps:

1. Build docker file  
 ## Create Dockerfile , file name is need to be "dockerfile"
<<
 FROM centos:7
 MAINTAINER "okanunal" <okanunall@hotmail.com>
 RUN yum update -y && yum -y install yum-utils && yum -y groupinstall development && yum -y install https://repo.ius.io/ius-release-el7.rpm
 RUN yum install -y python36u
 COPY ./APP /APP
 RUN pip3 install flask_table
 RUN pip3 install pymysql
 RUN pip3 install flask-mysql
 EXPOSE 8585
 CMD [ "python3", "./APP/main.py" ]
>>
## The APP folder must be in the same folder as the dockerfile.
## "docker build . -t <imagename:tag>"  ## This code needs to be run alongside your dockerfile

2. Install MySql, Create MySQL DB  and run the following query: ## This migration is necessery

```
CREATE TABLE `tbl_user` (
  `user_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `user_email` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `user_password` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
```
3. RUN container

docker run -d <imagename:tag>

4. Access the URL on the browser:
```
http://localhost:8585/
```
