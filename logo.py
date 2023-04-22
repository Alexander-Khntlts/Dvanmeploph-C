#--> Author's Info
Author    = 'Dapunta Khurayra X'
Developer = 'Denventa Ferly Afriliyan'
Facebook  = 'Facebook.com/Denventa.Xayonara.Team.UnlimitedARMY'
Instagram = 'Instagram.com/afriliyanferlly_shishigami'
Version = '0.1'
#--> oImprt Module
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
    sp = ' '*7    print('     %s________                               %s_________                       %s__ '%(M,P))    
    print('     %s\%s______ \   ____   _______  __         \_   ___ %s\____________    ____ |  | __'%(P,M,U))
    print('     %s|    |  \_/ __ \ /    \  \/ /  ______ /    \  %s\/\_  __ \__  \ _/ ___\|  |/ / '%(P,U))
    print('     %s|    `   %s\  ___/|   |  \   /  /_____/ \     \____|  | \/%s/ __ \\  \___|    < '%(M,P,U)) 
    print('     %s/_______  /\___  >___|  /\_/            %s\______  /|__|  (____  /\___  >__|_ \  '%(P,M))
    print('     %s\/     \/     \/                       %s\/            \/     \/     \/ '%(P,U))
    print('     %s Author %s: %sDapunta Adyapaksi Ratya  %s Developer %s: %sDenventa Afriliyan Ferly  '%(U,K,M,U,K,M))
