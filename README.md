# psm

Pypi Source Manager: fast switch between different Pypi Source: pypi, double, aliyun, tsu,.


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

or 'aliyun' and 'thu'

##### show current source

```
psm current
```

##### add a new source

```
psm add my_source https://pypi.python.org/simple
```

##### delete a source

```
psm delete my_source
```

### Windows 

##### list all pypi source

```
python -m psm ls
```

## LICENSE

[MIT](LICENSE)
