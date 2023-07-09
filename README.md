# 301 Hospital: **+1 S** to our mirrors' uptime!
## How to use

1. Edit `config.ini` to set your own configuration.

For example,
```ini
[Redirect]
path = anthon
url = "http://mirrors.ustc.edu.cn/anthon/"
```

will redirect `///anthon////114514` to `http://mirrors.ustc.edu.cn/anthon/114514`.


2. noticed `port = int(os.environ.get('PORT', 80)) ` if you want to use another port.

3. 

```python
python main.py
```

