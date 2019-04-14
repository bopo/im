# gobelieve vagrant
1. vagrant box add ubuntu/xenial64

2. cd $dir(Vagrantfile) && vagrant up

3. vagrant ssh

4. sudo redis-server /etc/redis.conf

5. cd /data/wwwroot/im_bin && sudo ./run.sh start

6. 获取 token

   python auth.py $uid $name

7. 群组操作
	
   	python groups.py create $master $group_name $is_super $m1 $m2 $m3...

   	python groups.py add_member $gid $m1 $m2 $m3...

   	python groups.py remove_member $gid $m1 $m2 $m3...

   	python groups.py delete $gid

   	python groups.py upgrade $gid

8. 测试
   python client.py


# 密码版本问题
mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH MYSQL_NATIVE_PASSWORD BY '123456';
mysql> FLUSH PRIVILEGES;


