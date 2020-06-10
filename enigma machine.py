#initialize
import sys
#--------------------------------------------------------------------------------------------------------------------------------------------------#
while True:
    message=[]
    encrypted=[]
    rotor1=[]
    count=0
    plugboard={'A':'A','B':'B','C':'C','D':'D','E':'E','F':'F','G':'G','H':'H','I':'I','J':'J','K':'K','L':'L','M':'M','N':'N','P':'P','Q':'Q',
               'R':'R','S':'S','T':'T','U':'U','V':'V','W':'W','X':'X','Y':'Y','Z':'Z'}#default plugboard settings
    sr=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']#static rotor
    I=['Q','W','E','R','T','Z','U','I','O','P','A','S','D','F','G','H','J','K','L','Y','X','C','V','B','N','M']#rotating rotor1
    II=['H','Q','Z','G','P','J','T','M','O','B','L','N','C','I','F','D','Y','A','W','V','E','U','S','R','K','X']#rotatingrotor2
    III=['U','Q','N','T','L','S','Z','F','M','R','E','H','D','P','X','K','I','B','V','Y','G','J','C','W','O','A']#rotatingrotor3
    IV=['E','S','O','V','P','Z','J','A','Y','Q','U','I','R','H','X','L','N','F','T','G','K','D','C','M','W','B']#rotatingrotor4
    V=['V','Z','B','R','G','I','T','Y','U','P','S','D','N','H','L','X','A','W','M','J','Q','O','F','E','C','K']#rotatingrotor5
    reflector={'A':'Y','B':'R','C':'U','D':'H','E':'Q','F':'S','G':'L','H':'D','I':'P','J':'X','K':'N','L':'G','M':'O','N':'K','O':'M',
               'P':'I','Q':'E','R':'B','S':'F','T':'Z','U':'C','V':'W','W':'V','X':'J','Y':'A','Z':'T'}#reflector
    
    #setting up the plugboard
    enterplugboardConnections=input('enter the plugboard configurations\n')
    plugboardConnections = enterplugboardConnections.split(" ")
    for pair in plugboardConnections:
        plugboard[pair[0]] = pair[1]
        plugboard[pair[1]] = pair[0]

    #choosing the rotors
    rotorset={1:I,2:II,3:III,4:IV,5:V}
    unsetrotor1=rotorset[int(input('choose rotor for slot1 '))]
    unsetrotor2=rotorset[int(input('choose rotor for slot2 '))]
    unsetrotor3=rotorset[int(input('choose rotor for slot3 '))]

    #setting up/permuting the rotors
    rotor1position=input('set rotor1 position ')
    rotor1=unsetrotor1[unsetrotor1.index(rotor1position)::]+unsetrotor1[:unsetrotor1.index(rotor1position):]#setting rotor 1
    rotor2position=input('set rotor2 position ')
    rotor2=unsetrotor2[unsetrotor2.index(rotor2position)::]+unsetrotor2[:unsetrotor2.index(rotor2position):]#setting rotor 2
    rotor3position=input('set rotor3 position ')
    rotor3=unsetrotor3[unsetrotor3.index(rotor3position)::]+unsetrotor3[:unsetrotor3.index(rotor3position):]#setting rotor 3

    #entering the message and running it through the plugboard
    print()
    n=input('type in the message and press enter to encrypt\n')
    for i in n:
        if i.upper():
            message.append(plugboard[i])

    #rotor shifting mechanism
    def shiftrotors():
        global count
        rotor1.insert(0,rotor1.pop())
        if count/26>=1 and count%26==0:
            rotor2.insert(0,rotor2.pop())
        if count/676>=1 and count%676==0:
            rotor3.insert(0,rotor3.pop())

    #encryption
    def scramble(a):
        return sr[rotor1.index(sr[rotor2.index(sr[rotor3.index(reflector[rotor3[ord(rotor2[ord(rotor1[sr.index(a)])-65])-65]])])])]

    for i in message:
        encrypted.append(plugboard[scramble(i)]) 
        count+=1
        shiftrotors()

    #output
    for i in encrypted:
        print(i,end='')
    print('\n')
    #-------------------------------------------------------------#
    print('press X to exit or enter to continue')
    n=input()
    if n=='X':
        sys.exit()
    else :
        continue
#------------------------------------------------------------------------------------------------------------------------------------------------#
