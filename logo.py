#--> Author's Info
Author    = 'Dapunta Adyapaksi Ratya'
Developer = 'Denventa Ferly Afriliyan'
Facebook  = 'Facebook.com/Denventa.Xayonara.Team.UnlimitedARMY'
Instagram = 'Instagram.com/afriliyanferlly_shishigami'
Version = '0.1'

#--> Import Module
import sys, time

#--> Style Warna
Z = '\x1b[38;5;232m' # Hitam
M = '\x1b[38;5;196m' # Merah
H = '\x1b[38;5;46m'  # Hijau
K = '\x1b[38;5;226m' # Kuning
B = '\x1b[38;5;44m'  # Biru
U = '\x1b[38;5;54m'  # Ungu
O = '\x1b[38;5;51m'  # Biru Muda
P = '\x1b[38;5;231m' # Putih
J = '\x1b[38;5;208m' # Jingga
A = '\x1b[38;5;248m' # Abu-Abu

#--> Animasi
def urut(i,t):
    for e in i + '\n': sys.stdout.write(e); sys.stdout.flush(); time.sleep(t)

#--> Logo
def logo():
    sp = ' '*7
    print('     %s   ________                               _________                       __ '%(M))    
    print('     %s   \______ \   ____   _______  __         \_   ___ \____________    ____ |  | __'%(M))
    print('     %s    |    |  \_/ __ \ /    \  \/ /  %s______ %s/    \  \/\_  __ \__  \ _/ ___\|  |/ / '%(M,P,M))
    print('     %s    |    `   \  ___/|   |  \   /  %s/_____/ %s\     \____|  | \// __ \\  \___|    < '%(M,P,M)) 
    print('     %s   /_______  /\___  >___|  /\_/            \______  /|__|  (____  /\___  >__|_ \  '%(M))
    print('     %s           \/     \/     \/                       \/            \/     \/     \/ '%(M))
    print('     %s Author %s: %sDapunta Adyapaksi Ratya  %s Developer %s: %sDenventa Afriliyan Ferly  '%(P,K,M,P,K,M))
