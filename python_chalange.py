#txt="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "

txt='map'
from string import ascii_letters
from string import ascii_lowercase

shift=2
shift_ascii='yzabcdefghijklmnopqrstuvwx'
out=''
for l in txt:
    if l in ascii_lowercase:
        i=shift_ascii.index(l)
        out+=ascii_lowercase[i]
    else:
        out+=i
print(out)
