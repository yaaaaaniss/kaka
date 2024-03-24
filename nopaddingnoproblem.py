from Crypto.Util.number import * 
from pwn import * 


host = 'mercury.picoctf.net'
port = 30048

r = remote(host, port)

r.recvuntil(b'n: ')
n = r.recvline()
#print(n)

r.recvuntil(b'e: ')
e = r.recvline()
#print(e)

r.recvuntil(b'ciphertext: ')
c = r.recvline()
#print(c)

#r.interactive()

n = int(n.decode())
print(n)
e = int(e.decode())
print(e)
c = int(c.decode())
print(c)

playload = str(c + n) 

playload = playload.encode()
print(playload)

r.sendlineafter(b'Give me ciphertext to decrypt: ',playload)

#r.interactive()


r.recvuntil(b'Here you go: ')
m = r.recvline()

print(m)

#r.interactive()
m = int(m.decode())

print(long_to_bytes(m))
