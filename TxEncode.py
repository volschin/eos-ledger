from asn1 import Encoder, Decoder, Numbers
import binascii

encoder = Encoder()
chain_id = binascii.unhexlify("99"*32)
expiration = binascii.unhexlify('5B30DC9A')
ref_block_num = binascii.unhexlify('3CA8')
ref_block_prefix = binascii.unhexlify('95AE4F71')
max_net_usage_words = binascii.unhexlify('00')
max_cpu_usage_ms = binascii.unhexlify('00')
delay_sec = binascii.unhexlify('00')

ctx_free_actions_size = binascii.unhexlify('00')
ctx_actions_size = binascii.unhexlify('01')
account = binascii.unhexlify('00A6823403EA3055')
name = binascii.unhexlify('0000000000A53176')
auth_size = binascii.unhexlify('01')
auth_actor = binascii.unhexlify('0000000000EA3055')
permission = binascii.unhexlify('00000000A8ED3232')
data_size = binascii.unhexlify('66')
data = binascii.unhexlify('00000000007015d640420f00000000000453595300000000046d656d6f')
data_types = binascii.hexlify('000102')
tx_ext = binascii.unhexlify('00')
cfd = binascii.unhexlify('00'*32)

encoder.start()
encoder.write(chain_id, Numbers.OctetString)
encoder.write(expiration, Numbers.OctetString)
encoder.write(ref_block_num, Numbers.OctetString)
encoder.write(ref_block_prefix, Numbers.OctetString)
encoder.write(max_net_usage_words, Numbers.OctetString)
encoder.write(max_cpu_usage_ms, Numbers.OctetString)
encoder.write(delay_sec, Numbers.OctetString)

encoder.write(ctx_free_actions_size, Numbers.OctetString)
encoder.write(ctx_actions_size, Numbers.OctetString)
encoder.write(account, Numbers.OctetString)
encoder.write(name, Numbers.OctetString)
encoder.write(auth_size, Numbers.OctetString)
encoder.write(auth_actor, Numbers.OctetString)
encoder.write(permission, Numbers.OctetString)
encoder.write(data_size, Numbers.OctetString)
encoder.write(data, Numbers.OctetString)
encoder.write(data_types, Numbers.OctetString)
encoder.write(tx_ext, Numbers.OctetString)
encoder.write(cfd, Numbers.OctetString)


encoded_bytes = encoder.output()
print binascii.hexlify(encoded_bytes)
