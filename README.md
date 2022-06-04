# TBD


## zip api

```python
pyminizip.compress(“/srcfile/path.txt”, “file_path_prefix”, “/distfile/path.zip”, “password”, int(compress_level))
```


Arguments:

src file path (string)
src file prefix path (string) or None (path to prepend to file)
dst file path (string)
password (string) or None (to create no-password zip)
compress_level(int) between 1 to 9, 1 (more fast) <—> 9 (more compress) or 0 (default)