# psm

Pypi Source Manager: fast switch between different Pypi Source: pypi, double, aliyun, qinghua.


This package is inspired by [Pana/nrm](https://github.com/Pana/nrm).

## [中文文档](Readme_CN.md)

## Installation

```
pip install psm
```


## Usage

### Unix

##### list all pypi source

```
psm ls
```

##### change pypi source

```
psm use douban
```

or 'aliyun' and 'qinghua'

##### show current source

```
psm show
```
### Windows 

##### list all pypi source

```
python -m psm ls
```

##### change pypi source

```
python -m psm use douban
```

##### show current source

```
python -m psm show
```

## LICENSE

[MIT](LICENSE)
