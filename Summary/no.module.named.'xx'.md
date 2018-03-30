#No module named 'exceptions'
* package
    1. package必须包含__init__.py 文件(可以为空),除非它在sys.path中某个文件夹下

* python 执行检索目录都是从sys.path中执行搜索的
    1. 你可以在sys.path.append 中添加,但是在退出python编辑器后,就会失效
    2. 你可以考虑使用环境变量PYTHONPATH,但是一旦工程量大的时候,你会感觉很乏力的
    3. 如果直接 eg：from exceptions import InvalidTokenError, 请避免内置(模块)关键字exceptions冲突
    4. 建议: 
            引用另外的package的时候,使用绝对路径package.xxx。当然，同一个package中是可以使用.xxx相对路径。这样做可以保证项目的可移植性和解耦性.

* 如果项目小且仅供测试，环境变量PYTHONPATH还是挺方便使用的。
    1. 该变量会自动加入到sys.path中去,只是多出来的配置项。
    2. 设置方法:
    win: set
    set PYTHONPATH=E:\D-desktop\project\www.test\wangDaJwt\               create
    set PYTHONPATH=%PYTHONPATH%,E:\D-desktop\project\www.test\wangDaJwt\  update warn:分隔符,逗号必须为英文的