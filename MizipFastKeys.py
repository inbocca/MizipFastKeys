import sys
global c
xortable = (
	('001', '09125a2589e5', 'F12C8453D821'),
	('002', 'AB75C937922F', '73E799FE3241'),
	('003', 'E27241AF2C09', 'AA4D137656AE'),
	('004', '317AB72F4490', 'B01327272DFD'),
)

def calcKey(uid, xorkey, keytype):
	p = []
	idx = {
		'A': (0,1,2,3,0,1),
		'B': (2,3,0,1,2,3),
	}.get(keytype)

	for i,j in enumerate(idx):
		p.append('%02x'% (uid[j] ^ xorkey[i]))

	return ''.join(p)

def hextostr(hexa):
	return bytes.fromhex(hexa)

def usage():
	global c
	c = input('Inserisci l\'uid della chiave..\t')
	if len(c) != 8:
		sys.exit("Lunghezza UID errata\n")

usage()


_uid = c
try:
	uid = hextostr(_uid)
except ValueError:
	print('Your UID is not a valid one')
	usage()
	sys.exit(1)	

print('+-----+-----------------------------+')
print('| UID | %s                    |' % _uid)
print('+-----+--------------+--------------+')
print('| SEC | key A        | key B        |')
print('+-----+--------------+--------------+')
print('| 000 | a0a1a2a3a4a5 | b4c132439eef |')
for sec, xorA, xorB in xortable:
	keyA = calcKey(uid, hextostr(xorA), 'A')
	keyB = calcKey(uid, hextostr(xorB), 'B')
	print('| %s | %s | %s |' % (sec, keyA, keyB))

print('+-----+--------------+--------------+')

