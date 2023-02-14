# aicloud

## 配合云平台使用，如果不在平台内部，程序包没有效果

## 编译

- 安装需要的软件： python3 -m pip install --user --upgrade setuptools wheel twine
- 编译：python3 setup.py sdist bdist_wheel
- 上传到测试服务器：python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/aicloud-0.0.2-py3-none-any.whl
- 安装：python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps aicloudx
- 上传正式服务器：python3 -m twine upload dist/aicloudx-0.0.2-py3-none-any.whl 
- 安装：python3 -m pip install --index-url https://pypi.org/simple --no-deps aicloudx
- 创建存放公共数据的bucket：mc mb minio/tfdatasets
- 设置权限：mc policy set download minio/tfdatasets
- 上传数据： mc cp --recursive tensorflow_datasets minio/tfdatasets