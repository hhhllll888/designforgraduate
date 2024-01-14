毕业设计项目说明
-----
## 所使用到的库
~~~
wxPython==4.2.1
tensorflow==2.14.0
numpy==1.26.1
~~~
## 文件说明

`model` 模型文件夹，里面存放模型文件  
`python-3.9.13-embed` 运行库文件，python3.9 嵌入式版本，其中 `lib` 文件夹为库文件  
`main.py` 项目主启动文件  
`model.py` 模型调用文件  
`ui.py` 界面 ui 文件  
`run.bat` windows 下主项目脚本启动文件  
## 启动方式

直接运行 run.bat 文件即可使用，打开后会卡顿运行 tensorflow 加载脚本，运行一个界面，直接放入图片文件，点击识别按钮即可识别
