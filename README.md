# Python环境SDK
提供Embeddable版本的Python环境，在此基础上进行了以下修改：  
1. 增加pip
2. 修改_pth文件，使其能够正确获取Python库所在位置
3. 精简重复文件，进一步缩减体积（例如pip只保留一个exe）
4. 清除cache

注：旧版本环境会默认增加Tkinter与VcRedist2019的支持，该版本不再进行整合，但会默认进行安装（省得有人说QPT打包出的的东西很大，那就变成可选的吧）

## SDK用法
无须关心用法，肯定会给你配一个Python环境的。

## 备注
构建：python setup.py sdist bdist_wheel  
twine upload dist/*

发包前要在版本号后再加一个版本号