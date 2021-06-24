# aicloud

## 配合云平台使用，如果不在平台内部，程序包没有效果

## 编译

- 安装需要的软件： python3 -m pip install --user --upgrade setuptools wheel twine
- 编译：python3 setup.py sdist bdist_wheel
- 上传到测试服务器：python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps aicloudx
- 上传正式服务器：python3 -m pip install --no-deps aicloudx