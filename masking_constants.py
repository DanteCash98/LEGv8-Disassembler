bMask = 0x3FFFFFF
jAddrMask = 0xFC000000
specialMask = 0x1FFFFF

#   @TO-DO
rnMask = 0x3E0 # 1st argument
rmMask = 0x3E0 # 1st argument
rdMask = 0x3E0 # 1st argument

ARM_RnrmMask = 0x1F0000  # second argument
ARM_RmrdMask = 0x1F  # destination
ARM_RdimMask = 0x3FFC00 # ARM I Immediate
shmtMask = 0xFC00 # ARM ShAMT
addrMask = 0x1FF000 # ARM address for ld and
staddr2Mask = 0xFFFFE0 # addr for CB format
imsftMask = 0x600000 # shift for IM format
imdataMask = 0x1FFFE0 # data for IM type

#   @TO-DO
negBitMask = 0x000000
extendMask = 0x000000