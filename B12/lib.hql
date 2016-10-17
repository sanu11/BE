
-- 1. Drop table if exists
drop table if exists librarylog;

-- 2. create a new table
create table librarylog (userid int, taskid int, unknown int, ip string, timestamp string, task string) row format delimited fields terminated by '\t'; 

-- 3. Check table schema
describe librarylog;

-- 4. Load data to table from HDFS hive directory 
load data inpath '/Pavan/LibraryLogFile.txt' into table librarylog;

-- In case you have not moved logfile to HDFS, then use below query. Word 'local' indicates file is available at local file system. 
-- load data local inpath '/home/pavan/LibraryLogFile.txt' into table librarylog;    

-- 5. Count the no of rows where userid = 4
select count(*) from librarylog where userid = 4;

-- 6. Top ten IPs who have made maximum hit to digital library server
select ip, count(ip) as totalhit from librarylog group by ip order by totalhit desc limit 10;

-- 7. Select distinct userids who have accessed task 'hadoop'
select distinct(userid) from librarylog where task like '%hadoop%';

-- 8. Check the count of 'Java' ebooks
select count(task) from librarylog where task like '%java%';

-- 9. List no of users who have accessed digital library from ip '172.16.2.105'
select distinct (userid) from librarylog where ip like '172.16.2.105';

-- 10. List the count of users who have accessed digital library on date 'Jul 08'
select count(userid) from librarylog where timestamp like '%Jul 08%'; 

-- Script ends here
