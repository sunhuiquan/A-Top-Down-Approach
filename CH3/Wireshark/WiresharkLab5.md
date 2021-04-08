ps:
1. 这个lab好简单。。

---
Answer:
1. 源端口，目的端口，校验和，UDP报文长度
2. 8B
3. header和payload的长度
4. 2^16 - 8 Bytes(UDP上的length是16位)(当然由于MTU这只是理论值)
5. 2^16 - 1
6. 6(TCP)和17(UDP) (看IP的protocol字段就可以了)
7. 源端口号变目的端口号，目的端口号变源端口号
