## 全局引入poetry
```
pip3 install poetry
```


## 初始化项目
```
poetry new my-project
```

## 安装依赖

在 pyproject.toml 中指定依赖,然后运行:    
eg：我们这里引入了koa      
[tool.poetry.dependencies]    
...
koa = "^0.3"    

```
poetry install

```

## 创建虚拟环境
```
poetry shell
```

## 添加依赖
使用
```
poetry add <package_name>   
```
添加新依赖，这会自动更新 pyproject.toml 和 poetry.lock。   

## 管理项目
可以使用 poetry config 修改项目名称、版本等元数据。           
使用 poetry publish 可以打包并发布项目到 PyPI。    

## 切换或退出环境
使用 poetry shell <environment_name> 切换环境。    
使用 exit 或 Ctrl+D 退出当前环境。   


## 删除环境
使用 poetry env remove <environment_name> 删除指定环境。


## PS :
python    
运行文件的时候是python xxx.py
运行模块的时候是python -m 模块名


## run

```
Pre : 
1.需要gpt4all在本地的安装准备
2.更改poe_test中本地训练数据的load地址
model = GPT4All_J('/Users/zack/Library/Application Support/nomic.ai/GPT4All/ggml-gpt4all-j-v1.3-groovy.bin')
例如，我的地址是/Users/zack/Library/Application Support/nomic.ai/GPT4All/ggml-gpt4all-j-v1.3-groovy.bin
需要改成自己的


then：
python -m poe_test


```

