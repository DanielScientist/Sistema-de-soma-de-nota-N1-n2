#notas da N1
from re import M


u1=float(input('qual foi a sua nota da primeira unidade? '))
u2=float(input('qual foi a sua nota da segunda unidade? '))
u3=float(input('qual foi a sua nota da terceira unidade? '))
u4=float(input('qual foi a sua nota da quarta unidade?'))

#soma total da N1
n1=u1+u2+u3+u4
n2=n1/4

print('dividindo a nota de todas as atividades n1,n2,n3 e n4 sua média foi {} '.format(n2))

p2=float(input('agora qual foi a nota na prova final?'))

media=n2+p2
print('sua media da n1 foi: {} e da n2 foi {} e o resultado final foi: {}'.format(n2,p2,media))

if media >= 6:
    print('você foi aprovado')
else:
        print('você foi reprovado')
    
