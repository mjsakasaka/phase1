## TASK 2
1. Create a new database named website.  

```
CREATE DATABASE website;
```

![img](/week5/imgs/task2-1.png)  

2. Create a new table named member, in the website database, designed as below:...  

```
CREATE TABLE member(
    id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique ID',
    name VARCHAR(255) NOT NULL COMMENT 'Name',
    username VARCHAR(255) NOT NULL COMMENT 'Username',
    password VARCHAR(255) NOT NULL COMMENT 'Password',
    follower_count INT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Follower Count',
    time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Signup Time'
);
```

![img](/imgs/task2-2.png)

## TASK 3

1. INSERT a new row to the member table where name, username and password must be set to test. INSERT additional 4 rows with arbitrary data.  

```
INSERT INTO member(name, username, password) VALUES ('test', 'test', 'test'), ('bob', 'bob', 'bob'), ('john', 'john', 'john'), ('alice', 'alice', 'alice'), ('mary', 'mary', 'mary');
```

![img](/imgs/task3-1.png)

2. SELECT all rows from the member table.  

```
SELECT * FROM member;
```

![img](/imgs/task3-2.png)

3. SELECT all rows from the member table, in descending order of time. 

```
SELECT * FROM member ORDER BY time DESC;
```

![img](/imgs/task3-3.png)

4. SELECT total 3 rows, second to fourth, from the member table, in descending order of time. Note: it does not mean SELECT rows where id are 2, 3, or 4.  

```
SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;
```

![img](/imgs/task3-4.png)

5. SELECT rows where username equals to test.  

```
SELECT * FROM member WHERE username='test';
```

![img](/imgs/task3-5.png)

6. SELECT rows where name includes the es keyword.  

```
SELECT * FROM member WHERE name LIKE '%es%';
```

![img](/imgs/task3-6.png)

7. SELECT rows where both username and password equal to test.  

```
SELECT * FROM member WHERE username='test' AND password='test';
```

![img](/imgs/task3-7.png)

8. UPDATE data in name column to test2 where username equals to test. 

```
UPDATE member SET name='test2' WHERE username='test';
```

![img](/imgs/task3-8.png)

## TASK 4

1. SELECT how many rows from the member table.

```
SELECT COUNT(*) FROM member;
```

![img](/imgs/task4-1.png)

2. SELECT the sum of follower_count of all the rows from the member table.

```
SELECT SUM(follower_count) FROM member;
```

![img](/imgs/task4-2.png)

3. SELECT the average of follower_count of all the rows from the member table.

```
SELECT AVG(follower_count) FROM member;
```

![img](/imgs/task4-3.png)

4. SELECT the average of follower_count of the first 2 rows, in descending order of follower_count, from the member table.

```
SELECT AVG(follower_count) FROM member ORDER BY follower_count DESC LIMIT 2;
```

![img](/imgs/task4-4.png)

##  TASK 5

1. Create a new table named message, in the website database. designed as below:...

```
CREATE TABLE message(
    id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique ID',
    member_id BIGINT NOT NULL COMMENT 'Member ID for Message Sender',
    content VARCHAR(255) NOT NULL COMMENT 'Content',
    like_count INT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Like Count',
    time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Publish Time',
    FOREIGN KEY(member_id) REFERENCES member(id)
);
```

![img](/imgs/task5-1.png)

2. SELECT all messages, including sender names. We have to JOIN the member table to get that.

```
SELECT message.*, member.name FROM message INNER JOIN member ON message.member_id=member.id;
```

![img](/imgs/task5-2.png)

3. SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.

```
SELECT message.*, member.name FROM message INNER JOIN member ON message.member_id=member.id WHERE member.username='test';
```

![img](/imgs/task5-3.png)

4. Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.

```
SELECT AVG(message.like_count) FROM message INNER JOIN member ON message.member_id=member.id WHERE member.username='test';
```

![img](/imgs/task5-4.png)

5. Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender username.

```
SELECT AVG(message.like_count) FROM message INNER JOIN member ON message.member_id=member.id GROUP BY member.username;
```

![img](/imgs/task5-5.png)
