##!/usr/bin/env python
## coding:utf-8 ##
#### ʹ��Struct,Ctypes�� ####

import struct
import ctypes

nInt = int("0xe3", 16)
str = "good"

# ʮ�����������ַ���ת��
buffer = struct.pack("!H4sbB", nInt, str, 180,180)
print repr(buffer)
print struct.unpack("!H4sbB", buffer)
print

# ����ת���Ľṹ�ֽ���
print struct.calcsize("!B16B4sHIBH4sBBBHBIBB") #ת�������ֽ���
print struct.calcsize("=B16B4sHIBH4sBBBHBIBB") #����ԭ���ֽ���
print struct.calcsize("B16B4sHIBH4sBBBHBIBB")  #�Զ���������
print

# ����ʾ�����ֽ���
# ʹ��apply�Ƿ�װ�ú����ĵ��ã�����ֵ��struct.pack�ķ���ֵ
data = [4123456789, 'cd', 3]
fmt = "!I%dsb" % len(data[1])
#buffer = apply(struct.pack, ("!Icb", ) + tuple(data))  //applyʹtupleչ��Ϊ����
#                                                       //���ʽ�������ַ�������
buffer = apply(struct.pack, (fmt, ) + tuple(data)) 
print repr(buffer)
#print struct.unpack("!I2sb", buffer)
print struct.unpack("!I", buffer[:4])
print

# ���������ݵ����
buf = ctypes.create_string_buffer("hello",10)   #����char[10]
struct.pack_into("!B2sB", buf, 5, 17, "PY", 19) #��char[5]��д������
print ctypes.sizeof(buf), repr(buf.raw)         #��ʾд������Ķ����Ʊ�ʾ
print struct.unpack_from("!B2sB", buf, 5)       #��char[5]������󷵻�tuple



