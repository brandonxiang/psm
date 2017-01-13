# Python 笔记九：打造pypi换源加速神器psm

> 源码github地址在此，记得点星：
https://github.com/brandonxiang/psm

其实这是一个很简单的repo，是参考了[使用国内镜像源来加速python pypi包的安装](http://topmanopensource.iteye.com/blog/2004853)，对pypi下载源的配置文件进行修改。该repo受到nodejs的[nrm](https://github.com/Pana/nrm)的启发。

pypi换源加速神器，又名psm（即pypi source manager）。如今，包含了douban和aliyun的pypi同步源，我觉得这两个大网站的资源已经很够用了。如果你想加更多的第三方源，请给我发issue或者pr。

## 安装

```
pip install psm
```

## 使用

### Unix 系

##### 列出所有源

```
psm ls
```

##### 更换pypi源

```
psm use douban
```

##### 显示当前源

```
psm show
```

### Windows 系

##### 列出所有源

```
python -m psm ls
```

##### 更换pypi源

```
python -m psm use douban
```

##### 显示当前源

```
python -m psm show
```

### 路书

现在支持linux平台，windows，希望在windows系统的兼容方面要进一步提升。

如果大家想加源或者修复一些bug，可以随时issue或者pr。

转载，请表明出处。[总目录Awesome GIS](http://www.jianshu.com/p/3b3efa92dd6d)
