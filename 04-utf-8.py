#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('中文测试')

s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))
