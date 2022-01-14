# ros-count
# 概要
ロボットシステム学の課題２を基に改良したものです。

カウントされ一定の値になると0になります。

# 環境
Raspberry Pi3 Model B

OS: ubuntu 20.04 server

ROS_VER=noetic

# 手順
> ## インストール


>> $cd ~/catkin_ws/src

>>$git clone git@github.com:Masashi-Okada/ros-kadai.git

>>$ catkin_make




>## 端末ごとの操作
>>#### 端末a

>>>$cd catkin_ws/src/mypkg/scripts

>>>$chmod +x count.py 

>>#### 端末b

>>>$cd catkin_ws/src

>>>$roscore

>>#### 端末c

>>>$cd catkin_ws

>>>$rosrun mypkg count.py

>>#### 端末d

>>>$cd catkin_ws

>>>$ rosrun mypkg twice.py

>>#### 端末e

>>>$rostopic echo /twice

>## 動作説明
>>2ずつ増えていき40になると0に戻ります。これをループします。

# 実行した様子
https://youtu.be/cJmko0m8ghI
# ライセンス
BSD 3-Clause License

