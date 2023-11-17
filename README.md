# QPT-SDK
在分支中归档QPT所需的SDK，其中体积过大的SDK将被单独划分一个分支，欢迎各大厂商与开发者在本仓库中留下SDK代码或其维护的仓库地址。

## SDK制作
文档待更新...  

推荐的目录结构  
```
--版本号          # 若每个大版本都有持续维护的可能，建议设置根目录为版本号，方便后续维护。若只维护主线版本，则不需要设置该目录。
  --QPT_SDK      # SDK必要的目录结构，这样能保证用户在安装SDK后，都会存放在QPT_SDK目录下，便于打包时注册SDK。
    --SDK名      # SDK名，和其它SDK一样，存放在目录下。
      --SDK代码  # 您的SDK代码。
--setup.py      # 发布至Pypi前，需要使用该文件进行打包。
```

## 目前已适配的SDK  

### 一、官方制作SDK
#### Python SDK
[QEnvPython: Python Embedding+Tkinter SDK](https://github.com/QPT-Family/QPT-SDK/tree/G-PythonSDK)
#### Tkinter（Tk/Tcl） SDK
[QEnvPython: Python Embedding+Tkinter SDK](https://github.com/QPT-Family/QPT-SDK/tree/G-PythonSDK)
#### VCRedist 2019 SDK
[VCRedist 2019 SDK](https://github.com/QPT-Family/QPT-SDK/tree/G-PythonSDK)
### 二、开发者贡献SDK
