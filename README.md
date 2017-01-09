# 快商通
DI模块下用于接入推送数据类型的数据源所开发的服务
### 框架
tornado
### 研发须知
> Python版本：2.7.x

基于conf/offline.conf 文件复制一份以自己的用户名命名的配置放到conf目录下，并修改端口，以防止重复。

**由于该服务用于接收数据，因此测试时需要联系运维人员开放相关端口**

启动kst服务:


```
source bin/env.sh   
python kst_server.py  
```
新增配置，注意同步到app.conf文件中
依赖的所有第三方包需要添加到requirements.txt中。通过`pip install -r requirements.txt`安装依赖包

### 命名规范
Python代码规范：统一采用PEP8规范，请参考<https://www.python.org/dev/peps/pep-0008/>

统一采用utf-8编码，代码文件头部统一添加：


```
#!/usr/bin/python
# -*- coding: utf-8 -*-
```

### 部署信息

- 线下测试环境：http://172.16.34.125:19930,需要通过dev01.haizhi.com代理访问
- 线上环境：暂未上线

### 关键设计

#### 项目结构说明

```
.
├── bin
├── conf
├── env.py
├── __init__.py
├── kst_server.py
├── README.md
├── script
├── src
├── supervisord.conf
└── task.py
```
### API接口文档
接口基于http协议，所有的接口均支持GET和POST两种请求，除`api/vistorid`接口返回json格式的数据，其余接口配合快商通推送服务皆返回`ok`。

#### `api/receive` 接收访客信息

|参数名|类型|含义|是否必选|
|----|----|----|----|
|user_id|str|用户在bdp中的唯一标示|√|
|compId|str|用户在快商通的唯一标示|√|
|data|str|推送过来的数据|√|

返回结果示例：

```
ok
```
#### `api/vcard` 接收名片数据

|参数名|类型|含义|是否必选|
|----|----|----|----|
|user_id|str|用户在bdp中的唯一标示|√|
|compId|str|用户在快商通的唯一标示|√|
|data|str|推送过来的数据|√|

返回结果示例：

```
ok
```
#### `api/hisreceive` 重新接收推送失败的访客信息

|参数名|类型|含义|是否必选|
|----|----|----|----|
|user_id|str|用户在bdp中的唯一标示|√|
|compId|str|用户在快商通的唯一标示|√|
|data|str|推送过来的数据|√|

返回结果示例：

```
ok
```
#### `api/hisvcard` 重新接收推送失败的名片数据

|参数名|类型|含义|是否必选|
|----|----|----|----|
|user_id|str|用户在bdp中的唯一标示|√|
|compId|str|用户在快商通的唯一标示|√|
|data|str|推送过来的数据|√|

返回结果示例：

```
ok
```
#### `api/vistorid` 查看访客ID

|参数名|类型|含义|是否必选|
|----|----|----|----|
|user_id|str|用户在bdp中的唯一标示|√|
|compId|str|用户在快商通的唯一标示|√|
|start_date|str|开始日期|√|
|end_date|str|结束日期|√|

返回结果示例：

```
{
    "status": "0", 
    "errstr": "", 
    "result":["20c7eff34f1d4513bfd80945e7f1d63d","8ccfec024d014689a9c2f2fc4cb38eb0"]
}

```
